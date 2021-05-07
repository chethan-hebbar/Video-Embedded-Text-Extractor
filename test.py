import cv2 
import numpy as np 
import os 
import pytesseract

frame = cv2.imread("images/sample.png")

# converting to grayscale
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# binary 
binary_frame = cv2.threshold(frame_gray ,130,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#inversion
inverted_frame = cv2.bitwise_not(binary_frame)
"""
# noise reduction
kernel = np.ones((2,2),np.uint8)
processed_frame = cv2.erode(inverted_frame, kernel, iterations = 1)
processed_frame = cv2.dilate(processed_frame, kernel, iterations = 1)"""
    
cv2.imshow("processed", inverted_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()