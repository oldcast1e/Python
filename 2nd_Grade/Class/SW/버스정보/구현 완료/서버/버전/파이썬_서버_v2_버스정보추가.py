from flask import Flask, jsonify
import socket
import requests
from bs4 import BeautifulSoup

# 와이파이 이름과 비밀번호를 여기에 입력하세요
WIFI_SSID = "oldcast1e"
WIFI_PASSWORD = "dlgjstjd"

app = Flask(__name__)

# API 키와 정류소 ID 설정
key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"
arsIds = ['05251']

def getArrivalInfo(arsId):
    try:
        # 정류소 고유번호(arsId)를 이용하여 해당 정류소의 정보를 가져옴
        url = f'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey={key}&arsId={arsId}'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'xml')
        
        # 정류소명과 버스도착정보목록을 출력
        station_name = root.find('stNm').text if root.find('stNm') else 'Unknown'
        items = root.find_all('itemList')
        
        # 버스 정보를 저장할 문자열 변수
        bus_info_str = f"정류소명: {station_name}\n"
        
        for item in items:
            bus_route_name = item.find('rtNm').text if item.find('rtNm') else 'Unknown'
            predict_msg = item.find('arrmsg1').text if item.find('arrmsg1') else 'Unknown'
            if predict_msg == '운행종료':
                bus_info_str += f'{bus_route_name}: 운행종료!\n'
            elif predict_msg == '곧 도착':
                bus_info_str += f'{bus_route_name}: 곧 도착!\n'
            else:
                # 예상 도착 시간과 "후"를 분리하여 처리
                time, suffix = predict_msg.split('후')
                time = time.strip()  # 앞뒤 공백 제거
                # 예상 도착 시간을 '분'과 '초'로 분리하여 출력
                minutes, seconds = time.split('분')
                bus_info_str += f'{bus_route_name}: {minutes.strip()} 분 {seconds} 후!\n'
        
        return bus_info_str
    except Exception as e:
        print(f"Error fetching data for arsId {arsId}: {e}")
        return 'Error fetching bus arrival information.'

@app.route('/')
def bus_info_route():
    bus_info = ""
    for arsId in arsIds:
        bus_info += getArrivalInfo(arsId)
        print(f"Fetched data for arsId {arsId}: {bus_info}")
    # '!' 문자를 '\n'으로 대체하여 줄 바꿈 처리
    bus_info = bus_info.replace('!', '\n')
    return bus_info

if __name__ == '__main__':
    # 호스트 이름을 가져와 IP 주소를 확인
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # 사용할 포트를 설정
    port = 5001
    
    # 서버 실행
    print(f"서버가 실행되었습니다: http://{ip_address}:{port}")
    app.run(host='0.0.0.0', port=port)
