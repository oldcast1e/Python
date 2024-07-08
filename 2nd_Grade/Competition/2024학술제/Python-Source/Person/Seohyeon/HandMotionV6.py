import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 손의 동작을 감지하는 함수
def detect_hand_gesture(landmarks_list):
    # 모든 손가락 끝이 손바닥보다 위에 있으면 "UP"
    fingers_up = [landmarks_list[i].y < landmarks_list[0].y for i in range(4, 21, 4)]
    if all(fingers_up):
        return "GO UP"
    # 모든 손가락 끝이 손바닥보다 아래에 있으면 "DOWN"
    fingers_down = [landmarks_list[i].y > landmarks_list[0].y for i in range(4, 21, 4)]
    if all(fingers_down):
        return "GO DOWN"
    # 모든 손가락 끝이 손바닥보다 오른쪽에 있으면 "RIGHT"
    fingers_right = [landmarks_list[i].x > landmarks_list[0].x for i in range(4, 21, 4)]
    if all(fingers_right):
        return "GO RIGHT"
    # 모든 손가락 끝이 손바닥보다 왼쪽에 있으면 "LEFT"
    fingers_left = [landmarks_list[i].x < landmarks_list[0].x for i in range(4, 21, 4)]
    if all(fingers_left):
        return "GO LEFT"
    # 그 외의 경우는 "STOP"
    return "STOP"

# 비디오 캡처 객체 생성
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

# Mediapipe 손 추적 모델 로드
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while capture.isOpened():
        # 비디오 프레임 읽기
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detected_image = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if detected_image.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(detected_image.multi_hand_landmarks, detected_image.multi_handedness):
                # 손의 랜드마크와 연결을 그립니다.
                mp_drawing.draw_landmarks(image, hand_landmarks,
                                           mp_hands.HAND_CONNECTIONS,
                                           landmark_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(
                                               color=(255, 0, 255), thickness=4, circle_radius=2),
                                           connection_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(
                                               color=(20, 180, 90), thickness=2, circle_radius=2)
                                           )
                
                # 손동작 감지
                landmarks_list = hand_landmarks.landmark
                hand_gesture = detect_hand_gesture(landmarks_list)
                
                # 손동작 표시
                if hand_gesture != "OTHER":
                    # 손동작을 손 옆에 표시
                    hand_x = int(landmarks_list[0].x * image.shape[1])
                    hand_y = int(landmarks_list[0].y * image.shape[0])
                    cv2.putText(image, hand_gesture, (hand_x, hand_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    
                    # 손의 라벨 표시
                    hand_label = handedness.classification[0].label
                    cv2.putText(image, hand_label, (hand_x, hand_y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # 화면에 보여주기
        cv2.imshow('Webcam', image)
        
        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 비디오 캡처 해제
capture.release()
cv2.destroyAllWindows()
