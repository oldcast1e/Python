from flask import Flask, jsonify
import socket
import requests
from bs4 import BeautifulSoup

# WiFi name and password
WIFI_SSID = "oldcast1e"
WIFI_PASSWORD = "dlgjstjd"

app = Flask(__name__)

# API key and bus stop IDs
key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"
arsIds = ['05251']

def getArrivalInfo(arsId):
    try:
        # Retrieve information for the given bus stop ID
        url = f'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey={key}&arsId={arsId}'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'xml')
        
        # Get bus stop name and bus arrival information
        station_name = root.find('stNm').text if root.find('stNm') else 'Unknown'
        items = root.find_all('itemList')
        
        # Variable to store bus information
        # bus_info_str = f"Station Name: {station_name}<br><br>"
        bus_info_str = f"Station Name: Sejong Univ.<br><br>"
        
        for item in items:
            bus_route_name = item.find('rtNm').text if item.find('rtNm') else 'Unknown'
            predict_msg = item.find('arrmsg1').text if item.find('arrmsg1') else 'Unknown'
            if predict_msg == '운행종료':
                bus_info_str += f'{bus_route_name}: Service ended!<br>'
            elif predict_msg == '곧 도착':
                bus_info_str += f'{bus_route_name}: Arriving soon!<br>'
            else:
                # Split the arrival message by "후"
                time, suffix = predict_msg.split('후')
                time = time.strip()  # Remove leading and trailing whitespace
                # Split the arrival time into minutes and seconds
                minutes, seconds = time.split('분')
                seconds = seconds.strip().replace('초', 'seconds')
                bus_info_str += f'{bus_route_name}: {minutes.strip()} min {seconds} after!<br>'
        
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
    # Replace '!' with '<br>' for line breaks
    bus_info = bus_info.replace('!', '<br>')
    return bus_info

if __name__ == '__main__':
    # Get the hostname and IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Set the port to be used
    port = 5001
    
    # Run the server
    print(f"Server is running at: http://{ip_address}:{port}")
    app.run(host='0.0.0.0', port=port)
