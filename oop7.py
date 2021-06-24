class Student:
    School = "Shivam"         #Class Variable
    
    def __init__(self,no1,no2,no3):
        self.m1 = no1                 #Instance Variable
        self.m2 = no2
        self.m3 = no3
        
    def Instanc_Total(self):           # Instance method
        print("Inside Instance method")
        return self.m1 + self.m2 + self.m3
        
    @classmethod                   #Decorator
    def Class_DisplaySchool(cls):       #class method
        print("School name is:",cls.School)
        
    @staticmethod              #Decorator
    def Static_Info():         #Static Method
        print("This Class Contains the information of school")
        
def main():
    Student.Class_DisplaySchool()  #Calling Class method
    obj1 = Student(50,80,70)        # object creation
    obj2 = Student(65,80,75)
    ret = obj1.Instanc_Total()      # Calling instance method
    print("Total Obtain Mark :",ret)
    Student.Static_Info()         #Calling Static Method

if __name__== "__main__":
    main()