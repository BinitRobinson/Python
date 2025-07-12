#shopping cart programe
Cart=[]
prices=[]
while True:
    food=input("Add items to your cart(q to quit) :")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of the {food}: Rs"))
        Cart.append(food)
        prices.append(price)
print("-----Your Cart-----")
for items in Cart:
    print(items,end=" ")
total=0
for i in prices:
    total += i
print()
print(f"Your toatal is : Rs{total}")


