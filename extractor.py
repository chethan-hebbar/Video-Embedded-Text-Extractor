import cv2 
import pytesseract

img = cv2.imread("images/example3.png")

cv2.imshow("anti life", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("anti life", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img_rgb)
print(text)