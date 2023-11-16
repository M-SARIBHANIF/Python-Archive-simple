MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
},
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}
profit = 0
recources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_recource_sufficant(order_ingredient):
    for items in order_ingredient:
        if order_ingredient[items] >= recources[items]:
            print(f"Sorry not enough {items}")
            return False
    return True

def process_coins():
    print("Please insert coins")
    total = int(input("How many Quarters?"))*0.25
    total += int(input("How many Dimes?")) * 0.1
    total += int(input("How many Nickles?")) * 0.05
    total += int(input("How many Pennies?")) * 0.01
    return total

def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_recieved - drink_cost,2)
        print(f"Here is your Change ${change}")
        return True
    else:
        print("Sorry That's Not Enough Money")
        return False
    
def make_la_coffee(drink_name,order_ingredients):
    for items in order_ingredients:
        recources[items]-=order_ingredients[items]
    print(f"Here is your Drink {drink_name}")

is_on = True

while True:
    choice=input("What would you like(espresso/latte/cappuccino)").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water:{recources['water']}")
        print(f"Milk:{recources['milk']}")
        print(f"Coffee:{recources['coffee']}")
        print(f"Money:${profit}")
    else:
        Drink = MENU[choice]
        if is_recource_sufficant(Drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,Drink["cost"]):
                make_la_coffee(choice,Drink["ingredients"])



