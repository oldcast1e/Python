import requests
from datetime import datetime, timedelta
import xmltodict
import pandas as pd

def get_current_date():
    current_date = datetime.now().date()
    return current_date.strftime("%Y%m%d")

def get_base_time():
    now = datetime.now()
    # KMA API typically provides data every hour and at the 30-minute mark.
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
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'  # Ultra short-term forecast
    try:
        # API request
        res = requests.get(url, params)
        res.raise_for_status()

        # XML -> Dictionary
        xml_data = res.text
        dict_data = xmltodict.parse(xml_data)

        # Extract necessary information from the response data
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
            print("Location information not found.")
            return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Get location information for Gwangjin-gu
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
        # print(f"Current date and time: {get_formatted_datetime()}")
        print(f"{get_formatted_datetime()}") 
        print("")

        # print(f"Current location: {location_name}")
        print(f"location: Gwangjin-gu")

        #print(f"Grid coordinates: ({location_info['격자 X']}, {location_info['격자 Y']})")
        #print(f"Longitude: {location_info['경도(초/100)']}, Latitude: {location_info['위도(초/100)']}")
        
        # print(f"Current temperature: {temperature}°C")
        print(f"temperature: {temperature}°C")
        # print(f"Current weather: {weather}")
        print(f"weather: {weather}")
    else:
        print("Failed to retrieve weather information.")
else:
    print("Failed to retrieve location information.")