import cv2
import numpy


img = cv2.imread('Resources and Stock/Cards.jpeg')
width = 236
height = 351
Point1 = numpy.float32([[587, 49], [787, 166], [412, 347], [611, 462]])
Point2 = numpy.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(Point1, Point2)
OutPut_Image = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Edited Image', OutPut_Image)
cv2.imshow('Original Image', img)
cv2.waitKey()
