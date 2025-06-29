from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        root.title("Face Recognition System")

    
        #HEADER IMAGE WITH COLLEGE LOGO AND NAME
        img1 = Image.open(r"Images\BTKIT_Name.png")
        img1 = img1.resize((screen_width, 150), Image.LANCZOS)
        self.photo_img1 = ImageTk.PhotoImage(img1)

        header = Label(self.root, image=self.photo_img1, bg="white")
        header.place(x=0, y=0, width=screen_width, height=150)

        
        #BACKGROUND
        img2 = Image.open(r"Images\BTKIT_Background.jpg")
        img2 = img2.resize((screen_width, screen_height), Image.LANCZOS)
        self.photo_img2 = ImageTk.PhotoImage(img2)

        background = Label(self.root, image=self.photo_img2)
        background.place(x=0, y=150, width=screen_width, height=screen_height-150)

        #TITLE
        title_Label = Label(background, text="FACE RECOGNITION WINDOW",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_Label.place(x=0, y=0, width=screen_width, height=50)



        #Train data Button
        face_recognition_button=Button(self.root,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="white")
        face_recognition_button.place(x=570,y=500,width=400,height=50)



    #************************Mark Attendance Function******************************
    def mark_attendance(self,no,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((no not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{no}, {r}, {n}, {d}, {dtString}, {d1}, Present")





    #************************Face Detection Function******************************
    def face_recog(self):

        #Function to Draw Boundries
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence= int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="fullmoon", database="face_recognizer")
                cursor = conn.cursor()

                cursor.execute("select student_no from student where student_no="+str(id))
                no=cursor.fetchone()
                no="+".join(no) if no else "Unknown"

                cursor.execute("select name from student where student_no="+str(id))
                n=cursor.fetchone()
                n="+".join(n) if n else "Unknown"

                cursor.execute("select roll from student where student_no="+str(id))
                r=cursor.fetchone()
                r="+".join(r) if r else "Unknown"


                cursor.execute("select deprt from student where student_no="+str(id))
                d=cursor.fetchone()
                d="+".join(d) if d else "Unknown"


                conn.close()


                if confidence>77:
                    cv2.putText(img,f"Student No. : {no}",(x,y-85),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Roll No. : {r}",(x,y-60),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name : {n}",(x,y-35),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department : {d}",(x,y-10),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,255,0),2)

                    self.mark_attendance(no,r,n,d)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        

        #Function to Recognize Face
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while(True):
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13 or cv2.waitKey(1)==27:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()