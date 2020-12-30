import cv2

capture = cv2.VideoCapture("Resources and Stock/Short_Video.mp4")
while True:
    success, img = capture.read()
    cv2.imshow("Video Viewer", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
