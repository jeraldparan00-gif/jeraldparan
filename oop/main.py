from restaurant import (
    display_menu,
    get_order,
    calculate_order,
    print_receipt
)


def main():
    print("\n============================================")
    print("       WELCOME TO FAST FOOD RESTAURANT")
    print("============================================")

    display_menu()

    while True:
        choice = input(
            "\nDo you want to order? (yes/no): "
        ).strip().lower()

        if choice == "yes" or choice == "y":
            break

        elif choice == "no" or choice == "n":
            print("\nThank you for visiting!")
            print("Have a great day!")
            return

        else:
            print("Please enter yes or no.")

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
