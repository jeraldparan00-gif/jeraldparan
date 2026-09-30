menu = {
    "Burger": 85.00,
    "Fries": 45.00,
    "Chicken": 120.00,
    "Pizza": 150.00,
    "Spaghetti": 100.00,
    "Soft Drink": 35.00,
    "Ice Cream": 50.00
}


def display_menu():
    print("\n============================================")
    print("           FAST FOOD RESTAURANT")
    print("                 FULL MENU")
    print("============================================")

    for item, price in menu.items():
        print(f"{item:<25} P{price:>8.2f}")

    print("============================================")


def is_valid_item(item):
    return item in menu


def get_price(item):
    return menu[item]