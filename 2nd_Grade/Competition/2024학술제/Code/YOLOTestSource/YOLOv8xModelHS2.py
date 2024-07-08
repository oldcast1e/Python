import cv2
from ultralytics import YOLO
import ssl
import certifi
import urllib.request
import time

# SSL 인증서 문제 해결을 위한 코드
ssl_context = ssl.create_default_context(cafile=certifi.where())

# YOLOv8x 모델 다운로드 (extra-large 모델)
url = 'https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x.pt'
file_path = 'yolov8x.pt'

with urllib.request.urlopen(url, context=ssl_context) as response, open(file_path, 'wb') as out_file:
    data = response.read()
    out_file.write(data)

# YOLOv8x 모델 로드
model = YOLO(file_path)

# 웹캠 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    start_time = time.time()
    
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    # 프레임 크기 줄이기 (성능 최적화)
    frame_resized = cv2.resize(frame, (640, 480))

    # YOLOv8 모델을 사용하여 객체 감지
    results = model(frame_resized)
    
    # 결과를 이미지에 그리기
    annotated_frame = frame_resized.copy()
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 좌표 추출
            label = f'{float(box.conf):.2f}'  # 신뢰도 레이블을 float으로 변환
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 박스 그리기
            cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # 레이블 추가
    
    # FPS 계산 및 출력
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 이미지 출력
    cv2.imshow('YOLOv8 Real-time Object Detection', annotated_frame)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
