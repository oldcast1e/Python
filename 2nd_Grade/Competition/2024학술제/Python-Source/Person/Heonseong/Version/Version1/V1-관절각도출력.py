import cv2
import mediapipe as mp
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 웹캠을 사용할 경우:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    prev_time = 0
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
                for i in range(4, 20, 4):  # 관절 인덱스 4부터 20까지 4씩 증가하여 4개씩 묶음
                    x1, y1 = hand_landmarks.landmark[i-3].x, hand_landmarks.landmark[i-3].y
                    x2, y2 = hand_landmarks.landmark[i-2].x, hand_landmarks.landmark[i-2].y
                    x3, y3 = hand_landmarks.landmark[i-1].x, hand_landmarks.landmark[i-1].y
                    x4, y4 = hand_landmarks.landmark[i].x, hand_landmarks.landmark[i].y

                    angle = math.degrees(math.acos(
                        ((x2-x1)*(x4-x3) + (y2-y1)*(y4-y3)) /
                        (math.sqrt((x2-x1)**2+(y2-y1)**2) * math.sqrt((x4-x3)**2+(y4-y3)**2))
                    ))
                    flexion_angles.append(angle)

                # 각 관절의 굽힘 정도 출력
                print("Flexion angles (degrees):", flexion_angles)

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('MediaPipe Hands', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
