import cv2
img = cv2.imread('Resources and Stock\Bill-Gates.jpg')
Canny_Img = cv2.Canny(img, 150, 75)
cv2.imshow("Canny Image Maker", Canny_Img)
cv2.waitKey(0)