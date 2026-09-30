from menu import is_valid_item, get_price


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
            else:
                return quantity

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")


def get_order():
    orders = {}

    while True:
        item = input(
            "\nEnter the menu item you want: "
        ).strip().title()

        if not is_valid_item(item):
            print("Invalid item. Please choose from the menu.")
            continue

        quantity = get_quantity()

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        while True:
            another = input(
                "Do you want to order another item? (yes/no): "
            ).strip().lower()

            if another in ["yes", "y"]:
                break

            elif another in ["no", "n"]:
                return orders

            else:
                print("Please enter yes or no.")


def calculate_order(orders):
    subtotal = 0

    for item, quantity in orders.items():
        subtotal += get_price(item) * quantity

    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    total = subtotal - discount

    return subtotal, discount, total