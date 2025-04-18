from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffee=CoffeeMaker()
machine=MoneyMachine()
is_on=True
while is_on:
    options=menu.get_items()

    order=input(f"What do you want to drink {options}?\n")
    if order=="off":
        is_on=False
    elif order=="report":
        coffee.report()
        machine.report()
    else:
        drink=menu.find_drink(order)

        if coffee.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
                coffee.make_coffee(drink)






