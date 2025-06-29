from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
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
        title_Label = Label(background, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_Label.place(x=0, y=0, width=screen_width, height=50)


        #***************Display Time************************************
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_Label,font=("times new roman",14,"bold"),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()



        #BUTTON 1 - Students Details
        img3 = Image.open(r"Images\Student_Button.png")
        img3 = img3.resize((210,210), Image.LANCZOS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        button_1=Button(background,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_1.place(x=200,y=300,width=210,height=40)

        button_img1=Button(background,image=self.photo_img3,command=self.student_details,cursor="hand2")
        button_img1.place(x=200,y=90,width=210,height=210)

        #BUTTON 2 - Face Detector
        img4 = Image.open(r"Images\Face_Detector.jpg")
        img4 = img4.resize((210,210), Image.LANCZOS)
        self.photo_img4 = ImageTk.PhotoImage(img4)

        button_2=Button(background,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_2.place(x=500,y=300,width=210,height=40)

        button_img2=Button(background,image=self.photo_img4,cursor="hand2",command=self.face_data)
        button_img2.place(x=500,y=90,width=210,height=210)


        #BUTTON 3 - Mark Attendance
        img5 = Image.open(r"Images\Attendance_Logo.png")
        img5 = img5.resize((210,210), Image.LANCZOS)
        self.photo_img5 = ImageTk.PhotoImage(img5)

        button_3=Button(background,text="Mark Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_3.place(x=800,y=300,width=210,height=40)

        button_img3=Button(background,image=self.photo_img5,cursor="hand2",command=self.attendance_data)
        button_img3.place(x=800,y=90,width=210,height=210)


        #BUTTON 4 - Help Desk
        img6 = Image.open(r"Images\Help_Desk_Logo.jpg")
        img6 = img6.resize((210,210), Image.LANCZOS)
        self.photo_img6 = ImageTk.PhotoImage(img6)

        button_4=Button(background,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_4.place(x=1100,y=300,width=210,height=40)

        button_img4=Button(background,image=self.photo_img6,command=self.help_desk,cursor="hand2")
        button_img4.place(x=1100,y=90,width=210,height=210)

        
        #BUTTON 5 - Train Data
        img7 = Image.open(r"Images\Train_Data_Logo.jpg")
        img7 = img7.resize((210,210), Image.LANCZOS)
        self.photo_img7 = ImageTk.PhotoImage(img7)

        button_5=Button(background,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_5.place(x=200,y=570,width=210,height=40)

        button_img5=Button(background,image=self.photo_img7,cursor="hand2",command=self.train_data)
        button_img5.place(x=200,y=360,width=210,height=210)

        #BUTTON 6 - Photos
        img8 = Image.open(r"Images\Photos_Logo.png")
        img8 = img8.resize((210,210), Image.LANCZOS)
        self.photo_img8 = ImageTk.PhotoImage(img8)

        button_6=Button(background,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_6.place(x=500,y=570,width=210,height=40)

        button_img6=Button(background,image=self.photo_img8,cursor="hand2",command=self.open_img)
        button_img6.place(x=500,y=360,width=210,height=210)


        #BUTTON 7 - Developer
        img9 = Image.open(r"Images\Developer_Logo.png")
        img9 = img9.resize((210,210), Image.LANCZOS)
        self.photo_img9 = ImageTk.PhotoImage(img9)

        button_7=Button(background,text="Developer",cursor="hand2",command=self.developer_info,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_7.place(x=800,y=570,width=210,height=40)

        button_img7=Button(background,image=self.photo_img9,command=self.developer_info,cursor="hand2")
        button_img7.place(x=800,y=360,width=210,height=210)


        #BUTTON 8 - Exit
        img10 = Image.open(r"Images\Exit_Logo.png")
        img10 = img10.resize((210,210), Image.LANCZOS)
        self.photo_img10 = ImageTk.PhotoImage(img10)

        button_8=Button(background,text="Exit",command=self.exit,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        button_8.place(x=1100,y=570,width=210,height=40)

        button_img8=Button(background,image=self.photo_img10,command=self.exit,cursor="hand2")
        button_img8.place(x=1100,y=360,width=210,height=210)


    #*********************Function Buttons************************

    #Button 1 Student Detail
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    #Button 2 Face Detactor
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    #Button 3 Attendance
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    #Button 4 Help Desk
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    #Button 5 Train Data
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    #Button 6 Photos
    def open_img(self):
        os.startfile("data")

    #Button 7 Train Data
    def developer_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    #Button 8 Exit
    def exit(self):
        confirm_exit = messagebox.askyesno("FACE RECOGNITION ATTENDANCE SYSTEM", "Are you sure?",parent=self.root)
        if confirm_exit:
            self.root.destroy()
        else:
            return

     
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
