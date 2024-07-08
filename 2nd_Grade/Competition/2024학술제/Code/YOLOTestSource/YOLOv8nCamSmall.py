import os
import cv2
import torch
from ultralytics import YOLO
import ssl
import certifi
import urllib.request
import time

# MPS 연산이 지원되지 않을 때 CPU로 폴백하도록 설정
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'

# SSL 인증서 문제 해결을 위한 코드
ssl_context = ssl.create_default_context(cafile=certifi.where())

# YOLOv8n 모델 다운로드 (nano 모델)
url = 'https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt'
file_path = 'yolov8n.pt'

with urllib.request.urlopen(url, context=ssl_context) as response, open(file_path, 'wb') as out_file:
    data = response.read()
    out_file.write(data)

# YOLOv8n 모델 로드
model = YOLO(file_path)

# MPS 장치 설정 (MacBook M1)
device = 'mps' if torch.backends.mps.is_available() else 'cpu'
if device == 'mps':
    print("MPS 사용 가능. 그러나 일부 연산은 CPU로 폴백될 수 있습니다.")
else:
    print("MPS 사용 불가. CPU 사용 중.")

model.to(device)

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

    # 프레임을 텐서로 변환하고 0-1 범위로 정규화하여 MPS로 이동
    frame_tensor = torch.from_numpy(frame_resized).float() / 255.0
    frame_tensor = frame_tensor.permute(2, 0, 1).unsqueeze(0)  # (HWC) -> (CHW) -> (BCHW)
    
    if device == 'mps':
        frame_tensor = frame_tensor.to(device)

    # YOLOv8 모델을 사용하여 객체 감지
    results = model(frame_tensor)
    
    # 결과를 이미지에 그리기
    annotated_frame = frame_resized.copy()
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())  # 좌표 추출
            label = f'{float(box.conf.cpu().numpy()):.2f}'  # 신뢰도 레이블을 float으로 변환
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
