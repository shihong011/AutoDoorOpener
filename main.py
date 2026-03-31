from ultralytics import YOLO
import cv2
from send import esp32

board = esp32("172.20.10.3")

model = YOLO('yolov8m.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(frame, verbose=False)
    has_ppl = False
    for box in result[0].boxes:
        if box.cls[0] == 0:
            if board.is_open:
                has_ppl = True
                break
            else:
                board.open()
                has_ppl = True
                break
            print("有人")
    has_ppl = False
    if not has_ppl:
        board.close()
        
    annotated_frame = result[0].plot()
    cv2.imshow('result',annotated_frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
