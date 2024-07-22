import win32print
import win32api
import os
import time

def print_file(file_path):
    # ดึงข้อมูลเครื่องปริ้นที่ใช้เป็นเครื่องตั้งต้น
    printer_name = win32print.GetDefaultPrinter()
    
    # สั่งพิมพ์
    win32api.ShellExecute(
        0,
        "print",
        file_path,
        f'/d:"{printer_name}"',
        ".",
        0
    )
    
    # รอให้การพิมพ์เสร็จสิ้น (อาจต้องปรับเวลาตามความเหมาะสม)
    time.sleep(10)
    
    # ถ้าต้องการลบไฟล์หลังจากพิมพ์เสร็จ ให้เอา # ออกจากบรรทัดด้านล่าง
    os.remove(file_path)

# ตัวอย่างการใช้งาน
# ปรินเไฟล์ .docx
#print_pdf("1110301373253_วีรภัทร_ข้อมูลส่วนตัว.docx")