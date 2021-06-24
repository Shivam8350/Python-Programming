#Inbuilt Function From Module
def Substraction(no1,no2):
    return no1 - no2
    
def SubDecorator(fun_name):
    return fun_name(10,5)
    
def main():
    
    ret = SubDecorator(Substraction) #Substraction is Function as a object
    
    print("Substraction is",ret)
    
if __name__ == "__main__":
    main()