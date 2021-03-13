from day12_menu import Menu, MenuItem
from day12_coffee_maker import CoffeeMaker
from day12_money_machine import MoneyMachine

machine = CoffeeMaker()
drink = Menu()
money = MoneyMachine()

is_on = True
while is_on:
    print(f"Drink options: {drink.get_items()}")
    name = input("What drink would you like?: ")
    if name == "off":
        is_on = False
    elif name == "report":
        print(machine.report())
        print(money.report())
    else:
        order = drink.find_drink(name)
        if machine.is_resource_sufficient(order):
            print(f"The cost of a {order.name} is ${order.cost}")
            if money.make_payment(order.cost):
                machine.make_coffee(order)
print("Goodbye!")