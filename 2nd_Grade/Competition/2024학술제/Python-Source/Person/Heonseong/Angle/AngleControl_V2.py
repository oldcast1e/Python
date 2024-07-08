"""

"""
import cv2
import mediapipe as mp
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles  
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

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
                # 각 손가락의 굽힘 각도 계산
                for finger in mp_hands.HandLandmark:
                    joint_ids = [finger.MIDDLE_FINGER_MCP, finger.MIDDLE_FINGER_PIP, 
                                 finger.MIDDLE_FINGER_DIP, finger.MIDDLE_FINGER_TIP];#중지
    
                    finger_angles = []
                    for i in range(len(joint_ids) - 1):
                        idx1, idx2 = joint_ids[i], joint_ids[i+1]
                        x1, y1, z1 = hand_landmarks.landmark[idx1].x, hand_landmarks.landmark[idx1].y, hand_landmarks.landmark[idx1].z
                        x2, y2, z2 = hand_landmarks.landmark[idx2].x, hand_landmarks.landmark[idx2].y, hand_landmarks.landmark[idx2].z
                        angle_rad = math.atan2(math.sqrt((y2-y1)**2 + (z2-z1)**2), x2-x1)
                        angle_deg = round(math.degrees(angle_rad), 2)
                        finger_angles.append(int(angle_deg))  # 정수로 변환하여 추가
                    flexion_angles.append(finger_angles)

                curr_time = time.time()
                if curr_time - prev_time >= 1:  # 1초에 한 번 출력
                    # print("Flexion angles (degrees):")
                    for finger_angle in flexion_angles:
                        print(finger_angle,end="\n")
                        break
                    print(',',end="\n")  # 줄바꿈
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