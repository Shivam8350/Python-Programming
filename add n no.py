
#Accept the n Number from user and Addition of n Numbers 

def addition(LIST):
    sum = 0
    for i in range(len(LIST)):
        sum = sum + LIST[i]
    return sum

def main():
    arr = []
    print("Enter the number of elements")
    size = int(input())
    
    for i in range(size):
        print("Enter the element no :",i + 1)
        value = int(input())
        arr.append(value)
        
    print("Accepted data is : " ,arr)
    
    ret = addition(arr)
    
    print("Addition of all elements is:",ret)
    
if __name__ == "__main__":
    main()
    