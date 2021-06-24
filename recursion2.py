
i = 1    # Define the Variable

def fun():
    global i   #Declare the Variable
    print(i)
    i = i + 1
    fun()
    
def main():
    fun()
    
if __name__ == "__main__":
    main()