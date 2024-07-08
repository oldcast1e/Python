import cv2
import mediapipe as mp
import math
import time

# Mediapipe 모듈을 가져옵니다.
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles  
mp_hands = mp.solutions.hands

# 웹캠 비디오를 캡처하기 위해 OpenCV를 사용합니다.
cap = cv2.VideoCapture(0)

# 손을 감지하기 위해 Mediapipe Hands 모델을 사용합니다.
# 모델 복잡도, 최소 감지 신뢰도 및 최소 추적 신뢰도를 설정할 수 있습니다.
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    # 프레임당 시간을 측정하기 위한 이전 시간을 초기화합니다.
    prev_time = time.time()

    # 웹캠이 열려 있는 동안 계속 반복합니다.
    while cap.isOpened():
        # 비디오에서 프레임을 읽어옵니다.
        success, image = cap.read()
        if not success:
            print("카메라를 찾을 수 없습니다.")
            continue

        # 이미지를 RGB 형식으로 변환합니다.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # Mediapipe Hands 모델을 사용하여 손을 처리합니다.
        results = hands.process(image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                flexion_angles = []
                # 각 손가락의 굽힘 각도를 계산합니다.
                for finger in mp_hands.HandLandmark:
		                # 각 관절의 id를 지정하여 굽힘 각도를 계산합니다.
                    joint_ids = [finger.WRIST,finger.MIDDLE_FINGER_MCP, finger.MIDDLE_FINGER_PIP, finger.MIDDLE_FINGER_DIP, finger.MIDDLE_FINGER_TIP]
                    # finger.MIDDLE_FINGER_MCP, finger.MIDDLE_FINGER_PIP, finger.MIDDLE_FINGER_DIP, finger.MIDDLE_FINGER_TIP,
                    finger_angles = []
                    for i in range(len(joint_ids) - 1): 
                        idx1, idx2 = joint_ids[i], joint_ids[i+1]
                        x1, y1, z1 = hand_landmarks.landmark[idx1].x, hand_landmarks.landmark[idx1].y, hand_landmarks.landmark[idx1].z
                        x2, y2, z2 = hand_landmarks.landmark[idx2].x, hand_landmarks.landmark[idx2].y, hand_landmarks.landmark[idx2].z
                        # 두 관절 사이의 직선거리를 구한 뒤, x축 방향의 거리를 계산하여 두 점 사이의 상대적인 각도를 얻습니다.
                        angle_rad = math.atan2(math.sqrt((y2-y1)**2 + (z2-z1)**2), x2-x1)
                        angle_deg = round(math.degrees(angle_rad), 2)
                        finger_angles.append(int(angle_deg))  # 정수로 변환하여 추가
                    flexion_angles.append(finger_angles)

                # 1초에 한 번씩 손가락 굽힘 각도를 출력합니다.
                curr_time = time.time()
                if curr_time - prev_time >= 1:
                    for angle_list in flexion_angles:
                        print(angle_list)
                        break
                    print()  # 줄바꿈
                    prev_time = curr_time  # prev_time 업데이트

                # 손가락 랜드마크를 이미지에 그립니다.
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # FPS를 계산하고 이미지에 표시합니다.
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if curr_time != prev_time else 0
        cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 화면에 이미지를 표시합니다.
        cv2.imshow('MediaPipe Hands', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # ESC 키를 누르면 프로그램을 종료합니다.
        if cv2.waitKey(1) & 0xFF == 27:
            break

# 비디오 캡처를 해제하고 창을 닫습니다.
cap.release()
cv2.destroyAllWindows()