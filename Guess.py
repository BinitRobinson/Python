import random

low=1
high=20
guesses=0
number=random.randint(low,high)
points=100

print("----------Try Your Luck!----------")

while True:
    guess=int(input(f"Enter the number between({low}-{high}): "))
    guesses+=1

    if guess<number:
        print(f"{guess} is too low")
    elif guess>number:
        print(f"{guess} is  too high")
    else :
        print(f"{guess} you guessed it right !")
        break

print(f"The number of guesses it took to guess the number is {guesses}")
points-=guesses
if(points<0):
    print("You really need to work on your guessing game")
else:
    print(f"Your scored {points} points ")

print("----------THANK YOU !----------")
