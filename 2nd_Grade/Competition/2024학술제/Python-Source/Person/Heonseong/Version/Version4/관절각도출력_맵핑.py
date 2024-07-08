"""
손가락 관절 맵핑
오류 발생

"""
import cv2
import mediapipe as mp
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# 손가락 노드에 대한 맵핑 이름 설정
finger_mapping = ["WRIST", "THUMB_CMC", "THUMB_MCP", "THUMB_IP", "THUMB_TIP",
                  "INDEX_FINGER_MCP", "INDEX_FINGER_PIP", "INDEX_FINGER_DIP", "INDEX_FINGER_TIP",
                  "MIDDLE_FINGER_MCP", "MIDDLE_FINGER_PIP", "MIDDLE_FINGER_DIP", "MIDDLE_FINGER_TIP",
                  "RING_FINGER_MCP", "RING_FINGER_PIP", "RING_FINGER_DIP", "RING_FINGER_TIP",
                  "PINKY_MCP", "PINKY_PIP", "PINKY_DIP", "PINKY_TIP"]

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    prev_time = time.time()
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("카메라를 찾을 수 없습니다.")
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                flexion_angles = []
                # 각 손가락의 굽힘 각도 계산 및 맵핑된 이름으로 저장
                for finger_idx, finger_name in enumerate(finger_mapping):
                    joint = hand_landmarks.landmark[finger_idx]
                    if joint.visibility < 0 or joint.presence < 0:
                        flexion_angles.append(-1)  # 각 관절의 visibility나 presence가 없을 때 -1로 처리
                    else:
                        flexion_angles.append(int(joint.direction.y * 180))  # 관절의 각도를 정수형으로 변환하여 저장

                curr_time = time.time()
                if curr_time - prev_time >= 1:  # 1초에 한 번 출력
                    print("Flexion angles (degrees):")
                    for finger_name, angle in zip(finger_mapping, flexion_angles):
                        print(f"{finger_name}: {angle}")
                    print(',')  # 줄바꿈
                    prev_time = curr_time

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('MediaPipe Hands', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
