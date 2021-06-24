class Demo:
    def Add(self,no1,no2):
        return no1 + no2
        
    def Add(self,no1,no2,no3):  #method overloading is not possible in python
        return no1 + no2 + no3
        
    
def main():

    obj = Demo()
    ret = obj.Add(10,20,30)
    print(ret)

if __name__ == "__main__":
    main()