# Embedded-text extractor from videos
* Video Link:: https://www.youtube.com/watch?v=9ezzpuOqkX4
* images:: contains the test images
* videos:: contains videos to be used
* outputs:: contains output file "result.txt" containing extractor outputs and cmd line outputs for test.py
* papers:: contains reference papers and report .odt file
* **extractor.py :: contains the code for the video extractor**
* test.py :: contains the code to test the preprocessing on images, to give best results using tesseract-ocr
* **report.pdf:: contains answers to follow-up mail**

# Analysis of the results from "results.txt"
* **The first five instances of embedded text has been identified with great accuracy(with no need for wrong results on mutliple frames)** 
* **After frame 245, the LSTM network seems to be taking many attempts to get the text right. The program tries to reduce redundancy(as many frames have the same text embedded) but after frame 245 the model gives out bad preditions about the text and hence takes more frames to get the correct prediction.**
* As seen from the output, the model gives out the correct text in for almost all the embedded-text(albiet it has many "misses" as the program goes on).
