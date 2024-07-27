import win32api
import os
import time

def print_file(file_path):
    try:
        current_directory = os.getcwd() # ใช้สำหรับอ้างอิงที่อยู่ปัจจุบันของไฟล์ python
        file_path = os.path.join(current_directory, file_path) # ดัึงที่อยู่ไฟล์ที่จะปริ้น
        
        win32api.ShellExecute(
            0,
            "print",
            file_path,
            None,
            ".",
            0
        )
        
        time.sleep(10)  # รอให้การพิมพ์เสร็จสิ้น (ปรับเวลาตามที่เหมาะสม)
        
        # ถ้าต้องการลบไฟล์หลังจากพิมพ์เสร็จ ให้เอา # ออกจากบรรทัดด้านล่าง
        # os.remove(file_path)
    
    except Exception as e:
        print(f"Error printing file: {e}")

# ตัวอย่างการใช้งาน
# ปรินเไฟล์ .docx
# print_file("documents/1110301373253_วีรภัทร.docx")
