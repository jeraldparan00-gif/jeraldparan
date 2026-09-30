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


def get_order():
    orders = {}

    while True:
        item = input("\nEnter the menu item you want: ").strip().title()

        if item not in menu:
            print("Invalid item. Please choose from the menu.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    break

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        while True:
            another = input(
                "Do you want to order another item? (yes/no): "
            ).strip().lower()

            if another == "yes" or another == "y":
                break

            elif another == "no" or another == "n":
                return orders

            else:
                print("Please enter yes or no.")


def calculate_order(orders):
    subtotal = 0

    for item, quantity in orders.items():
        subtotal += menu[item] * quantity

    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    total = subtotal - discount

    return subtotal, discount, total


def print_receipt(orders, subtotal, discount, total):
    print("\n")
    print("=" * 60)
    print("                 FAST FOOD RESTAURANT")
    print("                    OFFICIAL RECEIPT")
    print("=" * 60)

    print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>15}{'TOTAL':>15}")
    print("-" * 60)

    for item, quantity in orders.items():
        price = menu[item]
        item_total = price * quantity

        print(
            f"{item:<20}"
            f"{quantity:>5}"
            f"P{price:>13.2f}"
            f"P{item_total:>13.2f}"
        )

    print("-" * 60)

    print(f"{'SUBTOTAL:':<45} P{subtotal:>10.2f}")
    print(f"{'DISCOUNT:':<45} P{discount:>10.2f}")
    print(f"{'TOTAL:':<45} P{total:>10.2f}")

    print("=" * 60)
    print("              Thank you for your order!")
    print("                  Please come again!")
    print("=" * 60)
