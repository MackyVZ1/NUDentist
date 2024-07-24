import tkinter as tk
import datetime

from PIL import Image, ImageTk
from database import myCursor, db
from Printer import print_file
from temporaryInfo import temp_info
from tkinter import ttk

## ฟังก์ชันเข้าหน้าทำใบคัดกรอง
def makeCheckingYourself(
    DN,
    thai_title,
    thai_name,
    thai_surname,
    engTitle,
    engName,
    engSurname,
    ID,
    birthdate,
    age,
    gender,
    status,
    job,
    address,
    phoneNum,
    emergencyName,
    relation,
    emergencyNum,
    emergencyAddress,
):
    #ข้อตกลงก่อนกดตกลง
    def makesureyouInfo():
        # ฟังก์ชันกดปุ่ม "ตกลง"
        def submit():
            warning_screen.destroy()
            tempInfo = temp_info()
            #ส่งข้อมูลไปหน้ารอคิว
            # filename = tempInfo.makeDocument(
            #         thai_title,
            #         thai_name,
            #         thai_surname,
            #         ID,
            #         address,
            #         tempVar.get(),
            #         bloodtopVar.get(),
            #         bloodbottomVar.get(),
            #         hearrateVar.get(),
            #         checkbox1Var.get(),
            #         checkbox2Var.get(),
            #         checkbox3Var.get(),
            #         checkbox4Var.get(),
            #         checkbox5Var.get(),
            #         checkbox6Var.get(),
            #         checkbox7Var.get(),
            #         checkbox8Var.get(),
            #         checkbox9Var.get(),
            #         checkbox10Var.get(),
            #         checkbox11Var.get(),
            #         checkbox12Var.get(),
            #         checkbox13Var.get(),
            #         checkbox14Var.get(),
            #         checkbox15Var.get(),
            #         checkbox15inputVar.get(),
            #         checkbox16Var.get(),
            #         checkbox17Var.get(),
            #         checkbox18Var.get(),
            #         checkbox19Var.get(),
            #         checkbox20Var.get(),
            #         checkbox21Var.get(),
            #         checkbox22Var.get(),
            #         checkbox23Var.get(),
            #         checkbox24Var.get(),
            #         checkbox25Var.get(),
            #         checkbox26Var.get(),
            #         checkbox27Var.get(),
            #         checkbox28Var.get(),
            #         checkbox29Var.get(),
            #         checkbox30Var.get(),
            #         checkbox30inputVar.get())
            #print_file(filename)
            ### ส่งข้อมูลไป database ตารางชื่อ QueueInfo /ดึงข้อมูลจาก database ###
            tempdata = "INSERT INTO QueueInfo(Time, DN, thaiTitle, thaiName, thaiSurname, engTitle, engName, engSurname, ID, birthdate, age, gender, status, job, address, phoneNum, emergencyName, relation, emergencyNum, emergencyAddress, tempVar, bloodtopVar, bloodbottomVar, hearrateVar, checkbox1Var, checkbox2Var, checkbox3Var, checkbox4Var, checkbox5Var, checkbox6Var, checkbox7Var, checkbox8Var, checkbox9Var, checkbox10Var , checkbox11Var, checkbox12Var, checkbox13Var, checkbox14Var, checkbox15Var, checkbox15inputVar, checkbox16Var, checkbox17Var, checkbox18Var, checkbox19Var, checkbox20Var, checkbox21Var, checkbox22Var, checkbox23Var, checkbox24Var, checkbox25Var, checkbox26Var, checkbox27Var, checkbox28Var, checkbox29Var, checkbox30Var, checkbox30inputVar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (timer, DN, thai_title, thai_name, thai_surname, engTitle, engName, engSurname, ID, birthdate, age, gender, status, job, address, phoneNum, emergencyName, relation, emergencyNum, emergencyAddress, tempVar.get(), bloodtopVar.get(), bloodbottomVar.get(), hearrateVar.get(), checkbox1Var.get(), checkbox2Var.get(), checkbox3Var.get(), checkbox4Var.get(), checkbox5Var.get(), checkbox6Var.get(), checkbox7Var.get(), checkbox8Var.get(), checkbox9Var.get(), checkbox10Var.get(), checkbox11Var.get(), checkbox12Var.get(), checkbox13Var.get(), checkbox14Var.get(), checkbox15Var.get(), checkbox15inputVar.get(), checkbox16Var.get(), checkbox17Var.get(), checkbox18Var.get(), checkbox19Var.get(), checkbox20Var.get(), checkbox21Var.get(), checkbox22Var.get(), checkbox23Var.get(), checkbox24Var.get(), checkbox25Var.get(), checkbox26Var.get(), checkbox27Var.get(), checkbox28Var.get(), checkbox29Var.get(), checkbox30Var.get(), checkbox30inputVar.get())
            myCursor.execute(tempdata, values)
            db.commit()
            
            appWindow.destroy()
        warning_screen = tk.Toplevel()
        warning_screen.title("คำเตือน")
        warning_screen.geometry("600x200")
        warning_screen.resizable(False, False)
        warningLabel = tk.Label(
            warning_screen,
            text="ข้าพเจ้าขอรับรองว่าข้อความข้างต้นเป็นความจริงทุกประการ\nการปกปิดหรือให้ข้อมูลอันเป็นเท็จ อาจะมีความผิดตาม พ.ร.บ. โรคติดต่อ",
            font=("FreesiaUPC", 18)
        )
        warningLabel.place(relx=0.11, rely=0.25)
        submitButton = tk.Button(
            warning_screen, text="ตกลง", font=("FreesiaUPC", 22), command=submit
        )
        submitButton.place(relx=0.4, rely=0.65, width=100)

    # update เวลาจริง
    def UpdateTime():
        now = datetime.datetime.now()
        buddhistYear = now.year + 543
        thai_month = month_thai(now.month)
        date = f"{now.day} {thai_month} {buddhistYear}"
        time = f"{now.strftime('%H:%M:%S')}"
        dateShow.config(text=date)
        timeShow.config(text=time)
        global timer
        timer = timeShow.cget("text")
        
        appWindow.after(1000, UpdateTime)

    # เดือนไทย
    def month_thai(month_num):
        months = [
            "ม.ค.",
            "ก.พ.",
            "มี.ค.",
            "เม.ย.",
            "พ.ค.",
            "มิ.ย.",
            "ก.ค",
            "ส.ค.",
            "ก.ย.",
            "ต.ค",
            "พ.ย.",
            "ธ.ค.",
        ]
        return months[month_num - 1]
    
    # เช็คว่า checkbox15 ถูกติ๊กมั้ย
    def ischeckbox15():
        if checkbox15Var.get() == 1:
            checkbox15Input.config(state="normal")
        else:
            checkbox15Input.config(state="disabled")
            
    # เช็คว่า checkbox30 ถูกติ๊กมั้ย       
    def ischeckbox30():
        if checkbox30Var.get() == 1:
            checkbox30Input.config(state="normal")
        else:
            checkbox30Input.config(state="disabled")
            
    # ฟังก์ชันควบคุมการทำงานของ mouse pointer เมื่อปุ่มถูกชี้
    def on_enter(event):
        # ลดขนาดปุ่มลง 3%
        current_width = event.widget.winfo_width()
        current_height = event.widget.winfo_height()
        new_width = int(current_width * 0.97)
        new_height = int(current_height * 0.97)
        event.widget.config(width=new_width, height=new_height)
        
    # ฟังก์ชันควบคุมการทำงานของ mouse pointer เมื่อปุ่มไม่ถูกชี้   
    def on_leave(event):
        # คืนขนาดปุ่มกลับเป็นขนาดเดิม
        original_width = event.widget.original_width
        original_height = event.widget.original_height
        event.widget.config(width=original_width, height=original_height)
        
    ### สร้างหน้าต่างสำหรับทำการคัดกรอง
    appWindow = tk.Toplevel()
    appWindow.title("แบบคัดกรองโรงพยาบาลทันตกรรม มหาวิทยาลัยนเรศวร")
    appWindow.geometry("1366x768")
    appWindow.resizable(False, False)
    appWindow.config(bg="white")
    
    image = Image.open("components/submitButton.png")
    submitImage = ImageTk.PhotoImage(image)

    ### แสดงวันที่/เวลาบนหน้าจอ
    dateShow = tk.Label(appWindow, font=("FreesiaUPC", 18), bg="white")
    timeShow = tk.Label(appWindow, font=("FreesiaUPC", 18), bg="white")
    dateShow.place(relx=0.915, rely=0.02)
    timeShow.place(relx=0.93, rely=0.07)

    ### ข้อความต่างๆ ที่จะแสดงบนหน้าจอ
    titleLabel = tk.Label(appWindow, text="แบบคัดกรองโรงพยาบาลทันตกรรม มหาวิทยาลัยนเรศวร", font=("FreesiaUPC", 22, "bold"), bg="white")
    nameLabel = tk.Label(appWindow, text="ชื่อผู้ป่วย: ", font=("FreesiaUPC", 20, "bold"), bg="white")
    namefromData = tk.Label(appWindow, text=f"{thai_title}{thai_name} {thai_surname}", font=("FreesiaUPC", 18), bg="white")
    
    titleLabel.place(relx=0.32, rely=0.02)
    nameLabel.place(relx=0.04, rely=0.08)
    namefromData.place(relx=0.1, rely=0.08)

    ### ผลการวัดอุณหภูมิ / ความดัน / ชีพจร
    tempVar = tk.StringVar()
    bloodtopVar = tk.StringVar()
    bloodbottomVar = tk.StringVar()
    hearrateVar = tk.StringVar()
    bloodPressureLabel = tk.Label(appWindow, text="ความดันโลหิต", font=("FreesiaUPC", 20, "bold"), bg="white")
    bloodPressureLabel.place(relx=0.04, rely=0.15)
    tempbloodFrame = ttk.Frame(appWindow, width=500, height=110, relief="solid", borderwidth=1)
    tempbloodFrame.place(relx=0.14, rely=0.15)
    tempbloodCanvas = tk.Canvas(tempbloodFrame, width=500, height=100)
    tempbloodCanvas.pack()
    bloodPressureTOPLabel = tk.Label(tempbloodCanvas, text="SYS                mmHg(เลขบน)", font=("FreesiaUPC", 18))
    bloddPressureBOTTOMLabel = tk.Label(tempbloodCanvas, text="DIA                 mmHg(เลขล่าง)", font=("FreesiaUPC", 18))
    heartrateLabel = tk.Label(tempbloodCanvas, text="P.R.                 ครั้ง/นาที", font=("FreesiaUPC", 18))
    tempLabel = tk.Label(tempbloodCanvas, text="อุณหภูมิ                 °C", font=("FreesiaUPC", 18))
    
    bloodPressureTOPLabel.place(relx=0.02, rely=0.07)
    bloddPressureBOTTOMLabel.place(relx=0.54, rely=0.07)
    heartrateLabel.place(relx=0.02, rely=0.63)
    tempLabel.place(relx=0.54, rely=0.63)
    
    tempbloodCanvas.create_line(0, 55, 500, 55, fill="grey")  # (xเริ่ม, yเริ่ม, xจบ, yจบ)
    
    tempInput = tk.Entry(tempbloodCanvas, font=("FreesiaUPC", 18), width=5, textvariable=tempVar, relief="sunken", borderwidth=4)
    bloodPressureTOPInput = tk.Entry(tempbloodCanvas, font=("FreesiaUPC", 18), width=5, textvariable=bloodtopVar, relief="sunken", borderwidth=4)
    bloodPressureBOTTOMInput = tk.Entry(tempbloodCanvas, font=("FreesiaUPC", 18), width=5, textvariable=bloodbottomVar, relief="sunken", borderwidth=4)
    heartrateInput = tk.Entry(tempbloodCanvas, font=("FreesiaUPC", 18), width=5, textvariable=hearrateVar, relief="sunken", borderwidth=4)

    bloodPressureTOPInput.place(relx=0.1, rely=0.09)
    bloodPressureBOTTOMInput.place(relx=0.62, rely=0.09)
    heartrateInput.place(relx=0.1, rely=0.605)
    tempInput.place(relx=0.68, rely=0.605)

    ### แบบคัดกรองโรคติดเชื้อ
    ## โรคไข้หวัด
    checkbox1Var = tk.IntVar()  # 0 : ไม่ถูกติ๊ก / 1 : ถูกติ๊ก
    checkbox2Var = tk.IntVar()
    checkbox3Var = tk.IntVar()
    checkbox4Var = tk.IntVar()
    checkbox5Var = tk.IntVar()
    checkbox6Var = tk.IntVar()
    checkbox7Var = tk.IntVar()
    infectedcheckLabel = tk.Label(appWindow, text="แบบคัดกรองโรคติดเชื้อ", font=("FreesiaUPC", 20, "bold"), bg="white")
    infectedcheckLabel.place(relx=0.04, rely=0.305)
    
    infectedcheckFrame = ttk.Frame(appWindow, width=1280, height=380, relief="solid", borderwidth=1)
    infectedcheckFrame.place(relx=0.032, rely=0.35)
    feverCanvas = tk.Canvas(infectedcheckFrame, width=1280, height=380)
    feverCanvas.pack()
    
    feverLabel = tk.Label(feverCanvas, text="โรคไข้หวัด", font=("FreesiaUPC", 18, "bold"))
    feverLabel.place(relx=0.01, rely=0.015)
    checkbox1 = tk.Checkbutton(feverCanvas, text="ไม่มีอาการเหล่านี้", font=("FreesiaUPC", 18), variable=checkbox1Var)
    checkbox2 = tk.Checkbutton(feverCanvas, text="1.มีไข้ (อุณหภูมิ > 37.5 °C)",font=("FreesiaUPC", 18),variable=checkbox2Var)
    checkbox3 = tk.Checkbutton(feverCanvas, text="2.ไอ จาม มีน้ำมูก",font=("FreesiaUPC", 18),variable=checkbox3Var)
    checkbox4 = tk.Checkbutton(feverCanvas, text="3.มีเสมหะ เจ็บคอ", font=("FreesiaUPC", 18), variable=checkbox4Var)
    checkbox5 = tk.Checkbutton(feverCanvas, text="4.ปวดศีรษะ", font=("FreesiaUPC", 18), variable=checkbox5Var)
    checkbox6 = tk.Checkbutton(feverCanvas, text="5.มีอ่อนเพลีย", font=("FreesiaUPC", 18), variable=checkbox6Var)
    checkbox7 = tk.Checkbutton(feverCanvas, text="6.ปวดกล้ามเนื้อ", font=("FreesiaUPC", 18), variable=checkbox7Var)
    
    # จัดเรียง checkbox
    checkbox1.place(relx=0.02, rely=0.1)
    checkbox2.place(relx=0.02, rely=0.18)
    checkbox3.place(relx=0.02, rely=0.26)
    checkbox4.place(relx=0.02, rely=0.34)
    checkbox5.place(relx=0.02, rely=0.42)
    checkbox6.place(relx=0.02, rely=0.5)
    checkbox7.place(relx=0.02, rely=0.58)
    
    feverCanvas.create_line(260, 0, 260, 380, fill="grey")  # (xเริ่ม, yเริ่ม, xจบ, yจบ)
    
    ## โรควัณโรค
    checkbox8Var = tk.IntVar()
    checkbox9Var = tk.IntVar()
    checkbox10Var = tk.IntVar()
    checkbox11Var = tk.IntVar()
    checkbox12Var = tk.IntVar()
    checkbox13Var = tk.IntVar()
    checkbox14Var = tk.IntVar()
    checkbox15Var = tk.IntVar()
    checkbox15inputVar = tk.StringVar()
    checkbox16Var = tk.IntVar()
    deseaseLabel = tk.Label(feverCanvas, text="โรควัณโรค", font=("FreesiaUPC", 18, "bold"))
    deseaseLabel.place(relx=0.21, rely=0.015)
    checkbox8 = tk.Checkbutton(feverCanvas,text="ไม่มีอาการ",font=("FreesiaUPC", 18),variable=checkbox8Var)
    checkbox9 = tk.Checkbutton(feverCanvas, text="1.ไอเรื้อรังเกิน 2 สัปดาห์", font=("FreesiaUPC", 18), variable=checkbox9Var)
    checkbox10 = tk.Checkbutton(feverCanvas, text="2.ไอมีเลือดปน", font=("FreesiaUPC", 18), variable=checkbox10Var)
    checkbox11 = tk.Checkbutton(feverCanvas, text="3.น้ำหนักลด 3-5 กก./เดือนโดยไม่ทราบสาเหตุ", font=("FreesiaUPC", 18), variable=checkbox11Var)
    checkbox12 = tk.Checkbutton(feverCanvas, text="4.ไข้ตอนบ่ายเกิน 2 สัปดาห์", font=("FreesiaUPC", 18), variable=checkbox12Var)
    checkbox13 = tk.Checkbutton(feverCanvas, text="5.มีเหงื่อออกกลางคืนใน 1 เดือน", font=("FreesiaUPC", 18), variable=checkbox13Var)
    checkbox14 = tk.Checkbutton(feverCanvas, text="6.มีประวัติสัมผัสกับผู้ป่วยวัณโรค", font=("FreesiaUPC", 18), variable=checkbox14Var)
    checkbox15 = tk.Checkbutton(feverCanvas, text="7.กำลังรักษาโรควัณโรค (ระยะเวลาในการรักษา                     )", font=("FreesiaUPC", 18), variable=checkbox15Var, command=ischeckbox15)
    checkbox15Input = tk.Entry(feverCanvas, textvariable=checkbox15inputVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, state="disabled", width=8)
    deseasehistoryLabel = tk.Label(feverCanvas, text="ประวัติผู้ป่วยวัณโรค", font=("FreesiaUPC", 18))
    checkbox16 = tk.Checkbutton(feverCanvas, text="เคยมีประวัติเป็นโรควัณโรคและมีใบรับรองแพทย์ว่าไม่พบเชื้อ ระยะเวลาไม่เกิน 1 เดือน", font=("FreesiaUPC", 18), variable=checkbox16Var)
    
    # จัดเรียก checkbox
    checkbox8.place(relx=0.22, rely=0.1)
    checkbox9.place(relx=0.22, rely=0.18)
    checkbox10.place(relx=0.22, rely=0.26)
    checkbox11.place(relx=0.22, rely=0.34)
    checkbox12.place(relx=0.22, rely=0.42)
    checkbox13.place(relx=0.22, rely=0.5)
    checkbox14.place(relx=0.22, rely=0.58)
    checkbox15.place(relx=0.22, rely=0.66)
    checkbox15Input.place(relx=0.489, rely=0.66)
    deseasehistoryLabel.place(relx=0.21, rely=0.8)
    checkbox16.place(relx=0.22, rely=0.88)
    
    feverCanvas.create_line(890, 0, 890, 380, fill="grey")  # (xเริ่ม, yเริ่ม, xจบ, yจบ)
    ## โรคเริมและงูสวัด
    checkbox17Var = tk.IntVar()
    checkbox18Var = tk.IntVar()
    checkbox19Var = tk.IntVar()
    checkbox20Var = tk.IntVar()
    checkbox21Var = tk.IntVar()
    checkbox22Var = tk.IntVar()
    checkbox23Var = tk.IntVar()
    
    herpesLabel = tk.Label(feverCanvas, text="โรคเริมและงูสวัด", font=("FreesiaUPC", 18, "bold"))
    herpesLabel.place(relx=0.7, rely=0.015)
    checkbox17 = tk.Checkbutton(feverCanvas, text="ไม่มีอาการ", font=("FreesiaUPC", 18), variable=checkbox17Var)
    checkbox18 = tk.Checkbutton(feverCanvas, text="1.มีตุ่มน้ำที่ริมฝีปาก", font=("FreesiaUPC", 18), variable=checkbox18Var)
    checkbox19 = tk.Checkbutton(feverCanvas, text="2.แผลที่มีอาการเจ็บร้อนที่ริมฝีปาก", font=("FreesiaUPC", 18), variable=checkbox19Var)
    checkbox20 = tk.Checkbutton(feverCanvas, text="3.มีตุ่มน้ำใสเป็นแนวยาวตามผิวหนังร่างกาย", font=("FreesiaUPC", 18), variable=checkbox20Var)
    checkbox21 = tk.Checkbutton(feverCanvas, text="4.รู้สึกเจ็บแปลบบริเวณผิวหนัง", font=("FreesiaUPC", 18), variable=checkbox21Var)
    checkbox22 = tk.Checkbutton(feverCanvas, text="5.รู้สึกคัน ปวดแสบ ปวดร้อน บริเวณผิวหนัง", font=("FreesiaUPC", 18), variable=checkbox22Var)
    checkbox23 = tk.Checkbutton(feverCanvas, text="6.มีประวัติเคยเป็นเริมหรืองูสวัด", font=("FreesiaUPC", 18), variable=checkbox23Var)
    
    # จัดเรียง checkbox
    checkbox17.place(relx=0.71, rely=0.1)
    checkbox18.place(relx=0.71, rely=0.18)
    checkbox19.place(relx=0.71, rely=0.26)
    checkbox20.place(relx=0.71, rely=0.34)
    checkbox21.place(relx=0.71, rely=0.42)
    checkbox22.place(relx=0.71, rely=0.5)
    checkbox23.place(relx=0.71, rely=0.58)
    
    ### แบบคัดกรองโรคไม่ติดเชื้อ
    checkbox24Var = tk.IntVar()
    checkbox25Var = tk.IntVar()
    checkbox26Var = tk.IntVar()
    checkbox27Var = tk.IntVar()
    checkbox28Var = tk.IntVar()
    checkbox29Var = tk.IntVar()
    checkbox30Var = tk.IntVar()
    checkbox30inputVar = tk.StringVar()
    notdeseaseLabel = tk.Label(appWindow, text="แบบคัดกรองโรคไม่ติดเชื้อ", font=("FreesiaUPC", 20, "bold"), bg="white")
    notdeseaseLabel.place(relx=0.04, rely=0.86)
    checkbox24 = tk.Checkbutton(appWindow, text="โรคความดันโลหิตสูง", font=("FreesiaUPC", 18), bg="white", variable=checkbox24Var)
    checkbox25 = tk.Checkbutton(appWindow, text="โรคเบาหวาน", font=("FreesiaUPC", 18), bg="white", variable=checkbox25Var)
    checkbox26 = tk.Checkbutton(appWindow, text="โรคหัวใจ", font=("FreesiaUPC", 18), bg="white", variable=checkbox26Var)
    checkbox27 = tk.Checkbutton(appWindow, text="โรคไทรอยด์", font=("FreesiaUPC", 18), bg="white", variable=checkbox27Var)
    checkbox28 = tk.Checkbutton(appWindow, text="เคยมีประวัติเป็นโรคหลอดเลือดสมอง (stroke) หรือเคยมีอาการ", font=("FreesiaUPC", 18), bg="white", variable=checkbox28Var)
    checkbox29 = tk.Checkbutton(appWindow, text="โรคภูมิคุ้มกันบกพร่อง", font=("FreesiaUPC", 18), bg="white", variable=checkbox29Var)
    checkbox30 = tk.Checkbutton(appWindow, text="สตรีมีครรภ์ อายุครรภ์             เดือน", font=("FreesiaUPC", 18), bg="white", variable=checkbox30Var, command=ischeckbox30)
    checkbox30Input = tk.Entry(appWindow,font=("FreesiaUPC", 18), bg="white", textvariable=checkbox30inputVar, relief="sunken", borderwidth=4, width=4, state="disabled")
    ## จัดเรียง checkbox
    checkbox24.place(relx=0.22, rely=0.86)
    checkbox25.place(relx=0.35, rely=0.86)
    checkbox26.place(relx=0.44, rely=0.86)
    checkbox27.place(relx=0.515, rely=0.86)
    checkbox28.place(relx=0.04, rely=0.92)
    checkbox29.place(relx=0.6, rely=0.86)
    checkbox30.place(relx=0.38, rely=0.92)
    checkbox30Input.place(relx=0.51, rely=0.92)

    # ปุ่มกดยืนยัน
    makesureButton = tk.Button(appWindow, text="ยืนยัน", font=("FreesiaUPC", 18, "bold"), bg="white", border=0, image=submitImage, command=makesureyouInfo)
    makesureButton.place(relx=0.8, rely=0.86)
    
    # บันทึกขนาดเดิมของปุ่ม
    appWindow.update()  # อัพเดทหน้าต่างเพื่อให้ได้ขนาดปุ่มที่ถูกต้อง
    makesureButton.original_width = makesureButton.winfo_width()
    makesureButton.original_height = makesureButton.winfo_height()
    
    makesureButton.bind("<Enter>", on_enter)
    makesureButton.bind("<Leave>", on_leave)
    UpdateTime()
    appWindow.mainloop()
#makeCheckingYourself("-", "-", "-", "-", "-", "-", "-",
                     #"-", "-", "-", "-", "-", "-", "-", 
                     #"-", "-", "-", "-", "-")
