from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        root.title("Face Recognition System")


        #***********************Variables**************************
        self.var_course=StringVar()
        self.var_deprt=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_group=StringVar()
        self.var_name=StringVar()
        self.var_no=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.var_address=StringVar()




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
        title_Label = Label(background, text="STUDENT MANAGEMENT WINDOW",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_Label.place(x=0, y=0, width=screen_width, height=50)


        #Main Frame
        main_frame=Frame(background,bd=2,bg="white")
        main_frame.place(x=5,y=60,width=screen_width-20,height=screen_height-295)


        #Left Frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
        left_frame.place(x=5,y=0,width=720,height=screen_height-310)

        #Current Course Frame
        current_cousre_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
        current_cousre_frame.place(x=7,y=0,width=700,height=screen_height-745)


        #Course
        course_lable=Label(current_cousre_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_lable.grid(row=0,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_cousre_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","B.Tech","M.Tech","BCA","MCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Department
        depart_lable=Label(current_cousre_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        depart_lable.grid(row=0,column=2,padx=10,sticky=W)

        depart_combo=ttk.Combobox(current_cousre_frame,textvariable=self.var_deprt,font=("times new roman",10,"bold"),width=20,state="readonly")
        depart_combo["values"]=("Select Department","CSE","ECE","EE","ME","CE","CHE","BioTech")
        depart_combo.current(0)
        depart_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_lable=Label(current_cousre_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_cousre_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2022","2023","2024","2025","2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        sem_lable=Label(current_cousre_frame,text="Sem",font=("times new roman",13,"bold"),bg="white")
        sem_lable.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_cousre_frame,textvariable=self.var_sem,font=("times new roman",10,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","Sem I","Sem II")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Class Student Frame
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold"))
        class_student_frame.place(x=7,y=130,width=700,height=370)


        #Student No
        student_no_lable=Label(class_student_frame,text="Student No.",font=("times new roman",13,"bold"),bg="white")
        student_no_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_no,width=19,font=("times new roman",13,"bold"))
        student_no_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student roll number
        student_roll_lable=Label(class_student_frame,text="Student Roll No.",font=("times new roman",13,"bold"),bg="white")
        student_roll_lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #Student Name
        student_name_lable=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        student_name_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=19,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Student Group
        student_group_lable=Label(class_student_frame,text="Student Group",font=("times new roman",13,"bold"),bg="white")
        student_group_lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)


        student_group_combo=ttk.Combobox(class_student_frame,textvariable=self.var_group,font=("times new roman",13),width=18,state="readonly")
        student_group_combo["values"]=("Group","I","II")
        student_group_combo.current(0)
        student_group_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Student Gender
        student_gender_lable=Label(class_student_frame,text="Student Gender",font=("times new roman",13,"bold"),bg="white")
        student_gender_lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        student_gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13),width=17,state="readonly")
        student_gender_combo["values"]=("Gender","Male","Female","Other")
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #Student Date Of Birst
        student_DOB_lable=Label(class_student_frame,text="Student DOB",font=("times new roman",13,"bold"),bg="white")
        student_DOB_lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        student_DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        student_DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)



        #Student Mobile Number
        student_mobile_lable=Label(class_student_frame,text="Student Mobile",font=("times new roman",13,"bold"),bg="white")
        student_mobile_lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        student_mobile_entry=ttk.Entry(class_student_frame,textvariable=self.var_mobile,width=19,font=("times new roman",13,"bold"))
        student_mobile_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #Student Email
        student_email_lable=Label(class_student_frame,text="Student Email",font=("times new roman",13,"bold"),bg="white")
        student_email_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        student_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        student_email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        
        #Student Address
        student_address_lable=Label(class_student_frame,text="Student Address",font=("times new roman",13,"bold"),bg="white")
        student_address_lable.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        student_address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=19,font=("times new roman",13,"bold"))
        student_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)



        #Raido Buttons
        self.var_radio=StringVar()

        radio_button1=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="Take Photo Smaple",value="Yes")
        radio_button1.grid(row=6,column=0)

        radio_button2=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="No Photo Smaple",value="No")
        radio_button2.grid(row=6,column=1)

        #Button1 Frame
        button1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button1_frame.place(x=7,y=235,width=683,height=35)

        save_button=Button(button1_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)


        update_button=Button(button1_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)


        delete_button=Button(button1_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)


        reset_button=Button(button1_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)


        #Button2 Frame
        button2_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button2_frame.place(x=7,y=270,width=683,height=35)

        take_photo_button=Button(button2_frame,text="Take Photo",command=self.generate_dataset,width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0)

        update_photo_button=Button(button2_frame,text="Update Photo",width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_button.grid(row=0,column=1)


        #Right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
        right_frame.place(x=750,y=0,width=755,height=screen_height-310)

        #************************SEARCH SYSTEM***************************
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search Student",font=("times new roman",15,"bold"))
        search_frame.place(x=7,y=0,width=735,height=80)

        #Search Bar
        search_lable=Label(search_frame,text="Search Bar",width=8,font=("times new roman",15,"bold"),bg="red",fg="white")
        search_lable.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",14),width=12,state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=4,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",14,"bold"))
        search_entry.grid(row=0,column=2,padx=4,pady=5,sticky=W)

        search_button=Button(search_frame,text="Search",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=7)

        show_all_button=Button(search_frame,text="Show All",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        show_all_button.grid(row=0,column=4)

        #**************************TABLE FRAME*************************
        #Table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=85,width=735,height=400)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Student_No","Roll","Name","Deprt","Course","Year","Sem","Group","DOB","Gender","Email","Mobile","Address","Photo"),xscroll=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Deprt",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Student_No",text="Student No.")
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Group",text="Group")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mobile",text="Mobile")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Course",width=100)
        self.student_table.column("Deprt",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Student_No",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Group",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mobile",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #***************Add Data Function*****************
    def add_data(self):
        if self.var_course.get()=="Select Course" or self.var_deprt.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_no.get()=="" or self.var_name.get()=="" or self.var_group.get()=="Group" or self.var_roll.get()=="" or self.var_gender.get()=="Gender" or self.var_dob.get()=="" or self.var_mobile.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error !","All Fields are required",parent=self.root)
            return
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="fullmoon",
                database="face_recognizer"
            )
            cursor = conn.cursor()

            sql = """INSERT INTO student 
                    (student_no, roll,  name, course, deprt, year, semester,student_group, dob, gender, mobile, email, address, photosample)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            values = (
                self.var_no.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_course.get(),
                self.var_deprt.get(),
                self.var_year.get(),
                self.var_sem.get(), 
                self.var_group.get(), 
                self.var_dob.get(),
                self.var_gender.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_radio.get()
                )

            cursor.execute(sql, values)
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Student details have been added!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Database Error", f"Error due to {str(e)}", parent=self.root)





    #***************Fetch Data Function*****************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="fullmoon",database="face_recognizer")
        cursor = conn.cursor()
        cursor.execute("select * from student")
        data=cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




    #**************************Get cursor*************************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_no.set(data[0])
        self.var_roll.set(data[1])
        self.var_name.set(data[2])
        self.var_course.set(data[3])
        self.var_deprt.set(data[4])
        self.var_year.set(data[5])
        self.var_sem.set(data[6])
        self.var_group.set(data[7])
        self.var_dob.set(data[8])
        self.var_gender.set(data[9])
        self.var_mobile.set(data[10])
        self.var_email.set(data[11])
        self.var_address.set(data[12])
        self.var_radio.set(data[13])



    #***********************Update Data Function************************************
    def update_data(self):
        if self.var_course.get()=="Select Course" or self.var_deprt.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_no.get()=="" or self.var_name.get()=="" or self.var_group.get()=="Group" or self.var_roll.get()=="" or self.var_gender.get()=="Gender" or self.var_dob.get()=="" or self.var_mobile.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error !","All Fields are required",parent=self.root)
            return
        
        try:
            update_data=messagebox.askyesno("Update","Do you want to Update this student details",parent=self.root)
            if update_data>0:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="fullmoon",
                    database="face_recognizer"
                )
                cursor = conn.cursor()
                cursor.execute("Update student set roll=%s, name=%s, course=%s, deprt=%s, year=%s, semester=%s, student_group=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s, photosample=%s where student_no=%s ",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_deprt.get(),
                    self.var_year.get(),
                    self.var_sem.get(), 
                    self.var_group.get(), 
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_radio.get(),
                    self.var_no.get()
                ))
            else:
                if not update_data:
                    return
            messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)




    #****************************Delete Data Function*****************************
    def delete_data(self):
        if self.var_no.get()=="":
            messagebox.showerror("Error","Student must be required",parent=self.root)
        else:
            try:
                delete_data=messagebox.askyesno("Delete Student Page","Do you want to delete this Student",parent=self.root)
                if delete_data>0:
                    conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="fullmoon",
                    database="face_recognizer"
                    )
                    cursor = conn.cursor()
                    sql="delete from student where student_no=%s"
                    val=(self.var_no.get(),)
                    cursor.execute(sql,val)
                else:
                    if not delete_data:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",partent=self.root)


    #************************Reset data function************************
    def reset_data(self):
        self.var_no.set("")
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_course.set("Select Course"),
        self.var_deprt.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"), 
        self.var_group.set("Group"), 
        self.var_dob.set(""),
        self.var_gender.set("Gender"),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_radio.set("")



    #***************************Generate Data Set Sample***************************
    def generate_dataset(self):
        if self.var_course.get()=="Select Course" or self.var_deprt.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_no.get()=="" or self.var_name.get()=="" or self.var_group.get()=="Group" or self.var_roll.get()=="" or self.var_gender.get()=="Gender" or self.var_dob.get()=="" or self.var_mobile.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error !","All Fields are required",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="fullmoon",
                    database="face_recognizer"
                )
                cursor = conn.cursor()
                cursor.execute("Select *from student")
                myresult=cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                cursor.execute("Update student set roll=%s, name=%s, course=%s, deprt=%s, year=%s, semester=%s, student_group=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s, photosample=%s where student_no=%s ",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_deprt.get(),
                    self.var_year.get(),
                    self.var_sem.get(), 
                    self.var_group.get(), 
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_radio.get(),
                    self.var_no.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #**********************Load predefine data on face frontals from OpenCV********************
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets compeleted !")

            
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

            



        



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()