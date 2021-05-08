# OffNoteLabs_Task1_Vision
# Embedded-text extractor from videos
* Video Link: https://www.youtube.com/watch?v=9ezzpuOqkX4
* extractor.py :: contains the code for the video extractor
* test.py :: contains the code to test the preprocessing on images, to give best results using tesseract-ocr
* results.txt :: contains the output of the extractor with frame number for every embedded-text detection

# Analysis of the results from "results.txt"
* The first five instances of embedded text has been identified with great accuracy(with no need for wrong results on mutliple frames) 
* After frame 245, the LSTM network seems to be taking many attempts to get the text right. The program tries to reduce redundancy(as many frames have the same text embedded) but after frame 245 the model gives out bad preditions about the text and hence takes more frames to get the correct prediction.
* As seen from the output, the model gives out the correct text in for almost all the embedded-text(albiet it has many "misses" as the program goes on).