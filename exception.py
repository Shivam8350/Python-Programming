
def main():
    print("Enter first number")
    value1= int(input())
    
    print("Enter second number")
    value2= int(input())
    
    try:
        print("Inside try")
        ans = value1 / value2
    
    except Exception as eobj:
        print("Inside Except")
        print("Exception occur",eobj)
        
    else:
        print("Inside Else")
        print("Division is :",ans)
        
    finally:
        print("Inside Finally")
        print("Deallocate all the resources")
    
if __name__ =="__main__":
	main()