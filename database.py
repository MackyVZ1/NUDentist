import mysql.connector

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

# สร้างตารางเก็บข้อมูล
# Patient (เก็บข้อมูล)
# myCursor.execute("CREATE TABLE Patient(DN VARCHAR(6),thaiTitle VARCHAR(20),thaiName VARCHAR(75), thaiSurname VARCHAR(75), engTitle VARCHAR(7), engName VARCHAR(75), engSurname VARCHAR(75), ID bigint PRIMARY KEY, birthdate VARCHAR(12), age smallint, gender VARCHAR(5), status VARCHAR(20), job VARCHAR(30), address VARCHAR(140), phoneNum VARCHAR(11), emergencyName VARCHAR(150), relation VARCHAR(8), emergencyNum VARCHAR(11), emergencyAddress VARCHAR(140), cureType VARCHAR(35), cureName VARCHAR(40))")
# QueueInfo (เก็บข้อมูลชั่วคราวสำหรับนำไปเก็บในตาราง Patient)
# myCursor.execute("CREATE TABLE QueueInfo(Time VARCHAR(10) PRIMARY KEY, DN VARCHAR(6),thaiTitle VARCHAR(20),thaiName VARCHAR(75), thaiSurname VARCHAR(75), engTitle VARCHAR(7), engName VARCHAR(75), engSurname VARCHAR(75), ID bigint, birthdate VARCHAR(12), age smallint, gender VARCHAR(5), status VARCHAR(20), job VARCHAR(30), address VARCHAR(140), phoneNum VARCHAR(11), emergencyName VARCHAR(150), relation VARCHAR(8), emergencyNum VARCHAR(11), emergencyAddress VARCHAR(140))")
