# 4개의 정류소에 대해 1분마다 정보를 출력하는 함수
def main():
    arsIds = ['05251']  # 4개의 정류소고유번호
    status = 0
    while True:
        for arsId in arsIds:
            getArrivalInfo(arsId)
        time.sleep(60)  # 1분 간격으로 API 값을 불러옴