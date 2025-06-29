from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
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
        title_Label = Label(background, text="TRAIN DATA WINDOW",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_Label.place(x=0, y=0, width=screen_width, height=50)


        #Train data Button
        train_button=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="white")
        train_button.place(x=650,y=500,width=250,height=50)
    


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
    

        #*****************Train Classifier and Save**************************
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset completed !")








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()