# importing libraries
import cv2 
import numpy as np 
import os 
import pytesseract

# using opencv to start playing the video frame-by-frame
video = cv2.VideoCapture("videos/sample.mp4")

# control variables
video_available = 1
frame_count = 0

while video_available:

    # reading the frame
    video_available, frame = video.read()

    # converting to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # otsu's binarization
    filtered_frame = cv2.GaussianBlur(frame_gray, (5,5), 0)
    binarized_image = cv2.threshold(filtered_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #inversion of the image (as binarized contains 0 and 1, this will flip them)
    inverted_frame = cv2.bitwise_not(filtered_frame)

    # assigning value to previous_text
    if frame_count == 0:
        previous_text = ""
    
    else:
        previous_text = extracted_text

    # extracting text from the frame
    extracted_text = pytesseract.image_to_string(inverted_frame)

    # simple way to detect empty text or repeated text over a continous set of frames
    if(extracted_text == "" or extracted_text == previous_text):
        frame_count += 1
        continue

    else:
        extracted_set = set(extracted_text.split())
        previous_set = set(previous_text.split())

        if(len(extracted_set.difference(previous_set)) > 4):

            # printing out the text onto the cmd line
            print("Frame number: {}".format(frame_count))
            frame_count += 1
            print(extracted_text)
