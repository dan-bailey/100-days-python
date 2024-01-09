# pizza order
# my god, this is just basic bullshit
# i only do this in the name of thoroughness
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")    
extra_cheese = input("Do you want extra cheese? Y or N: ")

# set price
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

# add pepperoni
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

# add extra cheese
if extra_cheese == "Y":
    price += 1

# print out order summary
print(f"You order will cost: ${price}")