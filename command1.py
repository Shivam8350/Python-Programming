import sys

def Addition(no1,no2):
    return no1 + no2
    
def main():
    ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition is : ",ret)
    
if __name__ == "__main__":
    main()
    
    
    #Run Command-
# python command1.py 11 21