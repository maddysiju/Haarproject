import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import numpy as np


app = FastAPI()

@app.post("/process_image")
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    return len(roi_gray)