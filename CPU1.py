import os
import time

def Square(no):
    return no * no
    
def serialprocessing():
    start = time.time()
    print("Serial Processing")
    arr = range(100000)
    ret = []
    
    for i in arr:
        ret.append(Square(i))
        
    #print("Result of seial processing is",ret)
    end = time.time()
    print("Time required for serial execution",end-start)
    
def main():
    print("Inside main")
    serialprocessing()
   
    
if __name__ == "__main__":
    main()