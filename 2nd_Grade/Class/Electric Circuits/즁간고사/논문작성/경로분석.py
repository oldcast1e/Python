import cv2

# 카메라 초기화
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임 출력
    cv2.imshow('Camera', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import torch
from ultralytics import YOLO
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import csv
import os

# YOLOv8 모델 로드
model = YOLO('yolov8n.pt')

# 노트북 카메라 초기화
cap = cv2.VideoCapture(0)

# 이동 경로를 저장할 리스트
paths = []

# 파일 경로 설정 (현재 파이썬 코드와 동일한 디렉토리)
file_path = '/Users/apple/Desktop/Python/2nd_Grade/Electric Circuits/논문작성/paths.csv'

# CSV 파일 열기
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLOv8을 사용하여 객체 감지
        results = model(frame)

        people_positions = []
        for result in results:
            for box in result.boxes:
                if int(box.cls) == 0:  # 클래스 0은 사람
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    people_positions.append((center_x, center_y))

                    # 감지된 사람 위치 표시
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

        # 현재 프레임의 사람 위치를 경로에 추가
        paths.append(people_positions)
        
        # CSV 파일에 사람 위치 저장
        for pos in people_positions:
            writer.writerow(pos)

        # 프레임 출력
        cv2.imshow('YOLOv8 Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# CSV 파일에서 경로 데이터를 불러오기
loaded_paths = []
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        loaded_paths.append((int(row[0]), int(row[1])))

# 경로 데이터 분석 및 히트맵 생성
height, width, _ = frame.shape
heatmap = np.zeros((height, width))

for pos in loaded_paths:
    heatmap[pos[1], pos[0]] += 1

# 히트맵 스무딩
heatmap = gaussian_filter(heatmap, sigma=10)

plt.imshow(heatmap, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap of People Movement')
plt.show()
