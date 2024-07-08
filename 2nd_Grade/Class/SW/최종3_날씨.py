from flask import Flask
import socket
import requests
from datetime import datetime, timedelta
import xmltodict
import pandas as pd
import threading
import time
from bs4 import BeautifulSoup

# Flask 애플리케이션을 초기화합니다
app = Flask(__name__)

# 기상 API 키와 위치 정보를 설정합니다
weather_key = 'nyVvF841UBPdCn+vugXzKE1EEwkhTBIhjhaXOQgC/AlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA=='
location_name = '광진구'  # 변경 금지

# 버스 API 키와 정류장 ID 설정
bus_key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"
arsIds = ['05251']

# 전역 변수로 날씨 정보와 버스 정보를 저장합니다
weather_info = ""
bus_info = ""
current_display = "weather"  # 현재 출력 상태: "weather" 또는 "bus"
lock = threading.Lock()

# 위치 정보를 가져오는 함수입니다
def get_location_info(location_name):
    file_path = '/Users/apple/Desktop/Python/2nd_Grade/SW/기상청41_단기예보 조회서비스_오픈API활용가이드_격자_위경도(20240101).xlsx'
    try:
        # 엑셀 파일에서 위치 정보를 읽어옵니다
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

# 현재 날짜를 YYYYMMDD 형식으로 반환하는 함수입니다
def get_current_date():
    current_date = datetime.now().date()
    return current_date.strftime("%Y%m%d")

# 기준 시간을 반환하는 함수입니다 (예보 API의 요구 형식에 맞춤)
def get_base_time():
    now = datetime.now()
    if now.minute < 30:
        base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)
    else:
        base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(minutes=30)
    return base_time.strftime("%H%M")

# 현재 날짜와 시간을 포맷하여 반환하는 함수입니다
def get_formatted_datetime():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y/%m/%d %H:%M:%S")

# 기상 상태 코드를 설명으로 변환하는 사전입니다
int_to_weather = {
    "0": "Clear",
    "1": "Rain",
    "2": "Rain/Snow",
    "3": "Snow",
    "5": "Drizzle",
    "6": "Drizzle and Snow",
    "7": "Snow Flurry"
}

# 기상 정보를 예보 API로부터 가져오는 함수입니다
def forecast(params):
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    try:
        res = requests.get(url, params)  # API 요청을 보냅니다
        res.raise_for_status()
        xml_data = res.text
        dict_data = xmltodict.parse(xml_data)  # XML 데이터를 딕셔너리로 변환합니다
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

# 날씨 정보를 주기적으로 갱신하는 함수입니다
def update_weather_info():
    global weather_info
    location_info = get_location_info(location_name)  # 위치 정보를 가져옵니다
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
        temperature, weather = forecast(params)  # 기상 정보를 가져옵니다
        if temperature and weather:
            weather_info = (f"Y{get_formatted_datetime()}<br>!"
                            f"Location: Gwangjin-gu!<br>"
                            f"Temperature: {temperature} C!<br>"
                            f"Weather: {weather}!<br>")
        else:
            weather_info = "Failed to retrieve weather information.!<br>"
    else:
        weather_info = "Failed to retrieve location information.!<br>"
    print(weather_info)
    # threading.Timer(600, update_weather_info).start()  # 10분마다 이 함수를 다시 실행합니다

# 버스 도착 정보를 가져오는 함수입니다
def getArrivalInfo(arsId):
    try:
        # 주어진 버스 정류장 ID에 대한 정보를 가져옵니다
        url = f'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey={bus_key}&arsId={arsId}'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'xml')
        
        # 버스 정류장 이름과 버스 도착 정보를 가져옵니다
        station_name = root.find('stNm').text if root.find('stNm') else 'Unknown'
        items = root.find_all('itemList')
        
        # 버스 정보를 저장할 변수
        bus_info_str = f"Station Name: Sejong Univ.!<br>"
        
        for item in items:
            bus_route_name = item.find('rtNm').text if item.find('rtNm') else 'Unknown'
            predict_msg = item.find('arrmsg1').text if item.find('arrmsg1') else 'Unknown'
            if predict_msg == '운행종료':
                bus_info_str += f'{bus_route_name}: Service ended.!<br>'
            elif predict_msg == '곧 도착':
                bus_info_str += f'{bus_route_name}: Arriving soon.!<br>'
            else:
                # 도착 메시지를 "후"로 분할
                time, suffix = predict_msg.split('후')
                time = time.strip()  # 앞뒤 공백 제거
                # 도착 시간을 분과 초로 분할
                minutes, seconds = time.split('분')
                seconds = seconds.strip().replace('초', ' sec')
                bus_info_str += f'{bus_route_name}: {minutes.strip()} min {seconds} after.!<br>'
        
        # '포천'을 'Pocheon', '구리'를 'Guri'로 대체
        bus_info_str = bus_info_str.replace('포천', 'Pocheon')
        bus_info_str = bus_info_str.replace('구리', 'Guri')
        
        return bus_info_str
    except Exception as e:
        print(f"Error fetching data for arsId {arsId}: {e}")
        return 'Error fetching bus arrival information.'

# 버스 정보를 주기적으로 갱신하는 함수입니다
def update_bus_info():
    global bus_info
    bus_info = ""
    for arsId in arsIds:
        bus_info += getArrivalInfo(arsId)
    print(bus_info)
    # threading.Timer(600, update_bus_info).start()  # 10분마다 이 함수를 다시 실행합니다

# 날씨 정보와 버스 정보 출력을 10초마다 번갈아 가며 변경하는 함수입니다
def toggle_display():
    global current_display
    while True:
        with lock:
            current_display = "bus" if current_display == "weather" else "weather"
        print(f"Current display: {current_display}")  # 현재 출력 상태를 로그에 기록
        time.sleep(10)  # 10초마다 변경

# 기본 경로에서 현재 정보를 반환하는 라우트입니다
@app.route('/')
def info_route():
    with lock:
        if current_display == "weather":
            return weather_info.replace('!', '<br>')  # 날씨 정보를 반환하기 전에 '!' 문자를 '<br>' 태그로 변경합니다
        else:
            return bus_info.replace('!', '<br>')  # 버스 정보를 반환하기 전에 '!' 문자를 '<br>' 태그로 변경합니다

if __name__ == '__main__':
    threading.Thread(target=update_weather_info).start()  # 날씨 정보 갱신 스레드 시작
    threading.Thread(target=update_bus_info).start()  # 버스 정보 갱신 스레드 시작
    threading.Thread(target=toggle_display).start()  # 출력 상태 변경 스레드 시작
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    port = 5001
    print(f"서버가 실행되었습니다: http://{ip_address}:{port}")
    app.run(host='0.0.0.0', port=port)  # 서버를 0.0.0.0 주소와 지정된 포트에서 실행합니다
