import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston', img)

# Translation

# [ a b c, [ u,    [ x,
#   d e f,   v,  =   y,
#   g h i ]  w ]     z ]
# abde = linear transformation
# cf = translation
# gh = perpective transformation

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    # (image, transformation, size)
    return cv.warpAffine(img, transMat, dimensions)

# -x -->left
# -y -->up

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=Node):



cv.waitKey(0)
