class newPatient_info:
    ### set default each parameter to "None"
    def __init__(self, DN = None, thai_title = None, thai_name = None, thai_surname = None, eng_title = None, eng_name = None, eng_surname = None, id = None,
                birthdate = None,  age = None, gender = None, status = None, address = None, phone_num = None, job = None,
                emergency_name = None, relation = None, emergency_num = None, emergency_address = None):
        self.DN = DN
        self.thai_title = thai_title
        self.thai_name = thai_name
        self.thai_surname = thai_surname
        self.eng_title = eng_title
        self.eng_name =  eng_name
        self.eng_surname = eng_surname
        self.id = id
        self.birthdate = birthdate
        self.age = age
        self.gender = gender
        self.status = status
        self.address = address
        self.job = job
        self.phone_num = phone_num
        self.emergency_name = emergency_name
        self.relation = relation
        self.emergency_num = emergency_num
        self.emergency_address = emergency_address
    ### ---------------------------------------------
        
    ### ---------- get an input to set a variable ---------------   
    def setDN(self, dn):
        self.DN = dn
    
    def setThai_title(self, title):
        self.thai_title = title
        
    def setThai_name(self, name):
        self.thai_name = name
        
    def setThai_surname(self, surname):
        self.thai_surname = surname
        
    def setEng_title(self, title):
        self.eng_title = title
        
    def setEng_name(self, name):
        self.eng_name = name
        
    def setEng_surname(self, surname):
        self.eng_surname = surname
        
    def setID(self, id):
        self.id = id
            
    def setBirthdate(self, day, month, year):
        self.birthdate = f"{day}/{month}/{year}"
        
    def setAge(self, age):
        self.age = age
    
    def setGender(self, gender):
        self.gender = gender
        
    def setStatus(self, status):
        self.status = status
    
    def setPhoneNum(self, phone_num):
        self.phone_num = phone_num
    
    def setJob(self, job):
        self.job = job
    
    def setAddress(self, address):
        self.address = address
    
    def setEmergencyName(self, name):
        self.emergency_name = name
    
    def setRelation(self, relation):
        self.relation = relation
    
    def setEmergencyNum(self, emergency_num):
        self.emergency_num = emergency_num
        
    def setEmergencyAddress(self, address):
        self.emergency_address = address
        
    def showInfo(self):
        print(f"DN :{self.DN}")
        print(f"{self.thai_title}{self.thai_name} {self.thai_surname}")
        print(f"{self.eng_title}{self.eng_name} {self.eng_surname}")
        print(f"ID : {self.id}")
        print(f"วันเกิด : {self.birthdate} อายุ : {self.age} ปี")
        print(f"เพศ : {self.gender} สถานภาพ : {self.status}")
        print(f"อาชีพ : {self.job}")
        print(f"โทรศัพท์มือถือ : {self.phone_num}")
        print(f"ที่อยู่ที่ติดต่อได้ : {self.address}")
        print(f"ชื่อ - สกุลผู้ที่ติดต่อได้(กรณีฉุกเฉิน) : {self.emergency_name} เกี่ยวข้องเป็น : {self.relation}")
        print(f"ที่อยู่ : {self.emergency_address}")
    ### ------------------------------------------------
         
        
    