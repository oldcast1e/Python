import cv2
import yolov5

# YOLOv5 모델 로드
# model = yolov5.load_model("yolov5s.pt")

from yolov5.models import load_model
model = load_model("yolov5s.pt")


# 웹캠 캡처 시작
cap = cv2.VideoCapture(0)

while True:
    # 웹캠으로부터 프레임 읽어오기
    ret, frame = cap.read()

    # YOLOv5으로 객체 인식 수행
    results = model(frame)

    # 결과 시각화
    for result in results.xyxy:
        x1, y1, x2, y2 = result.astype("int")
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 결과 프레임 출력
    cv2.imshow("YOLOv5 Hands", frame)

    # 키 입력 처리
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
