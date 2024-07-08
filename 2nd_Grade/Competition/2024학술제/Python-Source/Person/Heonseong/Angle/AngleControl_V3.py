"""
서현이 형 버전
- 각 손가락의 관절 인덱스 출력


+ 반올림
+ 인덱스 출력 제거
+ 인덱스 출력 관절 인덱스 출력 후 줄 바꿈

"""

import cv2
import mediapipe as mp
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 각 손가락의 관절 인덱스
finger_joint_indices = {
    "thumb": [0, 1, 2, 3, 4],
    "index": [0, 5, 6, 7, 8],
    "middle": [0, 9, 10, 11, 12],
    "ring": [0, 13, 14, 15, 16],
    "pinky": [0, 17, 18, 19, 20]
}

# 각 손가락 관절 각도 계산 함수
def calculate_finger_angles(landmarks, finger):
    joints = [landmarks[i] for i in finger_joint_indices[finger]]
    angles = []
    for i in range(1, len(joints)-1):
        v1 = (joints[i-1].x - joints[i].x, joints[i-1].y - joints[i].y)
        v2 = (joints[i+1].x - joints[i].x, joints[i+1].y - joints[i].y)
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        magnitude_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        magnitude_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
        angle = (math.acos(dot_product / (magnitude_v1 * magnitude_v2)))
        angles.append(round(math.degrees(angle)))
    return (angles)

# 비디오 캡처 객체 생성
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

# 이전 시간 초기화
last_time = time.time()

# Mediapipe 손 추적 모델 로드
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while capture.isOpened():
        # 비디오 프레임 읽기
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        image_height, image_width, _ = frame.shape
        detected_image = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # 현재 시간
        current_time = time.time()
        
        # 이전 출력 시간으로부터 0.5초 이상 경과되었는지 확인
        if current_time - last_time >= 1:
            if detected_image.multi_hand_landmarks:
                for hand_landmarks, handedness in zip(detected_image.multi_hand_landmarks, detected_image.multi_handedness):
                    # 각 손가락의 관절 각도를 계산하여 출력
                    for finger in finger_joint_indices:
                        angles = calculate_finger_angles(hand_landmarks.landmark, finger)
                        print(angles)
                    print("\n")
            # 현재 시간을 마지막 출력 시간으로 설정
            last_time = current_time
        
        # 손 랜드마크와 연결 그리기
        if detected_image.multi_hand_landmarks:
            for hand_landmarks in detected_image.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks,
                                           mp_hands.HAND_CONNECTIONS,
                                           landmark_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(
                                               color=(255, 0, 255), thickness=4, circle_radius=2),
                                           connection_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(
                                               color=(20, 180, 90), thickness=2, circle_radius=2)
                                           )
        
        # 화면에 보여주기
        cv2.imshow('Webcam', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        
        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 비디오 캡처 해제
capture.release()
cv2.destroyAllWindows()
