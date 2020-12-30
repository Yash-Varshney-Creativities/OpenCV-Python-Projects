import cv2

img = cv2.imread('Resources and Stock\Bill-Gates.jpg')
GrayScale_Img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image Maker", GrayScale_Img)
cv2.waitKey(0)