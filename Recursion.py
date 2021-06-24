
def DisplayIF(no):
    for i in range(no):   # Iteration Using For Loop
        print("Hello")
        
def DisplayIW(no):
    while no != 0:
        print("Hello")
        no = no - 1   #Iteration Using While Loop
        
def DisplayR(no):
           if no !=0:
              no = no - 1
              print("Hello")
              DisplayR(no)   #Ricursive Call
        
def main():
    print("Enter the number of Iteration")
    value = int(input())

    print("Calling Iterative Function With For Loop")
    DisplayIF(value)
    
    print("Calling Iterative Function With While Loop")
    DisplayIW(value)
    
    print("Calling the recursion Function")
    DisplayR(value)

if __name__ == "__main__":
    main()