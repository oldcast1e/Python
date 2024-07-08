from flask import Flask
import socket

# 와이파이 이름과 비밀번호를 여기에 입력하세요
WIFI_SSID = "oldcast1e"
WIFI_PASSWORD = "dlgjstjd"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO WORLD!'

if __name__ == '__main__':
    # 호스트 이름을 가져와 IP 주소를 확인
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # 사용할 포트를 설정
    port = 5001
    
    # 서버 실행
    print(f"서버가 실행되었습니다: http://{ip_address}:{port}")
    app.run(host='0.0.0.0', port=port)