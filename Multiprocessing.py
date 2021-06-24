import os
import multiprocessing

def process1():
    print("Process1 is created")
    print("PID of process1 is :",os.getpid())
    print("PID of parent process of process1 is:",os.getppid())
    
def process2():
    print("Process2 is created")
    print("PID of process2 is :",os.getpid())
    print("PID of parent process of process2 is:",os.getppid())
    
    
def main():
    print("Inside main process")
    print("PID of current is",os.getpid())
    print("PID of parent process is :",os.getppid())
    
    p1 = multiprocessing.Process(target = process1,args = ())
    p2 = multiprocessing.Process(target = process2,args = ())
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("End of main process")
    
if __name__ == "__main__":
    main()