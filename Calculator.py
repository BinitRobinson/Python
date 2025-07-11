# project 1 simple calculator
#operation needed +,-,*,/

#function to add 
def add(x,y):
    a=round(x+y)
    return a

#function to subtract
def sub(x,y):
    a=round(x-y)
    return a

#function to multiply
def multi(x,y):
    a=round(x*y)
    return a

#function to devide
def devi(x,y):
    if(y==0):
        print("Error")
    else:
        a=round(x/y)
        return a

Num1=float(input("enter the number:"))
Num2=float(input("enter the number:"))
operator=input("Enter an operator '+','-','*','/':")

if(operator=='+'):
    print("=",add(Num1,Num2))

elif(operator=='-'):
    print("=",sub(Num1,Num2))

elif(operator=='*'):
    print("=",multi(Num1,Num2))

elif(operator=='/'):
    print("=",devi(Num1,Num2))

else:
    print(f"{operator}is not valid")



