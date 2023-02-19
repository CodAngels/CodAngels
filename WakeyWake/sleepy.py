#Line 2-5 imports libraries
import numpy as np
from imutils import face_utils
import dlib
import cv2
from pygame import mixer
#Setting a threshold
thres = 6
#Creating an alarm sound using pygame
mixer.init()
sound = mixer.Sound('alarm.mp3')

distList = []

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#Reading images from the webcam
cap = cv2.VideoCapture(0)

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return np.abs(x1-x2)**2 + np.abs(y1-y2)**0.5
#Reading images from the webcam
while True:
    _, image = cap.read()
    #Converting to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Detecting faces
    rects = detector(gray, 0)
    #Start traversing the faces
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        #Get the 68 face landmarks and convert them to a NumPy array
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
        #Draw al the landmarks
        le_38 = shape[37]
        le_39 = shape[38]
        le_41 = shape[40]
        le_42 = shape[41]

        re_44 = shape[43]
        re_45 = shape[44]
        re_47 = shape[46]
        re_48 = shape[47]
        
        distList.append((dist(le_38, le_42)+ dist(le_39, le_41)+dist(re_44, re_48)+dist(re_45, re_47))//4<thres)
        if len(distList) > 10:distList.pop(0)

        if sum(distList) >= 4:
            try:
                sound.play()
            except:
                print("Couldn't play sound")
        else:
            try:
                sound.stop()
            except:
                print("Oh Noo")

    cv2.imshow("Output", image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()