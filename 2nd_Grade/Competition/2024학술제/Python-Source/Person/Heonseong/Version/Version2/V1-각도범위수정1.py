import cv2
import math
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 웹캠, 영상 파일의 경우 이것을 사용하세요.:
cap = cv2.VideoCapture(0)

def calculate_angle(x1, y1, x2, y2):
  """두 점 사이의 각도를 계산합니다."""
  dx = x2 - x1
  dy = y2 - y1
  # 역탄젠트 함수를 사용하여 라디안 값을 계산합니다.
  rad = math.atan2(dy, dx)
  # 라디안 값을 도 단위로 변환합니다.
  angle = rad * 180 / math.pi
  return angle

# 손 동작 인식 모델 설정
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("카메라를 찾을 수 없습니다.")
      break

    # 이미지 처리 및 손 인식
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # 오른손 왼손 구별
    handedness = results.multi_handedness
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # 각도 계산
        angles = []
        for landmark_pair in [[mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.THUMB_CMC],
                              [mp_hands.HandLandmark.THUMB_MCP, mp_hands.HandLandmark.THUMB_IP],
                              [mp_hands.HandLandmark.THUMB_IP, mp_hands.HandLandmark.THUMB_TIP],
                              [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.INDEX_FINGER_MCP],
                              [mp_hands.HandLandmark.INDEX_FINGER_MCP, mp_hands.HandLandmark.INDEX_FINGER_PIP],
                              [mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.INDEX_FINGER_TIP],
                              [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
                              [mp_hands.HandLandmark.MIDDLE_FINGER_MCP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP],
                              [mp_hands.HandLandmark.MIDDLE_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                              [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.RING_FINGER_MCP],
                              [mp_hands.HandLandmark.RING_FINGER_MCP, mp_hands.HandLandmark.RING_FINGER_PIP],
                              [mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.RING_FINGER_TIP],
                              [mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.PINKY_MCP],
                              [mp_hands.HandLandmark.PINKY_MCP, mp_hands.HandLandmark.PINKY_PIP],
                              [mp_hands.HandLandmark.PINKY_PIP, mp_hands.HandLandmark.PINKY_TIP]]:
          landmark_a = hand_landmarks.landmark[landmark_pair[0]]
          landmark_b = hand_landmarks.landmark[landmark_pair[1]]
          angle = calculate_angle(landmark_a.x, landmark_a.y, landmark_b.x, landmark_b.y)
          angles.append(angle)

        # 출력
        print(f'Angles: {angles}')

        # 랜드마크와 연결선 그리기
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # 이미지 표시
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

    # 종료 조건
    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()
