import tkinter as tk
import mysql.connector

from CheckInfo import checkInfo
from tkinter import ttk
from PIL import Image, ImageTk
def StaffMenu():
    # ฟังก์ชันเมื่อเวลากดปิดโปรแกรม จะทำการหยุดเชื่อมต่อกับ database
    def closeApp():
        if db.is_connected():
            db.close()
        appWindow.destroy()
    # รีเฟรชข้อมูล
    def refresh():
        db.commit()
    # ก่อนจะกดใส่เลขDN   
    def prepareDN():
        # ----------------------
        infoList = newRecord # [ลำดับคิว, ชื่อ-สกุล, ID]
        idList = [] # สร้าง list สำหรับหาข้อมูล sql
        idList.append(infoList[2]) # เพิ่ม id ลงใน list
        myCursor.execute("SELECT * FROM QueueInfo WHERE ID = %s", idList)
        result = myCursor.fetchone() # ได้ tuple
        newData = [] # แปลง tuple เป็น list
        for data in result: # เอาข้อมูลใน tuple มาเก็บใน list เพื่อให้สามารถนำข้อมูลแต่ละ index ไปเก็บใน sql ได้
            newData.append(data)
        #print(newData) เอาไว้เช็คค่า 
        # กรณีเป็นผู่ป่วยใหม่ยังไม่มี DN
        if newData[1] == None:
            checkInfo(newData)
            myCursor.execute("DELETE FROM QueueInfo WHERE ID = %s", idList)
            db.commit
        # กรณีเป็นผู้ป่วยเก่ามี DN แล้ว
        else:
            # ลบข้อมูลชั่วคราวที่เก็บทิ้ง
            myCursor.execute("DELETE FROM QueueInfo WHERE ID = %s", idList)
            db.commit()
        # -----------------------
    # แสดงคิว
    def queueInfo(): 
        # ----------------------------    
        def item_selected(event):
            # --------------------------
            for seleced_item in queueTreeview.selection():
                # เก็บค่าจาก item ที่เลือก
                item = queueTreeview.item(seleced_item)
                # เอาค่าแต่ละค่ามาแสดง ผลลัพธ์ได้เป็น list
                global newRecord
                record = item['values']
                newRecord = [record[0], record[2], record[3]] # [ลำดับคิวที่, ชื่อ-สกุล, ID]
                
                #print(newRecord) เอาไว้เช็คค่า
            # -------------------------
        # อัพเดทตาราง
        def update_treeview():
            # ----------------------------
            # ลบข้อมูลเก่าทั้งหมดใน Treeview
            for item in queueTreeview.get_children():
                queueTreeview.delete(item)

            # ดึงข้อมูลใหม่จากฐานข้อมูลตาราง QueueInfo
            myCursor.execute("SELECT * FROM QueueInfo")
            patientQueue = myCursor.fetchall()

            # เพิ่มข้อมูลใหม่เข้า Treeview
            for row in range(len(patientQueue)):
                queueTreeview.insert(
                    "",
                    tk.END,
                    text=patientQueue[row][0], # เวลา
                    value=(row+1, patientQueue[row][1], patientQueue[row][2] + patientQueue[row][3] + " " + patientQueue[row][4], patientQueue[row][8])
                    # ลำดับคิวที่, DN, ชื่อ-สกุล, ID
                )
            # ----------------------------
        # ----------------           
        # สร้าง Treeview ถ้ายังไม่มี
        # ตารางแสดง เวลา/ลำดับคิว/ชื่อ-สกุล/ID
        if 'queueTreeview' not in globals():
            queueTreeview = ttk.Treeview(frameBackground, columns=("Queue", "DN","Name", "ID"), height=22)
            queueTreeview.heading("#0", text="เวลา")
            queueTreeview.heading("DN", text="DN")
            queueTreeview.heading("Queue", text="คิวที่")
            queueTreeview.heading("Name", text="ชื่อ - สกุล")
            queueTreeview.heading("ID", text="ID")
            queueTreeview.place(relx=0.06, rely=0.07)
            queueTreeview.bind("<<TreeviewSelect>>", item_selected)

        # อัพเดทข้อมูลใน Treeview
        update_treeview()
        # ตั้งเวลาให้เรียกฟังก์ชันนี้อีกครั้งหลังจาก 5 วินาที
        appWindow.after(5000, queueInfo)
    # ตัวแปรเก็บค่าจากการเลือก item (ข้อมูลคนไข้)
    selecteds_item = []    
    # ----------------------------------------
    # เชื่อมต่อกับ database ที่สร้างไว้
    db = mysql.connector.connect(
        host="localhost", # sql12.freesqldatabase.com
        database="patient_info", # sql12718944
        user="root", # sql12718944
        password="1234", # 1DYCQpAPGS
        port="3306"
    )
    # ตรวจสอบว่าเชื่อมต่อแล้วรึยัง
    if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server Version", db_Info)
        myCursor = db.cursor()
        
    appWindow = tk.Tk()
    appWindow.title("สำหรับเจ้าหน้าที่")
    appWindow.geometry("1280x720")
    appWindow.resizable(False, False)
    appWindow.config(bg="white")
    # import รูป
    image1 = Image.open("components/checkinfo.png")
    image2 = Image.open("components/refresh.png")
    checkinfoImage = ImageTk.PhotoImage(image1)
    refreshImage = ImageTk.PhotoImage(image2)
    
    # Label & Button
    staffLabel = tk.Label(appWindow, text="คิวรอพิมพ์ทำข้อมูล",font=("FreesiaUPC", 62, "bold"), bg="white")
    staffLabel.place(relx=0.05, rely=0.05)
    
    # Frame
    frameBackground = tk.Frame(appWindow, width=1160, height=540, bg="#DEA6D5")
    frameBackground.place(relx=0.039, rely=0.22)
    checkinfoButton = tk.Button(appWindow, image=checkinfoImage, border=0, bg="white", command=prepareDN)
    refreshButton = tk.Button(appWindow, image=refreshImage, border=0, bg="white", command=refresh)
    checkinfoButton.place(relx=0.58, rely=0.05)
    refreshButton.place(relx=0.78, rely=0.05)
    
    queueInfo()
    
    appWindow.protocol("WM_DELETE_WINDOW", closeApp)
    appWindow.mainloop()
    
StaffMenu()