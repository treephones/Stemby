import cv2 as cv
from PIL import Image

cascade = cv.CascadeClassifier('./statics/haarcascade_frontalface_default.xml')

PEPE = "./statics/memes/pepe_normal.png"

def get_faces(path):
    img = cv.imread(path)
    return cascade.detectMultiScale(cv.cvtColor(img, cv.COLOR_BGR2GRAY), 1.03, 3)

def pepe(path):
    faces = get_faces(path)
    face_img, meme_img = Image.open(path), Image.open(PEPE)
    for (x, y, w, h) in faces:
        meme_img.resize((w, h))
        face_img.paste(meme_img, (x, y), meme_img)
    face_img.save(path)