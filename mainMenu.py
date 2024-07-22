import tkinter as tk

from database import db
from PIL import Image, ImageTk
from oldpatientMenu import oldPatientMenu
from newMenu import newpatientMenu

## ฟังก์ชันเข้าหน้าเมนู
def Menu():
    
    ## ฟังก์ชันปิดการเชื่อมต่อ database เมื่อทำการปิดแอป
    def closeApp():
        if db.is_connected():
            db.close()
        appWindow.destroy()
        
    ## ฟังก์ชันควบคุมการทำงานของ mouse pointer ตอนเอาเมาส์ชี้ที่ปุ่ม
    def on_enter(event):
        # ลดขนาดปุ่มลง 3%
        current_width = event.widget.winfo_width()
        current_height = event.widget.winfo_height()
        new_width = int(current_width * 0.97)
        new_height = int(current_height * 0.97)
        event.widget.config(width=new_width, height=new_height)
        
    ## ฟังก์ชันควบคุมการทำงานของ mouse pointer ตอนเอาเมาส์ออกจากปุ่ม
    def on_leave(event):
        # คืนขนาดปุ่มกลับเป็นขนาดเดิม
        original_width = event.widget.original_width
        original_height = event.widget.original_height
        event.widget.config(width=original_width, height=original_height)

    appWindow = tk.Tk() # create an application
    appWindow.title("โรงพยาบาลทันตกรรม มหาวิทยาลัยนเรศวร") # name an application

    ## set a resolution
    appWindow.geometry("1280x720")
    appWindow.resizable(False, False) # fixed size
    
    ## โหลดรูปภาพ
    icon = Image.open("components/dentlogo.png") # โลโก้คณะ
    image1 = Image.open("components/mainmenu_background.png") # พื้นหลัง
    image2 = Image.open("components/oldpatientButton.png") # ปุ่มผู้ป่วยที่มีประวัติแล้ว
    image3 = Image.open("components/newpatientButton.png") # ปุ่มผู้ป่วยใหม่ 
    Icon = ImageTk.PhotoImage(icon) # เอาตัวแปร icon มาทำเป็นรูปสำหรับ tkinter
    backgroundImage = ImageTk.PhotoImage(image1) # เอาตัวแปร image1 มาทำเป็นรูปสำหรับ tkinter
    oldpatientImage = ImageTk.PhotoImage(image2) # เอาตัวแปร image2 มาทำเป็นรูปสำหรับ tkinter
    newpatientImage = ImageTk.PhotoImage(image3) # เอาตัวแปร image3 มาทำเป็นรูปสำหรับ tkinter
    
    ## set a window logo with .ico format
    appWindow.iconphoto(True,Icon)
    
    ## set a background
    backgrounLabel = tk.Label(appWindow, image=backgroundImage)
    backgrounLabel.pack()

    ## label on screen
    label1 = tk.Label(appWindow, text="โรงพยาบาลทันตกรรม คณะทันตแพทยศาสตร์ มหาวิทยาลัยนเรศวร", font=("FreesiaUPC", 28, "bold"), bg="white")
    label2 = tk.Label(appWindow, text="กรุณาเลือกทำการ", font=("FreesiaUPC", 28, "bold"), bg="white")
    label1.place(relx=0.52, rely=0.08, anchor="center")
    label2.place(relx=0.5, rely=0.15, anchor="center")

    ## ปุ่มกด
    # ปุ่มกดเข้าหน้า "ผู้ป่วยใหม่"
    newpatient_button = tk.Button(appWindow, 
                    image=newpatientImage,
                    bg="white",
                    border=0,
                    anchor="center",
                    command=newpatientMenu)
    # ปุ่มกดเข้าหน้า "ผู้ป่วยที่มีประวัติแล้ว"
    oldpatient_button = tk.Button(appWindow, 
                    image=oldpatientImage,
                    bg="white",
                    border=0,
                    anchor="center",
                    command=oldPatientMenu)
    # วางตำแหน่งของปุ่มกด
    newpatient_button.place(relx=0.1, rely=0.25)
    oldpatient_button.place(relx=0.53, rely=0.25)
    
    # บันทึกขนาดเดิมของปุ่ม
    appWindow.update()  # อัพเดทหน้าต่างเพื่อให้ได้ขนาดปุ่มที่ถูกต้อง
    newpatient_button.original_width = newpatient_button.winfo_width()
    newpatient_button.original_height = newpatient_button.winfo_height()
    oldpatient_button.original_width = oldpatient_button.winfo_width()
    oldpatient_button.original_height = oldpatient_button.winfo_height()
    
    newpatient_button.bind("<Enter>", on_enter)
    newpatient_button.bind("<Leave>", on_leave)
    oldpatient_button.bind("<Enter>", on_enter)
    oldpatient_button.bind("<Leave>", on_leave)
    
    # ทำฟังก์ชัน closeApp เมื่อปิดโปรแกรม
    appWindow.protocol("WM_DELETE_WINDOW", closeApp)
    appWindow.mainloop() # show a screen on a display

# เรียกฟังก์ชันเอาไว้ทดสอบโปรแกรม
#Menu()         