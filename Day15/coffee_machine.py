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


def show_report():
    """Muestra el reporte de los recursos y el dinero"""
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value}ml")


def choose_option():
    """Eliges las opciones de cafe o mostrar el reporte"""
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "report":
        show_report()
    elif(option == "off"):
        return option
    else:
        check_resorurces(option)


def check_resorurces(kind_of_coffee):
    """Chequea si hay suficientes recurso para hacer el cafe y si se introdujo sufiente dinero"""
    coffee = MENU[kind_of_coffee]
    ingredients = coffee["ingredients"]
    cost = coffee["cost"]
    continue_the_process = True
    for item in resources:
        if item == "milk" and kind_of_coffee == "espresso":
            pass
        else:
            if ingredients[item] >= resources[item]:
                print(f"Sorry there is not enough {item}.")
                continue_the_process = False
    if continue_the_process == True:
        money, change = process_coins(0, cost)
        if money >= cost:
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {kind_of_coffee} ☕️. Enjoy!")
            deduct_resources(kind_of_coffee)
        else:
            print("Sorry that's not enough money. Money refunded.")


def process_coins(money, cost):
    """Retorna el total de las monedas introducidas y su cambio"""
    quarter = .25
    dime = .10
    nickle = .05
    pennie = .01
    print("Please insert coins.")
    money = int(input("how many quarters?: ")) * quarter
    money += int(input("how many dimes?: ")) * dime
    money += int(input("how many nickles?: ")) * nickle
    money += int(input("how many pennies?: ")) * pennie
    change = money - cost
    return money, change


def deduct_resources(kind_of_coffee):
    """Resta los ingredientes utilizados a los recursos"""
    coffee = MENU[kind_of_coffee]
    ingredients = coffee["ingredients"]
    for key in resources:
        if key == "milk" and kind_of_coffee == "espresso":
            pass
        else:
            resources[key] = resources[key] - ingredients[key]


def main():
    turn_on = "on"
    while(turn_on != "off"):
        turn_on = choose_option()

main()





