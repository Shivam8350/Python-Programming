
def Substraction(no1,no2):
    return no1 - no2
    
def main():
    print("Enter First Number")
    Value1 = int(input())
    
    print("Enter Second Number")
    Value2 = int(input())
    
    ret = Substraction(Value1,Value2)
    
    print("Substraction is",ret)
    
if __name__ == "__main__":
    main()