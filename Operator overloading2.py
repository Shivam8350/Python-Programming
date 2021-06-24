class Student:
    def __init__(self,str,a,b,c):
        self.name = str
        self.m1 = a
        self.m2 = b
        self.m3 = c
 
    def __eq__(self,other):
        if self.m1==other.m1 and self.m2==other.m2 and self.m3==other.m3:
            return True
        else:
            return False
            
def main():
    obj1 = Student("Shivam",80,89,60)
    obj2 = Student("Shubham",80,89,60)
    
    if obj1 == obj2:
        print("Both the Student are Same")
    else:
        print("Both the Student are Different")

if __name__ == "__main__":
    main()