from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Attendance:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        root.title("Face Recognition System")



        #************************Variables***************************
        self.var_attendance_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_deprt=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()


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
        title_Label = Label(background, text="ATTENDANCE WINDOW",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_Label.place(x=0, y=0, width=screen_width, height=50)

        
        #Main Frame
        main_frame=Frame(background,bd=2,bg="white")
        main_frame.place(x=5,y=57,width=screen_width-20,height=screen_height-293)

        #Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 20, "bold"))
        left_frame.place(x=5, y=0, width=720, height=screen_height-310)

        img3 = Image.open(r"Images\Attendance_image.png")
        img3 = img3.resize((700, 180), Image.LANCZOS)
        self.photo_img3 = ImageTk.PhotoImage(img3)
        
        # Place the image at the top of the left_frame
        image_label = Label(left_frame, image=self.photo_img3, bg="white")
        image_label.place(x=7, y=0, width=700, height=180)

        # Inside Left Frame (adjusted to start BELOW the image)
        inside_left_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 15, "bold"))
        inside_left_frame.place(x=7, y=190, width=700, height=320)


        #Attendance ID
        student_no_lable=Label(inside_left_frame,text="Attendance ID",font=("times new roman",13,"bold"),bg="white")
        student_no_lable.grid(row=0,column=0,padx=130,pady=5,sticky=W)

        student_no_entry=ttk.Entry(inside_left_frame,width=19,textvariable=self.var_attendance_id,font=("times new roman",13,"bold"))
        student_no_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)


        #Student Roll number
        student_roll_lable=Label(inside_left_frame,text="Student Roll No.",font=("times new roman",13,"bold"),bg="white")
        student_roll_lable.grid(row=1,column=0,padx=130,pady=5,sticky=W)

        student_roll_entry=ttk.Entry(inside_left_frame,width=19,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        student_roll_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)


        #Student Name
        student_name_lable=Label(inside_left_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        student_name_lable.grid(row=2,column=0,padx=130,pady=5,sticky=W)

        student_name_entry=ttk.Entry(inside_left_frame,width=19,textvariable=self.var_name,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=2,column=1,padx=0,pady=5,sticky=W)


        #Student Department
        student_department_lable=Label(inside_left_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        student_department_lable.grid(row=3,column=0,padx=130,pady=5,sticky=W)


        student_department_entry=ttk.Entry(inside_left_frame,width=19,textvariable=self.var_deprt,font=("times new roman",13,"bold"))
        student_department_entry.grid(row=3,column=1,padx=0,pady=5,sticky=W)


        #Time
        time_lable=Label(inside_left_frame,text="Time",font=("times new roman",13,"bold"),bg="white")
        time_lable.grid(row=4,column=0,padx=130,pady=5,sticky=W)


        time_entry=ttk.Entry(inside_left_frame,width=19,textvariable=self.var_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=4,column=1,padx=0,pady=5,sticky=W)


        #Date
        date_lable=Label(inside_left_frame,text="Date",font=("times new roman",13,"bold"),bg="white")
        date_lable.grid(row=5,column=0,padx=130,pady=5,sticky=W)

        date_entry=ttk.Entry(inside_left_frame,width=19,textvariable=self.var_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=5,column=1,padx=0,pady=5,sticky=W)


        #Attendance Status
        attendance_status_lable=Label(inside_left_frame,text="Status",font=("times new roman",13,"bold"),bg="white")
        attendance_status_lable.grid(row=6,column=0,padx=130,pady=5,sticky=W)


        attendance_status_combo=ttk.Combobox(inside_left_frame,font=("times new roman",13),width=17,textvariable=self.var_status,state="readonly")
        attendance_status_combo["values"]=("Status","Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=6,column=1,padx=0,pady=5,sticky=W)



        #Button Frame
        button_frame=Frame(inside_left_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=7,y=270,width=683,height=35)


        import_button=Button(button_frame,text="Import CSV",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_button.grid(row=0,column=0)


        export_button=Button(button_frame,text="Export CSV",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_button.grid(row=0,column=1)


        update_button=Button(button_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=2)


        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)




        #Right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",20,"bold"))
        right_frame.place(x=750,y=0,width=755,height=screen_height-310)

        #**************************TABLE FRAME*************************
        #Table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=0,width=738,height=510)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_attendance_table=ttk.Treeview(table_frame,column=("ID","Roll","Name","Deprt","Time","Date","Attendance"),xscroll=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_attendance_table.xview)
        scroll_y.config(command=self.student_attendance_table.yview)
        self.student_attendance_table.heading("ID",text="Attendance ID")
        self.student_attendance_table.heading("Roll",text="Roll No.")
        self.student_attendance_table.heading("Name",text="Name")      
        self.student_attendance_table.heading("Deprt",text="Department")
        self.student_attendance_table.heading("Time",text="Time")
        self.student_attendance_table.heading("Date",text="Date")
        self.student_attendance_table.heading("Attendance",text="Attendance")
        self.student_attendance_table["show"]="headings"


        self.student_attendance_table.column("ID",width=100)
        self.student_attendance_table.column("Roll",width=100)
        self.student_attendance_table.column("Name",width=100)
        self.student_attendance_table.column("Deprt",width=100)
        self.student_attendance_table.column("Time",width=100)
        self.student_attendance_table.column("Date",width=100)
        self.student_attendance_table.column("Attendance",width=100)

        self.student_attendance_table.pack(fill=BOTH,expand=1)

        self.student_attendance_table.bind("<ButtonRelease>",self.get_cursor)




    #*************************Fetch Data**********************************
    def fetchData(self,rows):
        self.student_attendance_table.delete(*self.student_attendance_table.get_children())
        for i in rows:
            self.student_attendance_table.insert("",END,values=i)


    #*************************Import Data**********************************
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #*************************Export Data**********************************
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)





    #******************************************************************************
    def get_cursor(self,event=""):
        cursor_row=self.student_attendance_table.focus()
        content=self.student_attendance_table.item(cursor_row)
        rows=content['values']
        self.var_attendance_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_deprt.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])

    #********************************************************************************
    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_deprt.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()