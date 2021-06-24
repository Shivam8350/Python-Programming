# Defination of function
def Addition(no1,no2):
    ans = no1 + no2
    return ans

def main():
    print("Enter first number")
    value1= int(input())
    
    print("Enter second number")
    value2= int(input())
    
    ret = Addition(value1,value2)
    print("Addition of {} and {} is {}".format(value1,value2,ret))
    # printf("Addition of %d and %d is %d",value1,value2,ret);
    
if __name__ == "__main__":
    main()