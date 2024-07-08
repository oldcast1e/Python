import requests

def get_route_by_station_list(station_id):
    service_url = "http://ws.bus.go.kr/api/rest/stationinfo/getRouteByStation"
    params = {
        "serviceKey": "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D",
        "arsId": station_id,  # 정류소 ID
        "numOfRows": 10  # 조회할 노선 개수, 필요에 따라 조절 가능
    }
    response = requests.get(service_url, params=params)
    if response.status_code == 200:
        # 응답 처리
        routes = response.json()["ServiceResult"]["msgBody"]["itemList"]
        for route in routes:
            route_id = route["busRouteId"]
            route_name = route["busRouteNm"]
            print(f"노선 ID: {route_id}, 노선 이름: {route_name}")
    else:
        print("Error:", response.status_code)

# 정류소의 경유하는 노선 목록 조회 예시
get_route_by_station_list("05251")
