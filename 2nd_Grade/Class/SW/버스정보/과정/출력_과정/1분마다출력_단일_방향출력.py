import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"

def getArrivalInfo(arsId):
    # 정류소고유번호(arsId)를 이용하여 해당 정류소의 정보를 가져옴
    html = requests.get('http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey='+key+'&arsId='+arsId).text
    root = BeautifulSoup(html, 'xml')
    # 정류소명과 버스도착정보목록을 출력
    station_name = root.find('stNm').text
    # print(f'==================== {station_name} ====================')
    # 정류소에 도착하는 버스 정보를 가져옴
    items = root.find_all('itemList')
    for item in items:
        # 버스번호, 남은시간 등의 정보를 출력
        bus_route_id = item.find('busRouteId').text
        bus_route_name = item.find('rtNm').text
        predict_msg = item.find('arrmsg1').text  # 예상 도착 메시지
        if predict_msg == '운행종료':
            print(f'{bus_route_name}: 운행종료')
        elif predict_msg == '곧 도착':
            print(f'{bus_route_name}: 곧 도착')
        else:
            # 예상 도착 시간과 "후"를 분리하여 처리
            time, suffix = predict_msg.split('후')
            time = time.strip()  # 앞뒤 공백 제거
            # 예상 도착 시간을 '분'과 '초'로 분리하여 출력
            minutes, seconds = time.split('분')
            print(f'{bus_route_name}: {minutes.strip()} 분 {seconds} 후')

# 4개의 정류소에 대해 1분마다 정보를 출력하는 함수
def main():
    arsIds = ['05251']  # 4개의 정류소고유번호
    status = 0
    while True:
        # print(f'-----------------------건대방향-----------------------\n')
        for arsId in arsIds:
            if(arsId == "05251"):
                print('[건대방향]')
            getArrivalInfo(arsId)
        time.sleep(60)  # 1분 간격으로 API 값을 불러옴

if __name__ == "__main__":
    main()
