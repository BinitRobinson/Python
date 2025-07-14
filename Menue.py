menue={
    "pizza":200,
    "burger":150,
    "fries":200,
    "lemonade":100,
    "pasta":300,
    "mojito":80
}
cart=[]
total=0

print("----------MENUE----------")
for keys,values in menue.items():
    print(f"{keys:10}: Rs {values}")
print("-------------------------")

while True:
    food=input("Select the items to  add to your cart(press q to quit):").lower()
    if food=="q":
        break
    elif menue.get(food) is not None:
        cart.append(food)

for  food in cart:
    total+=menue.get(food)
    print(food,end=" ")
print()

print(f"Your total amount to be paid is Rs {total:2f}")