import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"

def getBusRouteId(strSrch):
    html = requests.get('http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey='+key+'&strSrch='+strSrch).text
    root = BeautifulSoup(html, 'xml')  # XML 파서를 사용하도록 수정
    try:
        bus_route = root.find('busrouteid')
        if bus_route is not None:  # busrouteid가 있는지 확인
            return bus_route.text
        else:
            return "No bus route found."
    except Exception as e:
        print(e)

# getBusRouteId('273')
# print(getBusRouteId('5003'))


def getStationList(routeid):
    html = requests.get('http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey='+key+'&busRouteId='+routeid).text
    root = BeautifulSoup(html, 'xml')
    items = root.find_all('itemlist')
    direction = root.find_all('direction')
    for i in set(direction):  
        print(f'======= 운행방향: {i.string} =======')
        for j in items:
            if j.find('direction').string == i.string:  # direction을 j.find('direction').string로 수정
                print(f'- {j.find("stationnm").string}')  # stationnm을 j.find("stationnm").string로 수정
        print()
        
# getStationList('100100049')

def getStationId(stSrch):
    html = requests.get('http://ws.bus.go.kr/api/rest/stationinfo/getStationByName?ServiceKey='+key+'&stSrch='+stSrch).text
    # root = BeautifulSoup(html, 'html.parser')
    root = BeautifulSoup(html, 'xml')
    items = root.find_all('itemlist')
    item_num = 1
    for i in items:
        print(f'====== 검색결과:{item_num} ======  ')
        print(f'정류소명:{i.stnm.string}\n고유번호:{i.arsid.string}')
        item_num += 1
    s = input('\n찾으시는 정류소의 검색결과 번호를 입력해주세요:')
    try:  #정류소 검색결과가 없거나 잘못된 번호를 선택할 경우에 대한 예외처리
        res = items[int(s)-1].arsid.string
    except Exception as e:
        print(e)
    else:
        return res
    
# getStationId('뱅뱅사거리')

def getBusTime(routeid):
    html = requests.get('http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo?ServiceKey='+key+'&busRouteId='+routeid).text
    root = BeautifulSoup(html, 'html.parser')
    first = root.find('firstbustm')
    last = root.find('lastbustm')
    term = root.find('term')
    print('====== 버스 시간 정보 ======')
    if first is not None:
        print(f'첫차시간: {first.string[8:10]}시 {first.string[10:12]}분')
    else:
        print('첫차시간 정보를 찾을 수 없습니다.')
    if last is not None:
        print(f'막차시간: {last.string[8:10]}시 {last.string[10:12]}분')
    else:
        print('막차시간 정보를 찾을 수 없습니다.')
    if term is not None:
        print(f'배차간격: {term.string}분')
    else:
        print('배차간격 정보를 찾을 수 없습니다.')

getBusTime('100100049')