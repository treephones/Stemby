import cv2 as cv

cascade = cv.CascadeClassifier('./statics/haarcascade_frontalface_default.xml')

def get_faces(path):
    img = cv.imread(path)
    return cascade.detectMultiScale(cv.cvtColor(img, cv.COLOR_BGR2GRAY), 1.03, 3)

def pepe(path):
    print("ok")