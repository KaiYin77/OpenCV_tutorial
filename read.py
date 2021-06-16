import cv2 as cv

'''
# Reading Image
img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)
#cv.waitkey(0)
'''

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Videos
# capture = cv.VideoCapture(0) # Reference the webcam
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, .5)

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
