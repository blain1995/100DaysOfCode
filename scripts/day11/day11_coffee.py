MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(money):
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${money}')


def select_coffee():
    print("Options: espresso, latte or cappuccino")
    choice = input("Please make a choice: ")
    drink = MENU[choice]
    return drink


def insert_money(drink_cost):
    quarters = int(input("How many quarters?: "))
    total = quarters * 0.25
    if total > drink_cost:
        return round(total, 2)
    dimes = int(input("How many dimes?: "))
    total += dimes * 0.1
    if total > drink_cost:
        return round(total, 2)
    nickles = int(input("How many nickles?: "))
    total += nickles * 0.05
    if total > drink_cost:
        return round(total, 2)
    pennies = int(input("How many pennies?: "))
    total += pennies * 0.01
    return round(total, 2)


def vend_drink(inputs):
    for i in inputs:
        resources[i] -= inputs[i]


def refill_machine():
    levels = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    print("Refilling machine \n"
          ". \n"
          "... \n"
          "...... \n"
          "............... refilled!")
    return levels


def run_coffee():
    global resources
    drink_choice = select_coffee()
    drink_requirements = drink_choice['ingredients']
    value = drink_choice["cost"]
    for i in drink_requirements:
        if resources[i] < drink_requirements[i]:
            print(f"Not enough {i}")
            print(f"I'm sorry, you need to refill the machine.")
            if input("Would you like to do this now? 'yes' or 'no': ") == 'yes':
                resources = refill_machine()
            else:
                return
    print(f"Drink costs {value}, please insert coins")
    money = insert_money(value)
    if money > value:
        print(f"Total money inserted: ${money}")
        change = round((money - value), 2)
        money -= round(change, 2)
        print(f"Total change given: ${change}")
        print("Vending your drink now!")
    else:
        print(f"I'm sorry, you failed to insert enough money. Here is a refund of ${money}")
        return
    vend_drink(drink_requirements)
    money = 0
    report(money)
    print("Here is your drink, enjoy!")


while input("Machine Status: 'on' / 'off'") == 'on':
    run_coffee()
print("Machine shutting down: \n"
      "- \n"
      "--- \n"
      "----- \n"
      "---------- \n"
      "------------------- off \n"
      "Goodnight!")
