Amount = 1000

def ATM(func):
    func()

def Deposit():
    value = int(input("Enter the amount to Deposit  : "))
    global Amount
    Amount = Amount + value
    print("Deposit Successful - Balance:",Amount)
    
def withdraw():
    value = int(input("Enter the amount to withdraw : "))
    global Amount
    if value > Amount:
        print("There is no Sufficeint balance")
    else:
        Amount = Amount- value
        print("Withdraw Successful - Balance :",Amount)
def main():
    print("Inside main")
    ATM(Deposit)
    ATM(withdraw)

if __name__ == "__main__":
    main()