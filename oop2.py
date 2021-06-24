
def Add(no1,no2):
    return no1 + no2;
    
def Sub(no1,no2):
    return no1 - no2
def main():
    print("Enter First Number")
    value1 = int(input())
    print("Enter Second Number")
    value2 = int(input())
    
    ret = Add(value1,value2)
    print("Addition is :",ret)
    
    ret = Sub(value1,value2)
    print("Subtraction is :",ret)
    
    
if __name__ == "__main__":
    main()