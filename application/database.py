import mysql.connector

# เชื่อมต่อกับ database ที่สร้างไว้
db = mysql.connector.connect(
    host="sql12.freesqldatabase.com", # sql12.freesqldatabase.com
    database="sql12718944", # sql12718944
    user="sql12718944", # sql12718944
    password="1DYCQpAPGS", # 1DYCQpAPGS
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
# myCursor.execute("CREATE TABLE QueueInfo(Time VARCHAR(10) PRIMARY KEY, DN VARCHAR(6),thaiTitle VARCHAR(20),thaiName VARCHAR(75), thaiSurname VARCHAR(75), engTitle VARCHAR(7), engName VARCHAR(75), engSurname VARCHAR(75), ID bigint, birthdate VARCHAR(12), age smallint, gender VARCHAR(5), status VARCHAR(20), job VARCHAR(30), address VARCHAR(140), phoneNum VARCHAR(11), emergencyName VARCHAR(150), relation VARCHAR(8), emergencyNum VARCHAR(11), emergencyAddress VARCHAR(140), tempVar float, bloodtopVar smallint, bloodbottomVar smallint, hearrateVar smallint, checkbox1Var smallint, checkbox2Var smallint, checkbox3Var smallint, checkbox4Var smallint, checkbox5Var smallint, checkbox6Var smallint, checkbox7Var smallint, checkbox8Var smallint, checkbox9Var smallint, checkbox10Var smallint, checkbox11Var smallint, checkbox12Var smallint, checkbox13Var smallint, checkbox14Var smallint, checkbox15Var smallint, checkbox15inputVar VARCHAR(10), checkbox16Var smallint, checkbox17Var smallint, checkbox18Var smallint, checkbox19Var smallint, checkbox20Var smallint, checkbox21Var smallint, checkbox22Var smallint, checkbox23Var smallint, checkbox24Var smallint, checkbox25Var smallint, checkbox26Var smallint, checkbox27Var smallint, checkbox28Var smallint, checkbox29Var smallint, checkbox30Var smallint, checkbox30inputVar VARCHAR(2))")
