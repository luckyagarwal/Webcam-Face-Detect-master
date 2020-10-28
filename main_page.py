# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
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
#import software
#from software import Ui_MainWindow_x
from atten import Ui_Dialog
def csv_to_dic(file_name):
    atten_dic={}
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            atten_dic[row[0]]=[r for r in row[1:len(row)]]

    return atten_dic
def csv_to_dic_new(file_name):
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
            padding = 30
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
        #cv2.imshow('Video', frame)with open(file_name, 'r') as csvFile:
      

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wel = QtWidgets.QLabel(self.centralwidget)
        self.wel.setGeometry(QtCore.QRect(260, 190, 251, 61))
        self.wel.setObjectName("wel")
        self.intro = QtWidgets.QLabel(self.centralwidget)
        self.intro.setGeometry(QtCore.QRect(290, 240, 491, 181))
        self.intro.setObjectName("intro")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 120, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Mark_a = QtWidgets.QPushButton(self.centralwidget)
        self.Mark_a.setGeometry(QtCore.QRect(630, 500, 131, 34))
        self.Mark_a.setObjectName("Mark_a")
        self.username = QtWidgets.QTextEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(30, 250, 181, 31))
        self.username.setObjectName("username")
        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.setGeometry(QtCore.QRect(30, 220, 121, 21))
        self.User.setObjectName("User")
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 320, 181, 31))
        self.password.setObjectName("password")
        self.faculty = QtWidgets.QLabel(self.centralwidget)
        self.faculty.setGeometry(QtCore.QRect(30, 160, 191, 41))
        self.faculty.setObjectName("faculty")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(70, 370, 88, 34))
        self.login.setObjectName("login")
        self.User_2 = QtWidgets.QLabel(self.centralwidget)
        self.User_2.setGeometry(QtCore.QRect(30, 290, 91, 21))
        self.User_2.setObjectName("User_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 500, 141, 34))
        self.pushButton.setObjectName("pushButton")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 450, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Mark_a.clicked.connect(self.prnt)
    def open_dialog(self):
       Dialog = QtWidgets.QDialog()
       ui = Ui_Dialog()
       ui.setupUi(Dialog)
       Dialog.show()
       Dialog.exec_() 
       
    def prnt(self):
        MainWindow.hide()
        dir_="images"
        dir_new="datasets/temp"
        image_l = os.listdir(dir_)
        data_image={}
        attendance={}
       
        data_image=csv_to_dic_new("image-rollno.csv")
        attendance=csv_to_dic_new("attendance.csv")
        web_cam()
        for photo in os.listdir(dir_new):
            Flag=False
            photo_path="./datasets/temp/" + photo
            try:
                boo,imag=face_(dir_,photo_path)
            except:
                continue
            
            if(boo==True):
                Flag=True
                for k,v in data_image.items():
                    if k==imag:
                        coer_id=v
                        
                       
               


      
            if Flag==True:
                for k1,v1 in attendance.items():
                   
                    if(str(coer_id)==k1):
                        attendance[k1]="present"
                        
            else:
                print("not marked")

        with open('attendance.csv','w') as output:
            writer=csv.writer(output)
            for k,v in attendance.items():
                writer.writerow([k,v])

        
        self.open_dialog()
        sys.exit()    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#00ff00;\">WELCOME TO STA</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.intro.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#55aaff;\">A face recognition based application. The system is designed</span></p><p><span style=\" font-weight:600; color:#55aaff;\">for marking attendance of student by recognizing their face.</span></p><p><span style=\" font-weight:600; color:#55aaff;\">Also can be used for statistical purposes.</span></p><p><br/></p></body></html>"))
        self.Mark_a.setText(_translate("MainWindow", "Mark Attendance"))
        self.User.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Username</span></p></body></html>"))
        self.faculty.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Faculty login</span></p></body></html>"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.User_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Check Attendance"))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
