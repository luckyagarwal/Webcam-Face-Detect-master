                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import the libraries
import numpy as np
import os
import face_recognition
import csv
import cv2
import sys
import time
import logging as log
import datetime as dt
from time import sleep
def csv_to_dic(file_name):
    atten_dic={}
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            atten_dic[row[0]]=row[1]

    return atten_dic

def web_cam(): 
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log',level=log.INFO)
    
    video_capture = cv2.VideoCapture(0)
    #video_capture.set(3, 1366)
    #video_capture.set(4, 768)


   
    anterior = 0
    folder = 'datasets/temp'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                      #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass
    
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30)
        )
        
        # Draw a rectangle around the faces
        for f in faces:
            x, y, w, h = [ v for v in f ]
            padding = 50
            cv2.rectangle(frame,(x-padding,y-padding),(x+w+padding,y+h+padding),(255,0,0),2)
        #Save just the rectangle faces in SubRecFaces
            sub_face = frame[y:y+h+padding, x:x+w+padding]
            
            FaceFileName = "datasets/temp/temp" + str(y) + ".jpg"
            cv2.imwrite(FaceFileName, sub_face)
        #Display the image 
            #cv2.namedWindow("Result", cv2.WND_PROP_FULLSCREEN)
            #cv2.setWindowProperty("Result",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.putText(frame, "Align your face with the centre", (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
            cv2.imshow('Result',frame)
    
        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
    
    
        # Display the resulting frame
        #cv2.imshow('Video', frame)
    
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
    
    return
def face_(dir_,im):
# make a list of all the available images
    images = os.listdir(dir_)

# load your image
    image_to_be_matched = face_recognition.load_image_file(im)

# encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(
            image_to_be_matched)[0]

# iterate over each image
    for image in images:
    # load the image
        current_image = face_recognition.load_image_file("images/" + image)
    # encode the loaded image into a feature vector
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        if len( current_image_encoded ) > 0:
            biden_encoding = current_image_encoded[0]
        else:
            print("No faces found in the image!")
            quit()
    # match your image with the image and check if it matches
        result = face_recognition.compare_faces(
                [image_to_be_matched_encoded], current_image_encoded)
    # check if it was a match
        if result[0] == True:

            x=True
            break
        else:
            x=False

    if(x==True):
        return True,image
    else:
        return False,image


dir_="images"
dir_new="datasets/temp"
image_l = os.listdir(dir_)
data_image={}
attendance={}
count=15041080
for i in range(len(image_l)):
    data_image[image_l[i]]=count
    count=count+1
"""
count=15041080
for i in range(len(image_l)):
    attendance[count]='absent'
    count=count+1
"""
attendance=csv_to_dic("attendance.csv")
web_cam()
for photo in os.listdir(dir_new):
    Flag=False
    photo_path="./datasets/temp/" + photo
    boo,imag=face_(dir_,photo_path)
    if(boo==True):
        Flag=True
        for k,v in data_image.items():
            if k==imag:
                coer_id=v
                print(coer_id)
                break
        break


print(attendance)
print(Flag)
if Flag==True:
    for k1,v1 in attendance.items():
        print(k1)
        if(str(coer_id)==k1):
            attendance[k1]="present"
            print(k1)
else:
    print("not marked")

with open('attendance.csv','w') as output:
    writer=csv.writer(output)
    for k,v in attendance.items():
        writer.writerow([k,v])
