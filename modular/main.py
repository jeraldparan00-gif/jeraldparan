from display import display_welcome, ask_yes_no
from menu import display_menu
from order import get_order, calculate_order
from receipt import print_receipt


def main():
    display_welcome()

    display_menu()

    if not ask_yes_no(
        "\nDo you want to order? (yes/no): "
    ):
        print("\nThank you for visiting!")
        print("Have a great day!")
        return

    orders = get_order()

    if not orders:
        print("\nNo items were ordered.")
        print("Thank you for visiting!")
        return

    subtotal, discount, total = calculate_order(orders)

    print_receipt(
        orders,
        subtotal,
        discount,
        total
    )


if __name__ == "__main__":
    main()