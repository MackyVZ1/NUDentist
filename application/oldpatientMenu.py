import tkinter as tk
import datetime
import Checkyourself as c

from PIL import Image, ImageTk
from database import myCursor
from tkinter import ttk

# ฟังก์ชันเข้าหน้า "ผู้ป่วยที่มีประวัติแล้ว"
def oldPatientMenu():
    ## วัน/เวลา 
    # อัพเดทเวลาปัจจุบัน
    def UpdateTime():
        now = datetime.datetime.now() # เรียกใช้ datetime.now จาก library datetime 
        buddhistYear = now.year + 543 # แปลงจาก ค.ศ. เป็น พ.ศ
        thai_month = month_thai(now.month)
        date = f"{now.day} {thai_month} {buddhistYear}"
        time = f"{now.strftime('%H:%M:%S')}"     
        dateShow.config(text=date)
        timeShow.config(text=time)
            
        appWindow.after(1000, UpdateTime) # อัพเดทเวลาทุกๆ 1 วินาที
        
    # เดือนไทย
    def month_thai(month_num):
        months = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.",
                  "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
        return months[month_num - 1]    
    
    ## ฟังก์ชันแสดงข้อมูลคนไข้ที่มีประวัติแล้วโดยรับ input ข้อมูลของคนไข้
    def showInfo(patient_data):
        # ฟังก์ชันไปหน้าทำใบคัดกรอง
        def getCheckyourself():
            searchID = patientID_input.get() # ดึงข้อมูลจาก patientID_input เเล้วนำไปเก็บใน searchID
            # ถ้า searchID ป้อนมาเป็น ID
            if len(searchID) == 13: #
                dataFromMYSQL = [] # สร้าง list สำหรับการแปลงจาก tuple ที่ได้จากการดึงข้อมูล MySQL
                searchID_int = int(searchID)
                searchID_list = [searchID_int] # บรรทัดนี้เกิดขึ้นเพราะ MySQL รับพารามิเตอร์เป็น list จึงนำ searchID มาทำเป็น list
                myCursor.execute("SELECT * FROM Patient WHERE ID = %s", searchID_list) ### ดึงข้อมูลจาก database ###
                result = myCursor.fetchone() # ดึงข้อมูลจากแถวที่มี ID นั้น
                # เอาข้อมูลใน mySQL มาเก็บใน dataFromMYSQL เพื่อจะดึงค่ามาใช้
                for info in result:
                    dataFromMYSQL.append(info)
                print(dataFromMYSQL)
                # เช็คว่าอยู่ในคิวหรือยัง
                myCursor.execute("SELECT * FROM QueueInfo WHERE ID = %s", searchID_list) ### ดึงข้อมูลจาก database ###
                queueResult = myCursor.fetchone() # ดึงข้อมูลจากหน้าต่างคิว
                if queueResult == None:
                    # ไปหน้าทำใบคัดกรอง
                    appWindow.destroy()
                    c.makeCheckingYourself(dataFromMYSQL[0], dataFromMYSQL[1], dataFromMYSQL[2], dataFromMYSQL[3],
                                       dataFromMYSQL[4], dataFromMYSQL[5], dataFromMYSQL[6], dataFromMYSQL[7],
                                       dataFromMYSQL[8], dataFromMYSQL[9], dataFromMYSQL[10], dataFromMYSQL[11],
                                       dataFromMYSQL[12], dataFromMYSQL[13], dataFromMYSQL[14], dataFromMYSQL[15],
                                       dataFromMYSQL[16], dataFromMYSQL[17], dataFromMYSQL[18])
                                    ### ดึงข้อมูลจาก database ตาราง Patient ###
                # ถ้ามีข้อมูลในหน้าต่างคิวแล้ว
                else:
                    queueWarning = tk.Toplevel()
                    queueWarning.geometry("400x100")
                    queueWarning.resizable(False, False)
                    queuewarningLabel = tk.Label(queueWarning, text="อยู่ในคิวเรียบร้อยแล้ว กรุณารอเจ้าหน้าที่เรียกค่ะ", font=("FreesiaUPC",18), justify="center", anchor="center").pack()
                    okButton = tk.Button(queueWarning, text="ตกลง", font=("FreesiaUPC", 18), command=queueWarning.destroy)
                    okButton.place(relx=0.4, rely=0.4)
            # ถ้า searchID ป้อนมาเป็น DN
            if len(searchID) == 6: 
                dataFromMYSQL = [] # สร้าง list ไว้สำหรับแปลงจาก tuple ที่ดึงจาก MySQL
                searchID_list = [searchID]
                myCursor.execute("SELECT * FROM Patient WHERE DN = %s", searchID_list) ### ดึงข้อมูลจาก database ###
                result = myCursor.fetchone() # ดึงข้อมูลจากแถวที่มี ID นั้น
                # เอาข้อมูลใน mySQL มาเก็บใน dataFromMYSQL เพื่อจะดึงค่ามาใช้
                for info in result:
                    dataFromMYSQL.append(info)
                print(dataFromMYSQL)
                # เช็คว่าอยู่ในคิวหรือยัง
                myCursor.execute("SELECT * FROM QueueInfo WHERE DN = %s", searchID_list) ### ดึงข้อมูลจาก database ###
                queueResult = myCursor.fetchone() # ดึงข้อมูลจากหน้าต่างคิว
                if queueResult == None:
                    # ไปหน้าทำใบคัดกรอง
                    appWindow.destroy()
                    c.makeCheckingYourself(dataFromMYSQL[0], dataFromMYSQL[1], dataFromMYSQL[2], dataFromMYSQL[3],
                                       dataFromMYSQL[4], dataFromMYSQL[5], dataFromMYSQL[6], dataFromMYSQL[7],
                                       dataFromMYSQL[8], dataFromMYSQL[9], dataFromMYSQL[10], dataFromMYSQL[11],
                                       dataFromMYSQL[12], dataFromMYSQL[13], dataFromMYSQL[14], dataFromMYSQL[15],
                                       dataFromMYSQL[16], dataFromMYSQL[17], dataFromMYSQL[18])
                                    ### ดึงข้อมูลจาก database ตาราง Patient ###
                # ถ้ามีข้อมูลในหน้าต่างคิวแล้ว
                else:
                    queueWarning = tk.Toplevel()
                    queueWarning.geometry("400x100")
                    queueWarning.resizable(False, False)
                    queuewarningLabel = tk.Label(queueWarning, text="อยู่ในคิวเรียบร้อยแล้ว กรุณารอเจ้าหน้าที่เรียกค่ะ", font=("FreesiaUPC",18), justify="center", anchor="center").pack()
                    okButton = tk.Button(queueWarning, text="ตกลง", font=("FreesiaUPC", 18), command=queueWarning.destroy)
                    okButton.place(relx=0.4, rely=0.4)
        # สร้างกรอบภายในหน้าต่างแอป
        info_window = tk.Label(appWindow, image=frameImage)
        info_window.place(relx=0.04, rely=0.28)
        
        getcheckyourselfButton = tk.Button(info_window, command=getCheckyourself, image=checkyourselfImage, bg="#DEA6D5", border=0)
        getcheckyourselfButton.place(relx=0.75, rely=0.09)
        
        # สร้าง Treeview แสดงข้อมูลที่ได้จากการใส่ข้อมูลของคนไข้
        # โดยจะแสดง DN / ชื่อ - สกุล / ID / อายุ(ปี)
        oldpatientInfo = ttk.Treeview(info_window, columns=("Name", "ID", "Age"), height=16)
        oldpatientInfo.heading("#0", text="DN")
        oldpatientInfo.heading("Name", text="ชื่อ - สกุล")
        oldpatientInfo.heading("ID", text="ID")
        oldpatientInfo.heading("Age", text="อายุ(ปี)")
        # สร้าง list เพื่อเก็บข้อมูลจากผู้ป่วยที่มีประวัติโดยดึงจาก patient_data
        oldpatientInfo_list = []
        for info in patient_data:
            oldpatientInfo_list.append(info)
        #print(oldpatientInfo_list)
        # เพิ่มข้อมูลลง treeview
        oldpatientInfo.insert(
            "",
            tk.END,
            text = oldpatientInfo_list[0], # DN
            values = (oldpatientInfo_list[1] + " " + oldpatientInfo_list[2], oldpatientInfo_list[3], oldpatientInfo_list[4])
            # ชื่อ-สกุล, ID, อายุ
        )
        oldpatientInfo.place(relx=0.02, rely=0.09)
        # เอาไว้เช็คค่าเฉยๆ
        # print(oldpatientInfo.get_children())
        
    # ฟังก์ชันยืนยัน ID เพื่อค้นหาประวัติ
    def submitID():
        if patientID_input.get():
            searchID()
        else:
            warning_show()
    # ฟังก์ชันแสดงเมื่อค้นหาประวัติไม่เจอ
    def notFound():
        notFound_window = tk.Toplevel()
        notFound_window.title("คำเตือน")
        notFound_window.geometry("300x110")
        notFound_window.resizable(False, False)
        warning_label = tk.Label(notFound_window, text="ไม่พบข้อมูล", font=("FreesiaUPC", 18), anchor="center").pack()
        ok_button = tk.Button(notFound_window, text="OK", font=("FreesiaUPC", 18), anchor="center", width=5, command=notFound_window.destroy).pack(padx=10, pady=10)
    # ฟังก์ชันหาประวัติด้วยการกรอก ID/DN
    def searchID():
        # ดึงข้อมูล ID/DN มาใช้เพื่อหาชุดข้อมูลที่มี ID นั้นๆ
        searchID = patientID_input.get()
        # ID
        if len(searchID) == 13:
            searchID_int = int(searchID)
            searchID_list = [searchID_int] # บรรทัดนี้เกิดขึ้นเพราะ MySQL รับพารามิเตอร์เป็น list หรือ tuple จึงนำ searchID มาทำเป็น list
            myCursor.execute("SELECT DN, thaiName, thaiSurname, ID, age FROM Patient WHERE ID = %s", searchID_list) ### ดึงข้อมูลจาก database ###
            result = myCursor.fetchone() # ดึงข้อมูลจากแถวที่มี ID นั้น   
            # ตรวจสอบว่ามีเลขบัตรประจำตัวประชาชนในระบบมั้ย
            if result:
                showInfo(result)
            else:
                notFound()
        # DN
        if len(searchID) == 6:
            searchID_str = str(patientID_input.get())
            searchID_list = [searchID_str] # บรรทัดนี้เกิดขึ้นเพราะ MySQL รับพารามิเตอร์เป็น list หรือ tuple จึงนำ searchID มาทำเป็น list
            myCursor.execute("SELECT DN, thaiName, thaiSurname, ID, age FROM Patient WHERE DN = %s", searchID_list) ### ดึงข้อมูลจาก database ###
            result = myCursor.fetchone() # ดึงข้อมูลจากแถวที่มี DN นั้น   
            # ตรวจสอบว่ามีเลขบัตรประจำตัวประชาชนในระบบมั้ย
            if result:
                showInfo(result)
            else:
                notFound()
        if len(searchID) != 6 and len(searchID) != 13:
            warning_show()
              
    def warning_show():
        warning_screen = tk.Toplevel()
        warning_screen.title("คำเตือน")
        warning_screen.geometry("300x110")
        warning_screen.resizable(False, False)
        warning_label = tk.Label(warning_screen, text="กรอกข้อมูลให้ถูกต้อง", font=("FreesiaUPC", 18), anchor="center").pack()
        ok_button = tk.Button(warning_screen, text="OK", font=("FreesiaUPC", 18), anchor="center", command=warning_screen.destroy).pack(padx=10, pady=10)
    
    ## ฟังก์ชันควบคุมการทำงานของ mouse pointer ตอนเอาเมาส์ชี้ที่ปุ่ม        
    def on_enter(event):
        # ลดขนาดปุ่มลง 3%
        current_width = event.widget.winfo_width()
        current_height = event.widget.winfo_height()
        new_width = int(current_width * 0.97)
        new_height = int(current_height * 0.97)
        event.widget.config(width=new_width, height=new_height)
        
    ## ฟังก์ชันควบคุมการทำงานของ mouse pointer ตอนเอาเมาส์ชี้ออกจากปุ่ม     
    def on_leave(event):
        # คืนขนาดปุ่มกลับเป็นขนาดเดิม
        original_width = event.widget.original_width
        original_height = event.widget.original_height
        event.widget.config(width=original_width, height=original_height)
    
    # สร้างหน้าเมนู
    appWindow = tk.Toplevel()
    appWindow.title("ผู้ป่วยที่มีประวัติแล้ว")
    appWindow.geometry("1280x620")
    appWindow.resizable(False, False)
    appWindow.config(bg="white")
    
    # โหลดรูปภาพ
    image1 = Image.open("components/bg.png") # พื้นหลัง
    image2 = Image.open("components/oldpatient_background.png") # พื้นหลังกรอบแสดงข้อมูลคนไข้
    image3 = Image.open("components/search.png") # ปุ่มค้นหา
    image4 = Image.open("components/checkyourself.png") # ปุ่มกดทำใบคัดกรอง
    bgImage = ImageTk.PhotoImage(image1)
    frameImage = ImageTk.PhotoImage(image2)
    searchImage = ImageTk.PhotoImage(image3)
    checkyourselfImage = ImageTk.PhotoImage(image4)
    bgLabel = tk.Label(appWindow, image=bgImage).pack()
    
    findInfo_label = tk.Label(appWindow, text="ค้นหาประวัติคนไข้", font=("FreesiaUPC", 24, "bold"), anchor="center", bg="white")
    findInfo_label.place(relx=0.23, rely=0.1)
    
    dateShow = tk.Label(appWindow, font=("FreesiaUPC", 18), bg="white")
    timeShow = tk.Label(appWindow, font=("FreesiaUPC", 18), bg="white")
    dateShow.place(relx=0.9, rely=0.05)
    timeShow.place(relx=0.91, rely=0.1)
    
    # รับค่า ID/DN ของคนไข้
    patientID_input = tk.Entry(appWindow, font=("FreesiaUPC",18), relief="sunken", borderwidth=5, width=25)
    patientID_input.place(relx=0.38, rely=0.11)
    patient_warning = tk.Label(appWindow, text="กรอก DN หรือ เลขบัตรประจำตัวประชาชน", font=("FreesiaUPC", 16), bg="white")
    patient_warning.place(relx=0.38, rely=0.18)
    
    # ปุ่มกดยืนยันข้อมูลจากการพิมพ์ ID หรือ DN
    submitButton = tk.Button(appWindow, text="ยืนยัน", font=("FreesiaUPC", 18), command=submitID, image=searchImage, border=0, bg="white")
    submitButton.place(relx=0.615, rely=0.1)
    
    
    # บันทึกขนาดเดิมของปุ่ม
    appWindow.update()  # อัพเดทหน้าต่างเพื่อให้ได้ขนาดปุ่มที่ถูกต้อง
    submitButton.original_width = submitButton.winfo_width()
    submitButton.original_height = submitButton.winfo_height()
    submitButton.bind("<Enter>", on_enter)
    submitButton.bind("<Leave>", on_leave)
    
    UpdateTime() # เรียกใช้เพื่ออัพเดทเวลา
    appWindow.mainloop()
    
#oldPatientMenu()