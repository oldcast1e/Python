import requests

def get_bus_arrival_info(station_id):
    service_url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUidItem"
    params = {
        "serviceKey": "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D",
        "arsId": station_id  # 정류소 ID
    }
    response = requests.get(service_url, params=params)
    if response.status_code == 200:
        try:
            # 응답을 JSON으로 변환
            json_response = response.json()
            # 응답 처리
            arrivals = json_response["ServiceResult"]["msgBody"]["itemList"]
            if arrivals:
                print("도착 예정 버스 목록:")
                for arrival in arrivals:
                    route_id = arrival["busRouteId"]
                    route_name = arrival["busRouteNm"]
                    arrival_time = arrival["arrmsg1"]
                    print(f"노선 ID: {route_id}, 노선 이름: {route_name}, 도착 예정 시간: {arrival_time}")
            else:
                print("도착 예정 버스가 없습니다.")
        except Exception as e:
            print("응답 처리 중 오류 발생:", e)
    else:
        print("에러:", response.status_code)

# 정류소 ID가 05251인 경우 버스 도착 정보 조회
get_bus_arrival_info("05251")
