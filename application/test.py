import tkinter as tk
from tkinter import ttk
import win32print

def get_printers():
    printers = []
    for printer in win32print.EnumPrinters(2):
        printers.append(printer[2])
    return printers

def select_printer():
    selected_printer = printer_combobox.get()
    result_label.config(text=f"เครื่องพิมพ์ที่เลือก: {selected_printer}")
    # ทำงานอื่นๆ กับเครื่องพิมพ์ที่เลือกตรงนี้

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("เลือกเครื่องพิมพ์")
root.geometry("300x150")

# สร้าง Combobox สำหรับเลือกเครื่องพิมพ์
printer_combobox = ttk.Combobox(root, values=get_printers())
printer_combobox.set("เลือกเครื่องพิมพ์")
printer_combobox.pack(pady=20)

# สร้างปุ่มยืนยัน
select_button = tk.Button(root, text="ยืนยัน", command=select_printer)
select_button.pack()

# สร้าง Label สำหรับแสดงผลลัพธ์
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()