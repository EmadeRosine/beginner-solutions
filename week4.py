# calculating cost of items in a shop
items={"book":"400","calculator":"1000","pen":"200","mathset":"1500","ruler":"250"}
print("WELCOME TO BLINKY'S SHOP. \n we sell gthe following items\n ")
for i in items:
    print(i)
buy1=input("what do you want to buy:\n ")
items={key.lower():val for key,val in items.items()}
buy1=buy1.lower()
if buy1 in items:
    price=items[buy1]
    print(f"The cost of {buy1} is {price}")
else:
    print("We dont sale that here!!")
quantity=int(input(f"how many {buy1}s do you want:\n "))
cost=int(items[buy1])*quantity
print('your bill for',buy1, f'is {cost}\n')
question=input("Do you need something else: \n")
question=question.lower()

if question=="yes":
    buy2=input("what do you want to buy: \n")
    items={key.lower():val for key,val in items.items()}
    buy2=buy2.lower()
    if buy2 in items:
        price=items[buy2]
        print(f"The cost of {buy2} is {price}\n")
    else:
        print("We dont sale that here!!")
    quantity1=int(input(f"how many {buy2}s do you want: \n"))
    cost1=int(items[buy2])*quantity1
    print('your bill for',buy2, f'is {cost1}\n')
    total_cost=cost+cost1
    print(f"Your total bill is {total_cost}\n")
elif question=="no":
    print(f"Your total bill is {cost}\n")
else:
    print("Invalid Response,Try again")

print("See you Next Time!")


