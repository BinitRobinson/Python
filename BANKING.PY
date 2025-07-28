def show_balance():
    print(f"Your balance is Rs {balance:.2f}")

def deposite():
    u=float(input("Enter the amout to be deposited : "))
    if u<0:
        print("Invalid Deposite !")
        return 0
    else :
        return u

def withdraw():
    a=float(input("Enter the amount to be withdraw: ")) 
    if a>balance:
        print("Insufficient balance !")
        return 0
    else:
        return a
   


balance=0
is_running=True

while is_running:
    print("***********************")
    print("*  BANKING PROGRAME   *")
    print("***********************")
    print("1) Show Balance")
    print("2) Deposite")
    print("3) Withdraw")
    print("4) Exit")
    print("****************************************************************")

    user=input("Enter your choice (1-4):")

    if user=="1":
        show_balance()
    elif user=="2":
        balance+=deposite()
    elif user=="3":
        balance-=withdraw()
    elif user=="4":
        is_running=False
    else :
        print("Invalid input try again !")

print("Thank You and have a nice day !")