class Demo:
    x = 10
    y = 20
    
    def __init__(self):
        print("Inside Constructor")
        self.i = 30
        self.j = 40
        
    def __del__(self):
        print("Inside Destructor")
        
    def fun(self):
        print("Inside Fun")
        
def main():
    obj1 = Demo()
    obj2 = Demo()
    obj1.fun()
    obj2.fun()
    del obj1   # fun(obj1)   fun(1000)
    del obj2   # fun(obj2)   fun(2000)

if __name__ == "__main__":
    main()