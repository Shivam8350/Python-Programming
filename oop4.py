
class Arithmatic:                # Class Defination
    value = 111                  #class variable
    
    # Self Means Pointed to our own object
    
    def __init__(self,i,j):      # Class Constructor
        print("Inside Constructor")
        self.no1 = i             # Class Instance Variable
        self.no2 = j             # Instance Variable

    def Add(self):                   #Instance method
        return self.no1 + self.no2
        
    def Sub(self):                   #Instance method
        return self.no1 - self.no2
def main():
    print("value is:",Arithmatic.value)

    obj1 = Arithmatic(11,21)  #__init__(obj1,11,21)
    obj2 = Arithmatic(69,66)  #__init__(obj2,69,66)
    
    ret = obj1.Add()          # ret = Add(obj1)
    print("Addition is:",ret)
    ret = obj1.Sub()          # ret = sub(obj1)
    print("Subtraction is:",ret)
    
    ret = obj2.Add()           # ret = Add(obj2)
    print("Addition is:",ret)
    ret = obj2.Sub()           # ret = Sub(obj2)
    print("Subtraction is:",ret)



if __name__ == "__main__":
    main()