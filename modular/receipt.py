from menu import get_price


def print_receipt(orders, subtotal, discount, total):
    print("\n")
    print("=" * 60)
    print("                 FAST FOOD RESTAURANT")
    print("                    OFFICIAL RECEIPT")
    print("=" * 60)

    print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>15}{'TOTAL':>15}")
    print("-" * 60)

    for item, quantity in orders.items():
        price = get_price(item)
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