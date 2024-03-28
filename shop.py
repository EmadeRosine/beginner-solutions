# calculating cost of items in a shop
items={"pant":400,"T-shirts":5000,"bra":500,"Trouser":4000,"caps":2500,"Innerwear":3000,"Perfume":5000,"Rubbing oil":14000}
items={key.lower():val for key,val in items.items()}
print("Welcome to Blinky's shop. Here we sell the following products\n")
for item in items:
    print("-",item)
# Initialize the total cost to zero
total_cost = 0

# Ask the customer for the items they want to buy
while True:
    item = input('What item will you like to purchase( Note that to stop purchase enter the word "done" ) :')
    if item == 'done':
        break
    elif item not in items:
        print('Sorry, we don\'t have that item.')
    else:
        quantity = int(input(f'How many {item}s do you want? '))
        total_cost = total_cost + (items[item] * quantity)

# Display the total cost to the customer
print(f'The total cost of your purchase is {total_cost:.2f}F CFA')