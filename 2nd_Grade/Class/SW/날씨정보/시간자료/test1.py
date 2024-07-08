import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# API 요청에 필요한 정보
api_key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"
endpoint = "http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList"
start_date = "20240101"
end_date = "20250101"
station_id = "108"

# API 요청 보내기
params = {
    "serviceKey": api_key,
    "pageNo": 1,
    "numOfRows": 10,
    "dataType": "XML",
    "dataCd": "ASOS",
    "dateCd": "HR",
    "startDt": start_date,
    "endDt": end_date,
    "stnIds": station_id
}

response = requests.get(endpoint, params=params)

# 응답 확인
if response.status_code == 200:
    root = ET.fromstring(response.content)
    today = datetime.now().strftime("%Y-%m-%d")
    
    found_today = False
    for item in root.findall('.//item'):
        obs_date = item.find('tm').text.split()[0]
        if obs_date == today:
            temperature = item.find('ta').text
            humidity = item.find('hm').text
            wind_speed = item.find('ws').text
            print(f"오늘({today})의 날씨 정보:")
            print(f"기온: {temperature}°C, 습도: {humidity}%, 풍속: {wind_speed}m/s")
            found_today = True
    
    if not found_today:
        print(f"{today}의 날씨 정보가 없습니다.")
else:
    print("API 요청이 실패하였습니다. 상태 코드:", response.status_code)
