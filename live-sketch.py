import cv2
import numpy as np

def sketch(image):
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    image_gray_blur=cv2.GaussianBlur(image_gray,(7,7),0)

    canny_edge=cv2.Canny(image_gray_blur,50,70)

    rect,mask=cv2.threshold(canny_edge,170,255,cv2.THRESH_BINARY_INV)

    return mask

cap=cv2.VideoCapture(0)
while True:
    rect,frame=cap.read()
    cv2.imshow("live sketch app",sketch(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()    
cv2.waitKey(1)
cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)

