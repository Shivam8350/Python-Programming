#Inbuilt Function From Module
def Substraction(no1,no2):     
    return no1 - no2
    
def SubDecorator(fun_name):    
    def Updator(a,b):          
        if a < b:  #First parameter is small
            temp = a
            #a = b
            #b = temp
            a,b = b,a
        return fun_name(a,b)
        
    return Updator;
       
def main():                   
    Sub = SubDecorator(Substraction)  
    
    print("Enter First Number")
    Value1 = int(input())
    
    print("Enter Second Number")
    Value2 = int(input())
    
    ret = Sub(Value1,Value2)
    
    print("Substraction is",ret)
    
if __name__ == "__main__":
    main()                    