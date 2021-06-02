from enum import Enum
import cv2 as cv
from PIL import Image

cascade = cv.CascadeClassifier('./statics/haarcascade_frontalface_default.xml')

class Memes(Enum):
    PEPE = "./statics/memes/pepe_normal.png"
    TROLL = "./statics/memes/trollface.png"
    SCREAM = "./statics/memes/scream.png"
    KEEF = "./statics/memes/keef.png"
    OBAMA = "./statics/memes/obama.png"

def get_faces(path):
    img = cv.imread(path)
    return cascade.detectMultiScale(cv.cvtColor(img, cv.COLOR_BGR2GRAY), 1.5, 3)

def meme(path, meme):
    faces = get_faces(path)
    face_img, meme_img = Image.open(path), Image.open(meme.value)
    for (x, y, w, h) in faces:
        meme_img = meme_img.resize((w, h))
        face_img.paste(meme_img, (x, y), meme_img)
    face_img.save(path)