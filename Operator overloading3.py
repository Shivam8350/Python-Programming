class Student:
    def __init__(self,str,a,b,c):
        self.name = str
        self.m1 = a
        self.m2 = b
        self.m3 = c
 
    def __eq__(self,other):
        return ((self.m1==other.m1) and (self.m2==other.m2) and (self.m3==other.m3))
    
        
def main():
    obj1 = Student("Shivam",70,91,80)
    obj2 = Student("Shubham",78,81,89)
    
    if obj1 == obj2:
        print("Both the Student are Same")
    else:
        print("Both the Student are Different")
        

if __name__ == "__main__":
    main()