import requests
from datetime import datetime, timedelta
import xmltodict
import pandas as pd

def get_current_date():
    current_date = datetime.now().date()
    return current_date.strftime("%Y%m%d")

def get_base_time():
    now = datetime.now()
    # 기상청 API는 보통 매 정시와 30분에 데이터가 제공됩니다.
    if now.minute < 30:
        base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)
    else:
        base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(minutes=30)
    return base_time.strftime("%H%M")

def get_formatted_datetime():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y/%m/%d %H:%M:%S")

int_to_weather = {
    "0": "맑음",
    "1": "비",
    "2": "비/눈",
    "3": "눈",
    "5": "빗방울",
    "6": "빗방울눈날림",
    "7": "눈날림"
}

def forecast(params):
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'  # 초단기예보
    try:
        # API 요청
        res = requests.get(url, params)
        res.raise_for_status()

        # XML -> 딕셔너리
        xml_data = res.text
        dict_data = xmltodict.parse(xml_data)

        # 응답 데이터에서 필요한 정보 추출
        for item in dict_data['response']['body']['items']['item']:
            if item['category'] == 'T1H':
                temp = item['obsrValue']
            if item['category'] == 'PTY':
                sky = item['obsrValue']

        sky = int_to_weather.get(sky, "알 수 없음")
        return temp, sky
    except requests.exceptions.RequestException as e:
        return None, None
    except KeyError as e:
        return None, None

def get_location_info(location_name):
    # Load the Excel file
    file_path = '/Users/apple/Desktop/Python/2nd_Grade/SW/기상청41_단기예보 조회서비스_오픈API활용가이드_격자_위경도(20240101).xlsx'
    try:
        data = pd.read_excel(file_path, sheet_name='최종 업데이트 파일_20240101')

        # Filter for the location
        location_info = data[data['2단계'] == location_name]
        if not location_info.empty:
            return location_info[['격자 X', '격자 Y', '경도(초/100)', '위도(초/100)']].iloc[0]
        else:
            print("위치 정보를 찾을 수 없습니다.")
            return None
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return None

# 광진구의 위치 정보 가져오기
location_name = '광진구'
location_info = get_location_info(location_name)

if location_info is not None:
    keys = 'nyVvF841UBPdCn+vugXzKE1EEwkhTBIhjhaXOQgC/AlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA=='

    params = {
        'serviceKey': keys,
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
        print(f"현재 위치: {location_name}")
        print(f"현재 날짜 및 시간: {get_formatted_datetime()}")
        #print(f"격자 좌표: ({location_info['격자 X']}, {location_info['격자 Y']})")
        #print(f"경도: {location_info['경도(초/100)']}, 위도: {location_info['위도(초/100)']}")
        print(f"현재 기온: {temperature}°C")
        print(f"현재 날씨: {weather}")
    else:
        print("날씨 정보를 가져오는 데 실패했습니다.")
else:
    print("위치 정보를 가져오는 데 실패했습니다.")
