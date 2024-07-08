from flask import Flask, jsonify
import socket
import requests
from datetime import datetime, timedelta
import xmltodict
import pandas as pd
import threading

# Flask app
app = Flask(__name__)

# Weather API key and location info
weather_key = 'nyVvF841UBPdCn+vugXzKE1EEwkhTBIhjhaXOQgC/AlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA=='
location_name = '광진구'  # 변경 금지

weather_info = ""

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
    global weather_info
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
        if temperature and weather:
            weather_info = (f"{get_formatted_datetime()}<br>"
                            f"Location: Gwangjin-gu<br>"
                            f"Temperature: {temperature}°C<br>"
                            f"Weather: {weather}<br>")
        else:
            weather_info = "Failed to retrieve weather information."
    else:
        weather_info = "Failed to retrieve location information."
    print(weather_info)
    threading.Timer(30, update_weather_info).start()

@app.route('/')
def weather_info_route():
    global weather_info
    return weather_info

if __name__ == '__main__':
    update_weather_info()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    port = 5001
    print(f"서버가 실행되었습니다: http://{ip_address}:{port}")
    app.run(host='0.0.0.0', port=port)
