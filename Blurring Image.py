import cv2
img = cv2.imread('Resources and Stock/Bill-Gates.jpg')
Blur_Img = cv2.GaussianBlur(img, (11, 11), 0)  # (7, 7),0 These are the Parameter which will make it blur by 7, [Number always to be in Odd]
cv2.imshow("Blur Image Maker", Blur_Img)
cv2.waitKey(0)