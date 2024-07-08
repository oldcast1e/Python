import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import serial

key = "nyVvF841UBPdCn%2BvugXzKE1EEwkhTBIhjhaXOQgC%2FAlD2F0YongS3tfgXgIxbW5lmlkuJ6Szjamn18IPVNMpXA%3D%3D"

# # Arduino serial port and baud rate settings
# serial_port = "/dev/tty.usbserial-0001"
# baud_rate = 115200

# # Connect to the serial port
# ard = serial.Serial(serial_port, baud_rate)

def getArrivalInfo(arsId):
    # Retrieve information for the given bus stop ID
    html = requests.get('http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey='+key+'&arsId='+arsId).text
    root = BeautifulSoup(html, 'xml')
    # Get bus stop name and bus arrival information
    station_name = root.find('stNm').text
    # Retrieve bus information arriving at the bus stop
    items = root.find_all('itemList')
    
    # Variable to store bus information
    bus_info_str = ""
    
    for item in items:
        # Print bus number, remaining time, etc.
        bus_route_id = item.find('busRouteId').text
        bus_route_name = item.find('rtNm').text
        predict_msg = item.find('arrmsg1').text  # Predicted arrival message
        if predict_msg == '운행종료':
            bus_info_str += f'{bus_route_name}: Service ended!\n'
        elif predict_msg == '곧 도착':
            bus_info_str += f'{bus_route_name}: Arriving soon!\n'
        else:
            # Split the arrival message by "후"
            time, suffix = predict_msg.split('후')
            time = time.strip()  # Remove leading and trailing whitespace
            # Split the arrival time into minutes and seconds
            minutes, seconds = time.split('분')
            bus_info_str += f'{bus_route_name}: {minutes.strip()} min {seconds} after!\n'
    
    # Return the string with all bus information
    return bus_info_str

# Function to print information for 4 bus stops every minute
def main():
    arsIds = ['05251']  # 4 bus stop IDs
    status = 0
    while True:
        for arsId in arsIds:
            rst = getArrivalInfo(arsId)
            print(rst)
            # ard.write(rst.encode())  # Encode string to bytes and send to serial port
            # ard.write(rst)
        time.sleep(10)  # Fetch API values at 1-minute intervals

if __name__ == "__main__":
    main()
