#입력 문자로 웹 브라우저 열기
import webbrowser
u = input("검색할 단어를 입력하세요: ")
url = 'https://search.naver.com/'
url += 'search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%s'%u
webbrowser.open(url)