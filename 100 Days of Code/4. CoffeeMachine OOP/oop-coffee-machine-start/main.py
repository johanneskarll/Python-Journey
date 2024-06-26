from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mac = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_obj = Menu()

is_on = True

while is_on:
    options = menu_obj.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_mac.report()
    else:
        drink = menu_obj.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_mac.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
