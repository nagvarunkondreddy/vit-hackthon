import cv2
import firebase_admin
from firebase_admin import credentials
from firebase import firebase
from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\kusha\Desktop\New folder (2)\facedetection-master\facedetection-master\ionic-15062-firebase-adminsdk-63km2-05f7bac8ed.json"
firebase = firebase.FirebaseApplication('https://ionic-15062.firebaseio.com/')
client = storage.Client()
bucket = client.get_bucket('ionic-15062.appspot.com')
# posting to firebase storage
imageBlob = bucket.blob("/")

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
import requests
import json
flag = 0
while True:
    # Read the frame
    _, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.4, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imwrite(filename='saved_img.jpeg', img=frame)
        #cap.release()
        print("Processing image...")
        #img_ = cv2.imread('saved_img.jpeg', cv2.IMREAD_ANYCOLOR)
        print("Converting RGB image to grayscale...")
        print("Image saved!")
        flag = 1
        if(flag == 1):
            header = {"Content-Type": "application/json; charset=utf-8",
                      "Authorization": "Basic MTk0NDgyM2QtYTYwOS00ODBiLTk2MGYtZmE0YTc0ZTNjM2Mz"}

            payload = {"app_id": "fa6e0cb5-c6d4-48cb-8bb5-8ec98e528a7f",
                       "included_segments": ["All"],
                       "contents": {"en": "Person Detected"}}
             
            req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
            print(req.status_code, req.reason)

        cap.release()
        break
    if(flag == 1):
        break


    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
    # Display
    cv2.imshow('img', frame)

