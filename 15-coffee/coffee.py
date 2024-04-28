## Coffee Code
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True

def is_resource_sufficient(order_ingredients):
    """ Returns True/False if resources are sufficient """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    """ Collect and process payment. """
    print("Please insert coins.")
    total = (int(input("How many quarters? ")) * 0.25) + (int(input("How many dimes? ")) * 0.1) + (int(input("How many nickels? ")) * 0.05) + (int(input("How many pennies? ")) * 0.01)
    return total

def is_transaction_successful(money_received, cost_of_drink):
    """ Returns boolean value. """
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry, not enough money.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffee!  Enjoy!  ☕️")

## What would you like prompt?
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


