from menu import MENU, resources


def are_ingredients_sufficient(order_ingredients):
    """Return True when drink can be made, False when ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_payment(money_received, drink_cost):
    """Return True when payment is sufficient to cover the cost of the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def payment_transaction():
    """Returns the total from the inserted coins."""
    print("Please insert coins.")
    payment = dict(quarters=int(input("How many quarters?:")) * 0.25,
                   dime=int(input("How many dimes?: ")) * 0.10,
                   nickles=int(input("How many nickles?: ")) * 0.05,
                   pennies=int(input("How many pennies?: ")) * 0.01
                   )

    return round(sum(payment.values()), 2)


def make_coffee(drink, ingredients):
    """Subtract ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")


profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif "report" == choice:
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        print(f'That would be ${MENU[choice]["cost"]}, please!')
        if are_ingredients_sufficient(drink["ingredients"]):
            transaction = payment_transaction()
            if process_payment(transaction, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
