def AdditionF(data):
    sum = 0
    for i in range(len(data)): sum = sum + data[i]
    return sum
    
def AdditionW(data):
    sum = 0
    i = 0
    while i< len(data):
        sum = sum + data[i]
        i = i + 1
    return sum
    
sum = 0
i = 0
def AdditionR(data):
    global sum
    global i
    if i < len(data):
        sum = sum + data[i]
        i = i + 1
        AdditionR(data)
    return sum
    
def main():
    arr = []
    size = int(input("Enter number of elements"))
    for i in range(size):arr.append(int(input()))
    
    print("Data is :",arr)
    
    print("Addition is",AdditionF(arr))
    print("Addition is",AdditionW(arr))
    print("Addition is",AdditionR(arr))
if __name__ == "__main__":
    main()