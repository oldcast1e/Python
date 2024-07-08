"""
오른손 왼손 구별 (한 손만) +  관절 구별 (출력 없음)
- 오른손 왼손 구별/ 한손만 가능 => right, left
- 손의 모양이 사각형으로 틀이 잡힘

-> 한손을 구별 할때 위상차를 판단할 때
-> 사각형 '틀'을 기준으로 중점을 잡으면, 
  공간에서 손의 상대적위치를 판단할 수 있지 않을까?
# -> 화면 공간 내의 손의 상하좌우 판단이 가능할 듯.
"""

import cv2
from cvzone.HandTrackingModule import HandDetector

# IP WebCam 어플을 사용 할 경우
# cap = cv2.VideoCapture("http://Your IP Number/video")
# WebCam 을 사용할 경우
cap = cv2.VideoCapture(0)


# 손을 감지
detector = HandDetector(maxHands=1, detectionCon=0.8)

while True:
  # 웹켐에서 프레임 가져오기
  success, img = cap.read()

  # Hands
  hands, img = detector.findHands(img)

  cv2.imshow("Image", img)

  if cv2.waitKey(1) == ord("q"): # q 누를 시 웹켐 종료
    break