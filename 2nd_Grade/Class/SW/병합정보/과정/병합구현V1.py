from flask import Flask, jsonify
import socket
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import xmltodict
import pandas as pd
import threading
import time

# Flask app
app = Flask(__name__)

# WiFi name and password
WIFI_SSID = "oldcast1e"
WIFI_PASSWORD = "dlgjstjd"

# API key and bus stop IDs
bus_key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"
arsIds = ['05251']

# Weather API key and location info
weather_key = 'nyVvF841UBPdCn+vugXzKE1EEwkhTBIhjhaXOQgC/AlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA=='
location_name = '광진구'
location_info = None

weather_info = ""
current_display = "bus"  # Current display state: "bus" or "weather"
lock = threading.Lock()

def get_location_info(location_name):
    file_path = '/Users/apple/Desktop/Python/2nd_Grade/SW/기상청41_단기예보 조회서비스_오픈API활용가이드_격자_위경도(20240101).xlsx'
    try:
        data = pd.read_excel(file_path, sheet_name='최종 업데이트 파일_20240101')
        location_info = data[data['2단계'] == location_name]
        if not location_info.empty:
            return location_info[['격자 X', '격자 Y', '경도(초/100)', '위도(초/100)']].iloc[0]
        else:
            print("Location information not found.")
            return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def get_current_date():
    current_date = datetime.now().date()
    return current_date.strftime("%Y%m%d")

def get_base_time():
    now = datetime.now()
    if now.minute < 30:
        base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)
    else:
        base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(minutes=30)
    return base_time.strftime("%H%M")

def get_formatted_datetime():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y/%m/%d %H:%M:%S")

int_to_weather = {
    "0": "Clear",
    "1": "Rain",
    "2": "Rain/Snow",
    "3": "Snow",
    "5": "Drizzle",
    "6": "Drizzle and Snow",
    "7": "Snow Flurry"
}

def forecast(params):
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    try:
        res = requests.get(url, params)
        res.raise_for_status()
        xml_data = res.text
        dict_data = xmltodict.parse(xml_data)
        for item in dict_data['response']['body']['items']['item']:
            if item['category'] == 'T1H':
                temp = item['obsrValue']
            if item['category'] == 'PTY':
                sky = item['obsrValue']
        sky = int_to_weather.get(sky, "Unknown")
        return temp, sky
    except requests.exceptions.RequestException as e:
        return None, None
    except KeyError as e:
        return None, None

def update_weather_info():
    global weather_info, location_info
    while True:
        location_info = get_location_info(location_name)
        if location_info is not None:
            params = {
                'serviceKey': weather_key,
                'pageNo': '1',
                'numOfRows': '10',
                'dataType': 'XML',
                'base_date': get_current_date(),
                'base_time': get_base_time(),
                'nx': int(location_info['격자 X']),
                'ny': int(location_info['격자 Y'])
            }
            temperature, weather = forecast(params)
            with lock:
                if temperature and weather:
                    weather_info = (f"{get_formatted_datetime()}<br>"
                                    f"Location: Gwangjin-gu<br>"
                                    f"Temperature: {temperature}°C<br>"
                                    f"Weather: {weather}<br>")
                else:
                    weather_info = "Failed to retrieve weather information."
        else:
            weather_info = "Failed to retrieve location information."
        time.sleep(30)

def getArrivalInfo(arsId):
    try:
        url = f'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey={bus_key}&arsId={arsId}'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'xml')
        station_name = root.find('stNm').text if root.find('stNm') else 'Unknown'
        items = root.find_all('itemList')
        bus_info_str = f"Station Name: Sejong Univ.<br><br>"
        for item in items:
            bus_route_name = item.find('rtNm').text if item.find('rtNm') else 'Unknown'
            predict_msg = item.find('arrmsg1').text if item.find('arrmsg1') else 'Unknown'
            if predict_msg == '운행종료':
                bus_info_str += f'{bus_route_name}: Service ended!<br>'
            elif predict_msg == '곧 도착':
                bus_info_str += f'{bus_route_name}: Arriving soon!<br>'
            else:
                time, suffix = predict_msg.split('후')
                time = time.strip()
                minutes, seconds = time.split('분')
                seconds = seconds.strip().replace('초', 'seconds')
                bus_info_str += f'{bus_route_name}: {minutes.strip()} min {seconds} after!<br>'
        bus_info_str = bus_info_str.replace('포천', 'Pocheon')
        bus_info_str = bus_info_str.replace('구리', 'Guri')
        return bus_info_str
    except Exception as e:
        print(f"Error fetching data for arsId {arsId}: {e}")
        return 'Error fetching bus arrival information.'

def toggle_display():
    global current_display
    while True:
        with lock:
            current_display = "weather" if current_display == "bus" else "bus"
        time.sleep(30)

@app.route('/')
def bus_info_route():
    with lock:
        if current_display == "bus":
            bus_info = ""
            for arsId in arsIds:
                bus_info += getArrivalInfo(arsId)
            return bus_info
        else:
            return weather_info

if __name__ == '__main__':
    threading.Thread(target=update_weather_info).start()
    threading.Thread(target=toggle_display).start()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    port = 5001
    print(f"Server is running at: http://{ip_address}:{port}")
    app.run(host='0.0.0.0', port=port)
