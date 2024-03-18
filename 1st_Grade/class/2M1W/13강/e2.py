import webbrowser

search = input("찾고싶은 음식점을 입력하세요(호텔/커피숍/음식점): ")

la =input("위도를 입력하세요: ")
lon= input("경도를 입력하세요: ")

url = 'https://www.google.co.kr/maps/'
url += 'search/' + search
url += '/@' + la +','+lon+','+'15z'

webbrowser.open(url)