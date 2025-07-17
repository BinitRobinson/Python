import random

option=("rock","paper","sciccors")
running=True
while running:
    computer=random.choice(option)
    player=None

    while player not in option:
        player = input("Enter Rock, Paper, Sciccors:")

    print(f"Player :{player}")
    print(f"Computer :{computer}")

    if(player==computer):
        print("Tie!")
    elif(player=='rock' and computer=='sciccors'):
        print("You win!")
    elif(player=='paper' and computer=='rock'):
        print("You win!")
    elif(player=='sciccors' and computer=='paper'):
        print("You win!")
    else:
        print("You Loose!")

    if not input("play again?(Y/N)").lower()=="y":
        running=False
print("Thank for playing")


