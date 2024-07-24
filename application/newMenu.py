import tkinter as tk
import datetime
import Checkyourself as c # สำหรับใช้ทำใบคัดกรอง


from PIL import Image, ImageTk
from Printer import print_file
from database import myCursor, db
from NewPatientInfo import newPatient_info
from tkinter import ttk
from temporaryInfo import temp_info # สำหรับใช้ทำใบประวัติ

def newpatientMenu():
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
    # คำนำหน้าภาษาไทย
    def on_select_thai_title(event):
        selected_value_thai_title = thai_title_combobox.get() # ดึงค่ามาจาก title_combobox ที่มาจาก thai_title
        update_value_thai_title.set(f"{selected_value_thai_title}")
        if selected_value_thai_title == "อื่น ๆ":
            thai_title_combobox.config(state="normal")
            update_value_thai_title.set(selected_value_thai_title)
    # คำนำหน้า eng
    def on_select_eng_title(event):
        selected_value_eng_title = eng_title_combobox.get()
        update_value_eng_title.set(f"{selected_value_eng_title}")
    
    # เพศ    
    def on_select_gender(event):
        selected_value_gender = gender_combobox.get()
        update_value_gender.set(f"{selected_value_gender}")
        
    # สถานภาพ
    def on_select_status(event):
        selected_value_status = status_combobox.get()
        update_value_status.set(f"{selected_value_status}")
        
    # อัพเดทเวลา
    def UpdateTime():
        now = datetime.datetime.now()
        buddhistYear = now.year + 543
        thai_month = month_thai(now.month)
        date = f"{now.day} {thai_month} {buddhistYear}"
        time = f"{now.strftime('%H:%M:%S')}"     
        dateShow.config(text=date)
        timeShow.config(text=time)
            
        appWindow.after(1000, UpdateTime)
        
    # เดือนไทย
    def month_thai(month_num):
        months = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.",
                  "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
        return months[month_num - 1]
    
    # คำนวณอายุ
    def calculate_age(day_var, month_var, year_var):
        # กรณีขำวันเกิดไม่ได้ (มีแต่ข้อมูลปี)
        if day_var == "-" and month_var == "-":
            day = 1
            month = 1
            year_thai = int(year_var)
            year = year_thai - 543 # ค.ศ เป็น พ.ศ
            birthdate = datetime.date(year, month, day)
            today = datetime.date.today()
            age = today.year - birthdate.year
            return int(age)
        # รู้วันเกิดตัวเอง
        else:
            day = int(day_var)
            month = int(month_var)
            year_thai = int(year_var)
            year = year_thai - 543 # ค.ศ เป็น พ.ศ
            birthdate = datetime.date(year, month, day)
            today = datetime.date.today()
            age = today.year - birthdate.year
            return int(age)
    
    
    # ปรับรูปแบบเบอร์โทรศัพท์ xxx-xxxxxxx
    def phonenumFormat(phoneNum):
        newphoneNum = phoneNum[:3] + "-" + phoneNum[3:]
        return newphoneNum
    
    # ลิมิต ID
    def limitID(event):
        if len(event.widget.get()) == 13:
            event.widget.tk_focusNext().focus()
    # ลิมิตค่าวัน/เดือน/ปี
    def limitDay(event):
        if len(event.widget.get()) == 2 or event.widget.get() == "-":
            event.widget.tk_focusNext().focus()
    def limitMonth(event):
        if len(event.widget.get()) == 2 or event.widget.get() == "-":
            event.widget.tk_focusNext().focus()
    def limitYear(event):
        if len(event.widget.get()) == 4:
            event.widget.tk_focusNext().focus()
    
    # ลิมิตค่าของเบอร์โทรศัพท์
    def limitPhonenum(event):
        if len(event.widget.get()) == 10:
            event.widget.tk_focusNext().focus()         
    # กดส่งข้อมูลทั้งหมดที่ผู้ใช้กรอกเข้ามา
    def submit():
        # เช็คว่ากรอกข้อมูลครบทุกช่องมั้ย
        if(update_value_thai_title.get() and thai_name_input.get() and thai_surname_input.get() and id_input.get() and
           update_value_eng_title.get() and eng_name_input.get() and eng_surname_input.get() and day_input.get() and month_input.get() and
           year_input.get() and update_value_gender.get() and update_value_status.get() and phoneNum_Input.get()
           and contactAdInfo_Input.get() and emergency_contact_Input.get() and
           emergency_address_Input.get() and emergency_num_Input.get()):
            # คำนำหน้า/ชื่อ/นามสกุลภาษาไทย
            Patient_register.setThai_title(update_value_thai_title.get())
            Patient_register.setThai_name(thai_name_input.get())
            Patient_register.setThai_surname(thai_surname_input.get())
            # บัตร/เลขบัตร
            Patient_register.setID(id_input.get())
            # คำนำหน้า/ชื่อ/นามสกุลภาษาอังกฤษ
            Patient_register.setEng_title(update_value_eng_title.get())
            Patient_register.setEng_name(eng_name_input.get())
            Patient_register.setEng_surname(eng_surname_input.get())
            # วว/ดด/ปปปป และ อายุ
            Patient_register.setBirthdate(day_var.get(), month_var.get(), year_var.get())
            Patient_register.setAge(calculate_age(day_var.get(), month_var.get(), year_var.get()))
            # เพศ / สถานภาพ
            Patient_register.setGender(update_value_gender.get())
            Patient_register.setStatus(update_value_status.get())
            # เบอร์ติดต่อ
            Patient_register.setPhoneNum(phonenumFormat(phoneNum_Input.get()))
            # อาชีพ
            Patient_register.setJob(job_var.get())
            # ที่อยู่ที่ติดต่อได้ / เบอร์บ้าน, เบอร์ทำงาน
            Patient_register.setAddress(contactAdInfo_Input.get())
            # ผู้ติดต่อฉุกเฉิน, ความเกี่ยวข้อง, ที่อยู่, เบอร์
            Patient_register.setEmergencyName(emergency_contact_Input.get())
            Patient_register.setRelation(emergency_relation_Input.get())
            Patient_register.setEmergencyAddress(emergency_address_Input.get())
            Patient_register.setEmergencyNum(phonenumFormat(emergency_num_Input.get()))
            # แสดงข้อมูล
            Patient_register.showInfo() 
            # นำข้อมูลไปทำใบคัดกรอง
            appWindow.destroy()
            c.makeCheckingYourself(None, Patient_register.thai_title, Patient_register.thai_name, Patient_register.thai_surname,
                                   Patient_register.eng_title, Patient_register.eng_name, Patient_register.eng_surname, Patient_register.id,
                                   Patient_register.birthdate, Patient_register.age, Patient_register.gender, Patient_register.status, Patient_register.job,
                                   Patient_register.address, Patient_register.phone_num, Patient_register.emergency_name, Patient_register.relation,
                                   Patient_register.emergency_num, Patient_register.emergency_address)
        else:
            warning_show()
    
    
    # คำเตือนเมื่อกรอกข้อมูลไม่ครบ
    def warning_show():
        warning_screen = tk.Toplevel()
        warning_screen.title("คำเตือน")
        warning_screen.geometry("300x110")
        warning_screen.resizable(False, False)
        warning_label = tk.Label(warning_screen, text="กรอกข้อมูลให้ถูกต้อง", font=("FreesiaUPC", 18), anchor="center").pack()
        ok_button = tk.Button(warning_screen, text="OK", font=("FreesiaUPC", 18), anchor="center", width=5, command=warning_screen.destroy).pack(padx=10, pady=10)
    
    
    ### ------------- Declaration ------------------------ 
    Patient_register = newPatient_info() # สร้างชุดข้อมูลคนไข้
    eng_title = ["Mr.", "Miss", "Mrs.", "Master", "Other"]
    thai_title = ["ด.ช.", "ด.ญ.", "นาย", "น.ส.", "นาง", "อื่น ๆ"]
    gender = ["ชาย", "หญิง"]
    status = ["โสด", "สมรส", "หย่า", "หม้าย", "แยกกันอยู่"]
    ### ------------- Application Design -----------------
    appWindow = tk.Toplevel() # create an application
    appWindow.title("ลงทะเบียนผู้ป่วยใหม่") # name an application
    appWindow.config(bg="white")
    ## set a resolution
    appWindow.geometry("1280x720")
    appWindow.resizable(False, False)
    
    image1 = Image.open("components/submitButton.png")
    image2 = Image.open("components/newpatient_background.png")
    submitImage = ImageTk.PhotoImage(image1)
    header = ImageTk.PhotoImage(image2)
    
    headerLabel = tk.Label(appWindow, image=header).pack()
    
    ## text that show on a screen
    dateShow = tk.Label(appWindow, font=("FreesiaUPC", 18), bg="#E7D3EE")
    timeShow = tk.Label(appWindow, font=("FreesiaUPC", 18), bg="#E7D3EE")
    label1 = tk.Label(appWindow, text="โรงพยาบาลทันตกรรม คณะทันตแพทยศาสตร์ มหาวิทยาลัยนเรศวร", font=("FreesiaUPC", 20, "bold"), bg="#E7D3EE")
    label2 = tk.Label(appWindow, text="ใบคำร้องขอมีเวชระเบียนผู้ป่วยใหม่", font=("FreesiaUPC", 20, "bold"), bg="#E7D3EE")
    label1.place(relx=0.5, rely=0.07, anchor="center")
    label2.place(relx=0.5, rely=0.13, anchor="center")
    dateShow.place(relx=0.89, rely=0.05)
    timeShow.place(relx=0.9, rely=0.1)
    
    ## thai title 
    thai_title_label = tk.Label(appWindow, text="คำนำหน้า", font=("FreesiaUPC", 18), bg="white")
    thai_title_label.place(relx=0.07, rely=0.2)
    update_value_thai_title = tk.StringVar() # ผูกกับ combobox เผื่อโชว์สิ่งทื่เลือก
    thai_title_combobox = ttk.Combobox(appWindow, textvariable=update_value_thai_title, font=("FreesiaUPC", 18), values=thai_title, state="readonly")
    thai_title_combobox.bind("<<ComboboxSelected>>", on_select_thai_title)
    thai_title_combobox.place(relx=0.135, rely=0.197, width=90, height=35)
    
    ## thai name & surname
    thai_name_label = tk.Label(appWindow, text="ชื่อ", font=("FreesiaUPC", 18), bg="white")
    thai_name_label.place(relx=0.22, rely=0.2)
    thai_name_input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4) # รับ input
    thai_name_input.place(relx=0.25, rely=0.2, width=234, height=40)
    thai_surname_label = tk.Label(appWindow, text="นามสกุล", font=("FreesiaUPC", 18), bg="white")
    thai_surname_label.place(relx=0.44, rely=0.2)
    thai_surname_input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    thai_surname_input.place(relx=0.5, rely=0.2, width=234, height=40)
    
    ## id
    id_label = tk.Label(appWindow, text="เลขบัตรประชาชน", font=("FreesiaUPC", 18), bg="white")
    id_label.place(relx=0.69, rely=0.2)
    id_input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    id_input.place(relx=0.79, rely=0.2, width=180, height=35)
    id_input.bind("<KeyRelease>", limitID)
    ## english title
    eng_title_label = tk.Label(appWindow, text="Title", font=("FreesiaUPC", 18), bg="white")
    eng_title_label.place(relx=0.07, rely=0.29)
    update_value_eng_title = tk.StringVar() # ผูกกับ combobox เผื่อโชว์สิ่งทื่เลือก
    eng_title_combobox = ttk.Combobox(appWindow, textvariable=update_value_eng_title, font=("FreesiaUPC", 18), values=eng_title, state="readonly")
    eng_title_combobox.bind("<<ComboboxSelected>>", on_select_eng_title)
    eng_title_combobox.place(relx=0.11, rely=0.29, width=90, height=35)
    
    ## english name & surname
    eng_name_label = tk.Label(appWindow, text="Name", font=("FreesiaUPC", 18), bg="white")
    eng_name_label.place(relx=0.195, rely=0.29)
    eng_name_input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4) # รับ input
    eng_name_input.place(relx=0.24, rely=0.293, width=240, height=35)
    eng_surname_label = tk.Label(appWindow, text="Surname", font=("FreesiaUPC", 18), bg="white")
    eng_surname_label.place(relx=0.45, rely=0.29)
    eng_surname_input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4)
    eng_surname_input.place(relx=0.52, rely=0.293, width=240, height=35)
    
    ## date
    day_var = tk.StringVar() # นำมาใช้เก็บค่าและผูกค่ากับวันที่จากการใช้ entry
    month_var = tk.StringVar() # นำมาใช้เก็ยค่าและผูกค่ากับเดือนจากการใช้ entry
    year_var = tk.StringVar() # นำมาใช้เก็บค่าและผูกค่ากับปีจากการใช้ entry
    day_var.trace("w", limitDay)
    month_var.trace("w", limitMonth)
    year_var.trace("w", limitYear)
    date_label = tk.Label(appWindow, text="วว/ดด/ปปปป", font=("FreesiaUPC", 18), bg="white")
    date_label.place(relx=0.72, rely=0.29)
    day_input = tk.Entry(appWindow, textvariable=day_var,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=2)
    day_input.place(relx=0.805, rely=0.285)
    slash1 = tk.Label(appWindow, text="/", font=("FreesiaUPC", 28, "bold"), bg="white")
    slash1.place(relx=0.83, rely=0.275)

    month_input = tk.Entry(appWindow, textvariable=month_var,font=("FreesiaUPC", 18),  relief="sunken", borderwidth=4, width=2)
    month_input.place(relx=0.845, rely=0.285)
    slash2 = tk.Label(appWindow, text="/", font=("FreesiaUPC", 28, "bold"), bg="white")
    slash2.place(relx=0.87, rely=0.275)
    
    year_input = tk.Entry(appWindow, textvariable=year_var,font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=4,)
    year_input.place(relx=0.885, rely=0.285)
    
    day_input.bind("<KeyRelease>", limitDay)
    month_input.bind("<KeyRelease>", limitMonth)
    year_input.bind("<KeyRelease>", limitYear)
    
    ## gender
    gender_label = tk.Label(appWindow, text="เพศ", font=("FreesiaUPC", 18), bg="white")
    gender_label.place(relx=0.07, rely=0.38)
    update_value_gender = tk.StringVar()
    gender_combobox = ttk.Combobox(appWindow, textvariable=update_value_gender, font=("FreesiaUPC", 18), values=gender, state="readonly")
    gender_combobox.bind("<<ComboboxSelected>>", on_select_gender)
    gender_combobox.place(relx=0.11, rely=0.38, width=90, height=35)
    
    ## status
    status_label = tk.Label(appWindow, text="สถานภาพ",font=("FreesiaUPC", 18), bg="white")
    status_label.place(relx=0.195, rely=0.38)
    update_value_status = tk.StringVar()
    status_combobox = ttk.Combobox(appWindow, textvariable=update_value_status, font=("FreesiaUPC", 18), values=status, state="readonly")
    status_combobox.bind("<<ComboboxSelected>>", on_select_status)
    status_combobox.place(relx=0.265, rely=0.38, width=90, height=35)
    
    ## phone number
    phoneNum_label = tk.Label(appWindow, text="โทรศัพท์มือถือ", font=("FreesiaUPC", 18), bg="white")
    phoneNum_label.place(relx=0.35, rely=0.38)
    phoneNum_Input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=20)
    phoneNum_Input.place(relx=0.445, rely=0.378)
    phoneNum_Input.bind("<KeyRelease>", limitPhonenum)
    
    ## job
    job_var = tk.StringVar()
    job_label = tk.Label(appWindow, text="อาชีพ", font=("FreesiaUPC", 18), bg="white")
    job_input = tk.Entry(appWindow, textvariable=job_var, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=27)
    job_label.place(relx=0.64, rely=0.38)
    job_input.place(relx=0.688, rely=0.378)
    
    ## contact address
    contactAdInfo_label = tk.Label(appWindow, text="ที่อยู่ที่ติดต่อได้", font=("FreesiaUPC", 18), bg="white")
    contactAdInfo_label.place(relx=0.07, rely=0.475)
    contactAdInfo_Input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=87)
    contactAdInfo_Input.place(relx=0.17, rely=0.47)
    
    
    ## emergency contact
    emergency_contact_label = tk.Label(appWindow, text="ชื่อ - สกุลผู้ที่ติดต่อได้ (กรณีฉุกเฉิน) ", font=("FreesiaUPC",18), bg="white")
    emergency_contact_Input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=30)
    emergency_contact_label.place(relx=0.07, rely=0.56)
    emergency_contact_Input.place(relx=0.28, rely=0.56)
    emergency_relation_label = tk.Label(appWindow, text="เกี่ยวข้องเป็น", font=("FreesiaUPC", 18), bg="white")
    emergency_relation_Input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=6)
    emergency_relation_label.place(relx=0.555, rely=0.56)
    emergency_relation_Input.place(relx=0.63, rely=0.56)
    emergency_num_label = tk.Label(appWindow, text="โทรศัพท์มือถือ", font=("FreesiaUPC", 18), bg="white")
    emergency_num_Input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=14)
    emergency_num_label.place(relx=0.7, rely=0.56)
    emergency_num_Input.place(relx=0.8, rely=0.56)
    emergency_address_label = tk.Label(appWindow, text="ที่อยู่", font=("FreesiaUPC", 18), bg="white")
    emergency_address_Input = tk.Entry(appWindow, font=("FreesiaUPC", 18), relief="sunken", borderwidth=4, width=93)
    emergency_address_label.place(relx=0.07, rely=0.65)
    emergency_address_Input.place(relx=0.12, rely=0.65)
    emergency_num_Input.bind("<KeyRelease>", limitPhonenum)
    
    ## submit button
    submit_button = tk.Button(appWindow, text="ยืนยัน", font=("FreesiaUPC", 18), image=submitImage ,command=submit, anchor="center",bg="white",border=0,)
    submit_button.place(relx=0.8, rely=0.83)
    
    ## บันทึกขนาดเดิมของปุ่ม
    appWindow.update()  # อัพเดทหน้าต่างเพื่อให้ได้ขนาดปุ่มที่ถูกต้อง
    submit_button.original_width = submit_button.winfo_width()
    submit_button.original_height = submit_button.winfo_height()
    
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)
    

    UpdateTime()
    appWindow.mainloop()