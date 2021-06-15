import cv2 as cv

# Reading Image
# img = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitkey(0)

# Reading Videos
# capture = cv.VideoCapture(0) # Reference the webcam
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
