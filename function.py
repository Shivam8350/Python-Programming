# Types of function definations

# Accepts nothing return nothing
def fun():
    print("Inside fun")
    
# Accepts parameter and return nothing
def gun(value):
    print("Inside gun",value)
    
# Accepts parameter  and return the value
def sun(value):
    value = value + 1
    print("Inside sun")
    return value

def mun():
    pass

def Outer():
    print("Inside Outer")
    def Inner():
        print("Inside Inner")
    Inner()

def main():
    fun()
    gun(11)
    ret = sun(10)
    print(ret)
    mun()
    Outer()
    
if __name__ == "__main__":
    main()