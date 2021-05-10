import cv2 
import numpy as np 
import os 
import pytesseract

frame = cv2.imread("images/sample11.png")

# converting to grayscale
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# binary 
filtered_frame = cv2.GaussianBlur(frame_gray, (5,5), 0)
ret,binarized_frame = cv2.threshold(filtered_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#inversion
inverted_frame = cv2.bitwise_not(binarized_frame)

cv2.imshow("processed", inverted_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(pytesseract.image_to_string(inverted_frame))