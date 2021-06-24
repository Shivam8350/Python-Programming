#name = lambda parameter:body


#named function
def Addition(no1,no2):
    return no1 + no2

#Lambda Function
Sum = lambda no1,no2 : no1 + no2

def fun(name):
    ret = name(10,20)
    print("Value from fun is : ",ret)
    
def main():
    print("Enter First Number")
    value1 = int(input())
    
    print("Enter Second Number")
    value2 = int(input())
    
    ret = Addition(value1,value2)
    print("Addition is : ",ret)

    ret = Sum(value1,value2)  # ret = value1 + value2
    
    print("Addition with lambda is :",ret)
    fun(sum)

if __name__ == "__main__":
    main()