import cv2
import math
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 웹캠, 영상 파일의 경우 이것을 사용하세요.:
cap = cv2.VideoCapture(0)

def calculate_angles(hand_landmarks):
  """손 랜드마크에서 각도를 계산하고 배열에 저장합니다."""
  angles = []
  for landmark_triplet in [[mp_hands.HandLandmark.WRIST, mp_hands.HandLandmark.THUMB_CMC, mp_hands.HandLandmark.THUMB_MCP],
                          # ...
                          ]:
    landmark_a = hand_landmarks.landmark[landmark_triplet[0]]
    landmark_b = hand_landmarks.landmark[landmark_triplet[1]]
    landmark_c = hand_landmarks.landmark[landmark_triplet[2]]

    # 벡터 AB와 벡터 BC의 내적을 계산합니다.
    dot_product = (landmark_b.x - landmark_a.x) * (landmark_c.x - landmark_b.x) + \
                  (landmark_b.y - landmark_a.y) * (landmark_c.y - landmark_b.y)

    # 벡터 AB와 벡터 BC의 크기를 계산합니다.
    magnitude_ab = math.sqrt((landmark_b.x - landmark_a.x)**2 + (landmark_b.y - landmark_a.y)**2)
    magnitude_bc = math.sqrt((landmark_c.x - landmark_b.x)**2 + (landmark_c.y - landmark_b.y)**2)

    # 코사인 법칙을 사용하여 각도를 계산합니다.
    cos_angle = dot_product / (magnitude_ab * magnitude_bc)
    angle = math.acos(cos_angle) * 180 / math.pi

    # 0~180도 범위 내의 값으로 변환합니다.
    if angle > 180:
      angle = 360 - angle

    # 각도 배열에 추가합니다.
    angles.append(angle)

  return angles


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
        angles = calculate_angles(hand_landmarks)  # Pass only hand_landmarks

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
