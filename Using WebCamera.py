import cv2

Camera = cv2.VideoCapture(0)
Camera.set(3, 640)
Camera.set(4, 480)
while True:
    success, img = Camera.read()
    cv2.imshow("Video Viewer", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break