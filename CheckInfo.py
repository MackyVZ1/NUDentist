import tkinter as tk


from database import myCursor, db
from PIL import Image, ImageTk
from tkinter import ttk

# ฟังก์ชันเรียกตรวจสอบข้อมูล
def checkInfo(data):
    # ส่งข้อมูลเข้าฐานข้อมูล
    def prepare():
        def submit():
            # เพิ่มข้อมูลเลข DN
            newInfo[1] = dnVar.get()
            idList = [newInfo[8]] # เก็บ Id เป็น list เพื่อใช้ในบรรทัดที่ 24
            # เพิ่มข้อมูลเข้าฐานข้อมูลตาราง Patient
            forsql = "INSERT INTO Patient(DN, thaiTitle, thaiName, thaiSurname, engTitle, engName, engSurname, ID, birthdate, age, gender, status, job, address, phoneNum, emergencyName, relation, emergencyNum, emergencyAddress, cureType, cureName) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (newInfo[1], newInfo[2], newInfo[3], newInfo[4], newInfo[5],
                    newInfo[6], newInfo[7], newInfo[8], newInfo[9], newInfo[10],
                    newInfo[11], newInfo[12], newInfo[13], newInfo[14], newInfo[15],
                    newInfo[16], newInfo[17], newInfo[18], newInfo[19], cureWaysVar.get(), nuhospitalVar.get())
            myCursor.execute(forsql, values)
            # ลบข้อมูลชั่วคราวที่เก็บทิ้ง
            myCursor.execute("DELETE FROM QueueInfo WHERE ID = %s", idList)
            db.commit()
            dnWindow.destroy()
            appWindow.destroy()
        dnWindow = tk.Toplevel()
        dnWindow.geometry("400x200")
        dnWindow.resizable(False, False)
        dnWindow.config(bg="white")
        
        dnVar = tk.StringVar()
        dnLabel = tk.Label(dnWindow, text="กรอก DN", font=("FreesiaUPC", 18), bg="white")
        dnLabel.place(relx=0.05, rely=0.35)
        dnInput = tk.Entry(dnWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=5, textvariable=dnVar)
        dnInput.place(relx=0.25, rely=0.345)
        submitButton = tk.Button(dnWindow, text="ยืนยัน", font=("FreesiaUPC", 18), width=20, command=submit)
        submitButton.place(relx=0.3, rely=0.68)
        
            
    def on_select_cureways(event):
        selected_value_cureways = curewayCombobox.get() # ดึงค่ามาจาก title_combobox ที่มาจาก thai_title
        cureWaysVar.set(f"{selected_value_cureways}")
        if selected_value_cureways == "บัตรทอง":
            goldencardNUEntry.place(relx=0.365, rely=0.75)
            nuhospitalVar.set("(โรงพยาบาลมหาวิทยาลัยนเรศวร)")
        else:
            goldencardNUEntry.place_forget()
            nuhospitalVar.set("-")
            
    def on_enter(event):
        # ลดขนาดปุ่มลง 3%
        current_width = event.widget.winfo_width()
        current_height = event.widget.winfo_height()
        new_width = int(current_width * 0.97)
        new_height = int(current_height * 0.97)
        event.widget.config(width=new_width, height=new_height)
    def on_leave(event):
        # คืนขนาดปุ่มกลับเป็นขนาดเดิม
        original_width = event.widget.original_width
        original_height = event.widget.original_height
        event.widget.config(width=original_width, height=original_height)
   
    # นำ data มาเก็บไว้ใน list
    newInfo = []
    for info in data:
        newInfo.append(info)
    
    cureWays = ["ชำระเงินเอง", "ชำระเงินเอง/เบิกต้นสังกัด", "บัตรทอง", "ประกันสังคม", "เบิกได้(จ่ายตรง)"]
    
    appWindow = tk.Toplevel()
    appWindow.title("ตรวจสอบข้อมูล") # name an application
    appWindow.config(bg="white")
    ## set a resolution
    appWindow.geometry("1280x720")
    appWindow.resizable(False, False)
    
    image1 = Image.open("components/submitButton.png")
    submitImage = ImageTk.PhotoImage(image1)
    
    ## text that show on a screen
    label1 = tk.Label(appWindow, text="ตรวจสอบข้อมูล", font=("FreesiaUPC", 49, "bold"), bg="white")
    label1.place(relx=0.15, rely=0.1, anchor="center")
    
    # thai title
    thaititleVar = tk.StringVar()
    thaititleVar.set(newInfo[2]) 
    thaititleLabel = tk.Label(appWindow, text="คำนำหน้า", font=("FreesiaUPC", 18), bg="white")
    thaititleLabel.place(relx=0.07, rely=0.2)
    thaititleInput = tk.Entry(appWindow, textvariable=thaititleVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    thaititleInput.place(relx=0.135, rely=0.197, width=90, height=35)
    
    # thai name & surname
    thainameVar = tk.StringVar()
    thainameVar.set(newInfo[3])
    thaisurnameVar = tk.StringVar()
    thaisurnameVar.set(newInfo[4])
    thainameLabel = tk.Label(appWindow, text="ชื่อ", font=("FreesiaUPC", 18), bg="white")
    thainameLabel.place(relx=0.22, rely=0.2)
    thainameInput = tk.Entry(appWindow, textvariable=thainameVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4) # รับ input
    thainameInput.place(relx=0.25, rely=0.2, width=234, height=40)
    thaisurnameLabel = tk.Label(appWindow, text="นามสกุล", font=("FreesiaUPC", 18), bg="white")
    thaisurnameLabel.place(relx=0.44, rely=0.2)
    thaisurnameInput = tk.Entry(appWindow, textvariable=thaisurnameVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    thaisurnameInput.place(relx=0.5, rely=0.2, width=234, height=40)
    
    # id
    idVar = tk.StringVar()
    idVar.set(newInfo[8])
    idLabel = tk.Label(appWindow, text="เลขบัตรประชาชน", font=("FreesiaUPC", 18), bg="white")
    idLabel.place(relx=0.69, rely=0.2)
    idInput = tk.Entry(appWindow, textvariable=idVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    idInput.place(relx=0.79, rely=0.2, width=180, height=35)
    
    # english title
    engtitleVar = tk.StringVar()
    engtitleVar.set(newInfo[5])
    engtitleLabel = tk.Label(appWindow, text="Title", font=("FreesiaUPC", 18), bg="white")
    engtitleLabel.place(relx=0.07, rely=0.29)
    engtitleInput = tk.Entry(appWindow, textvariable=engtitleVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    engtitleInput.place(relx=0.11, rely=0.29, width=90, height=35)
    
    # english name & surname
    engnameVar = tk.StringVar()
    engnameVar.set(newInfo[6])
    engsurnameVar = tk.StringVar()
    engsurnameVar.set(newInfo[7])
    engnameLabel = tk.Label(appWindow, text="Name", font=("FreesiaUPC", 18), bg="white")
    engnameLabel.place(relx=0.195, rely=0.29)
    engnameInput = tk.Entry(appWindow, textvariable=engnameVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4) # รับ input
    engnameInput.place(relx=0.24, rely=0.293, width=240, height=35)
    engsurnameLabel = tk.Label(appWindow, text="Surname", font=("FreesiaUPC", 18), bg="white")
    engsurnameLabel.place(relx=0.45, rely=0.29)
    engsurnameInput = tk.Entry(appWindow, textvariable=engsurnameVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    engsurnameInput.place(relx=0.52, rely=0.293, width=240, height=35)
    
    # date
    dateVar = newInfo[9]
    dayVar = tk.StringVar() # นำมาใช้เก็บค่าและผูกค่ากับวันที่จากการใช้ entry
    dayVar.set(dateVar[:2])
    monthVar = tk.StringVar() # นำมาใช้เก็ยค่าและผูกค่ากับเดือนจากการใช้ entry
    monthVar.set(dateVar[3:5])
    yearVar = tk.StringVar() # นำมาใช้เก็บค่าและผูกค่ากับปีจากการใช้ entry
    yearVar.set(dateVar[6:])
    
    dateLabel = tk.Label(appWindow, text="วว/ดด/ปปปป", font=("FreesiaUPC", 18), bg="white")
    dateLabel.place(relx=0.72, rely=0.29)
    dayInput = tk.Entry(appWindow, textvariable=dayVar,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=2)
    dayInput.place(relx=0.805, rely=0.285)
    slash1 = tk.Label(appWindow, text="/", font=("FreesiaUPC", 28, "bold"), bg="white")
    slash1.place(relx=0.83, rely=0.275)

    monthInput = tk.Entry(appWindow, textvariable=monthVar,font=("FreesiaUPC", 18),  relief="sunken", borderwidth=4, width=2)
    monthInput.place(relx=0.845, rely=0.285)
    slash2 = tk.Label(appWindow, text="/", font=("FreesiaUPC", 28, "bold"), bg="white")
    slash2.place(relx=0.87, rely=0.275)
    
    yearInput = tk.Entry(appWindow, textvariable=yearVar,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=4,)
    yearInput.place(relx=0.885, rely=0.285)
    
    # gender
    genderVar = tk.StringVar()
    genderVar.set(newInfo[11])
    genderLabel = tk.Label(appWindow, text="เพศ", font=("FreesiaUPC", 18), bg="white")
    genderLabel.place(relx=0.07, rely=0.38)
    genderInput = tk.Entry(appWindow, textvariable=genderVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    genderInput.place(relx=0.11, rely=0.38, width=90, height=35)
    
    # status
    statusVar = tk.StringVar()
    statusVar.set(newInfo[12])
    statusLabel = tk.Label(appWindow, text="สถานภาพ",font=("FreesiaUPC", 18), bg="white")
    statusLabel.place(relx=0.195, rely=0.38)
    statusInput = tk.Entry(appWindow, textvariable=statusVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    statusInput.place(relx=0.265, rely=0.38, width=90, height=35)
    
    # phone number
    phonenumVar = tk.StringVar()
    phonenumVar.set(newInfo[15])
    phoneNumLabel = tk.Label(appWindow, text="โทรศัพท์มือถือ", font=("FreesiaUPC", 18), bg="white")
    phoneNumLabel.place(relx=0.35, rely=0.38)
    phonenumInput = tk.Entry(appWindow, textvariable=phonenumVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=20)
    phonenumInput.place(relx=0.445, rely=0.378)
    
    # job
    jobVar = tk.StringVar()
    jobVar.set(newInfo[13])
    jobLabel = tk.Label(appWindow, text="อาชีพ", font=("FreesiaUPC", 18), bg="white")
    jobInput = tk.Entry(appWindow, textvariable=jobVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=27)
    jobLabel.place(relx=0.64, rely=0.38)
    jobInput.place(relx=0.688, rely=0.378)
    
    # contact address
    contactaddressVar = tk.StringVar()
    contactaddressVar.set(newInfo[14])
    contactAdInfoLabel = tk.Label(appWindow, text="ที่อยู่ที่ติดต่อได้", font=("FreesiaUPC", 18), bg="white")
    contactAdInfoLabel.place(relx=0.07, rely=0.475)
    contactAdInfoInput = tk.Entry(appWindow, textvariable=contactaddressVar, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=87)
    contactAdInfoInput.place(relx=0.17, rely=0.47)
    
    # emergency contact
    emergencycontactVar = tk.StringVar()
    emergencycontactVar.set(newInfo[16])
    emergencyrelationVar = tk.StringVar()
    emergencyrelationVar.set(newInfo[17])
    emergencynumVar = tk.StringVar()
    emergencynumVar.set(newInfo[18])
    emergencyaddressVar = tk.StringVar()
    emergencyaddressVar.set(newInfo[19])
    emergencycontactLabel = tk.Label(appWindow, text="ชื่อ - สกุลผู้ที่ติดต่อได้ (กรณีฉุกเฉิน) ", font=("FreesiaUPC",18), bg="white")
    emergencycontactInput = tk.Entry(appWindow, textvariable=emergencycontactVar,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=30)
    emergencycontactLabel.place(relx=0.07, rely=0.56)
    emergencycontactInput.place(relx=0.28, rely=0.56)
    emergencyrelationLabel = tk.Label(appWindow, text="เกี่ยวข้องเป็น", font=("FreesiaUPC", 18), bg="white")
    emergencyrelationInput = tk.Entry(appWindow, textvariable=emergencyrelationVar,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=6)
    emergencyrelationLabel.place(relx=0.555, rely=0.56)
    emergencyrelationInput.place(relx=0.63, rely=0.56)
    emergencynumLabel = tk.Label(appWindow, text="โทรศัพท์มือถือ", font=("FreesiaUPC", 18), bg="white")
    emergencynumInput = tk.Entry(appWindow, textvariable=emergencynumVar,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=14)
    emergencynumLabel.place(relx=0.7, rely=0.56)
    emergencynumInput.place(relx=0.8, rely=0.56)
    emergencyaddressLabel = tk.Label(appWindow, text="ที่อยู่", font=("FreesiaUPC", 18), bg="white")
    emergencyaddressInput = tk.Entry(appWindow, textvariable=emergencyaddressVar,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=93)
    emergencyaddressLabel.place(relx=0.07, rely=0.65)
    emergencyaddressInput.place(relx=0.12, rely=0.65)
    
    # สิทธิการรักษา
    cureWaysVar = tk.StringVar()
    nuhospitalVar = tk.StringVar()
    goldencardNUEntry = tk.Entry(appWindow, textvariable=nuhospitalVar, font=("FreesiaUPC", 18), bg="white")
    curewayLabel = tk.Label(appWindow, text="สิทธิการรักษา", font=("FreesiaUPC", 18), bg="white")
    curewayCombobox = ttk.Combobox(appWindow, textvariable=cureWaysVar, font=("FreesiaUPC", 18), values=cureWays, state="readonly", )
    curewayCombobox.bind("<<ComboboxSelected>>", on_select_cureways)
    curewayLabel.place(relx=0.07, rely=0.75)
    curewayCombobox.place(relx=0.165, rely=0.75)
    # submit button
    submit_button = tk.Button(appWindow, text="ยืนยัน", font=("FreesiaUPC", 18), image=submitImage ,command=prepare, anchor="center",bg="white",border=0,)
    submit_button.place(relx=0.8, rely=0.83)
    
    # บันทึกขนาดเดิมของปุ่ม
    appWindow.update()  # อัพเดทหน้าต่างเพื่อให้ได้ขนาดปุ่มที่ถูกต้อง
    submit_button.original_width = submit_button.winfo_width()
    submit_button.original_height = submit_button.winfo_height()
    
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)
    appWindow.mainloop()