import cv2

Text = input("Enter (10 digits):  ")
Length = len(Text)
if Length < 10:
    print('\n')
else:
    print('This is more than 10')
    exit()
img = cv2.imread('Resources and Stock\Bill-Gates.jpg')
cv2.putText(img, Text, (550, 450), cv2.FONT_HERSHEY_COMPLEX, 1.3, (255, 0, 0))
cv2.imshow('Image', img)
cv2.waitKey()
