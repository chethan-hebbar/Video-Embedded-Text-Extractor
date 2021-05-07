import cv2 
import numpy as np 
import os 
import pytesseract

video = cv2.VideoCapture("videos/sample.mp4")

video_available = 1
frame_count = 0

while video_available:

    video_available, frame = video.read()
    # converting to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # binary 
    binary_frame = cv2.threshold(frame_gray ,130,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #inversion
    inverted_frame = cv2.bitwise_not(binary_frame)

    if frame_count == 0:
        previous_text = ""
    
    else:
        previous_text = extracted_text

    extracted_text = pytesseract.image_to_string(frame_gray)

    if(extracted_text == "" or extracted_text == previous_text):
        frame_count += 1
        continue

    else:
        extracted_set = set(extracted_text.split())
        previous_set = set(previous_text.split())

        if(len(extracted_set.difference(previous_set)) > 4):
            print("Frame number: {}".format(frame_count))
            frame_count += 1
            print(extracted_text)
