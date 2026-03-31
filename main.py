from ultralytics import YOLO
import cv2
from send import esp32

board = esp32("172.20.10.2")

model = YOLO('yolov8m.pt')
cap = cv2.VideoCapture(0)

while True:
    has_ppl = False
    print(has_ppl)
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(frame, verbose=False)
    for box in result[0].boxes:
        if box.cls[0] == 0:
            if board.is_open:
                has_ppl = True
                break
            else:
                board.open()
                has_ppl = True
                break
        
    annotated_frame = result[0].plot()
    cv2.imshow('result',annotated_frame)
    if cv2.waitKey(10) == ord('q'):
        break
    if has_ppl:
        continue
    else:
        board.close()

cap.release()
cv2.destroyAllWindows()
