# load yolov8 model
from ultralytics import YOLO
import cv2

model = YOLO("yolov8m.pt")


#load video
#video_path = "https://www.youtube.com/watch?v=KBsqQez-O4w"
video_path = './images/car.mp4'
cap = cv2.VideoCapture(video_path)

# read frames
ret = True
while ret:
    ret, frame = cap.read()
    
    # detect objects
    # track objects
    results = model.track(frame, persist=True)

    # plot results
    frame_ = results[0].plot()
    
    # visualize
    cv2.imshow("frame", frame_)
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break
