from ultralytics import YOLO
import cv2
from send import esp32

board = esp32("172.20.10.2")

model = YOLO('yolov8m.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(frame, verbose=False)
    has_person = False
    for box in result[0].boxes:
        if box.cls[0] == 0:
            #board.open()
            print("有人")
            has_person = True
            break
    if not has_person:
        print("沒人")
    annotated_frame = result[0].plot()
    cv2.imshow('result',annotated_frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
