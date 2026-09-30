from menu import menu


def print_welcome():
    print("\n" + "=" * 60)
    print("                D' House")
    print("Where great food meets good vibes and good company")
    print("=" * 60)
    print("              Welcome,Cuz!")
    print("=" * 60)


def print_menu():
    print("\n" + "=" * 60)
    print("                    OUR MENU")
    print("=" * 60)

    print(f"{'CODE':<8}{'ITEM':<35}{'PRICE':>12}")
    print("-" * 60)

    for code, item in menu.items():
        print(
            f"{code:<8}"
            f"{item['name']:<35}"
            f"₱{item['price']:>10.2f}"
        )

    print("=" * 60)


def print_order_summary(orders):
    print("\n" + "-" * 60)
    print("                 CURRENT ORDER")
    print("-" * 60)

    for code, quantity in orders.items():
        item = menu[code]
        total = item["price"] * quantity

        print(
            f"{item['name']:<30}"
            f"x{quantity:<5}"
            f"₱{total:.2f}"
        )

    print("-" * 60)


def print_receipt(
    orders,
    subtotal,
    discount_name,
    discount_amount,
    total,
    payment
):
    change = payment - total

    print("\n\n")
    print("=" * 65)
    print("                    D' HOUSE")
    print("                 RESTAURANT RECEIPT")
    print("=" * 65)
    print("Date: Today")
    print("-" * 65)

    print(
        f"{'ITEM':<28}"
        f"{'QTY':>5}"
        f"{'PRICE':>14}"
        f"{'TOTAL':>16}"
    )

    print("-" * 65)

    for code, quantity in orders.items():
        item = menu[code]
        price = item["price"]
        item_total = price * quantity

        print(
            f"{item['name']:<28}"
            f"{quantity:>5}"
            f"₱{price:>12.2f}"
            f"₱{item_total:>14.2f}"
        )

    print("-" * 65)

    print(f"{'SUBTOTAL':<48} ₱{subtotal:>13.2f}")
    print(
        f"{discount_name:<48} "
        f"-₱{discount_amount:>12.2f}"
    )
    print(f"{'TOTAL AMOUNT':<48} ₱{total:>13.2f}")
    print(f"{'CASH RECEIVED':<48} ₱{payment:>13.2f}")
    print(f"{'CHANGE':<48} ₱{change:>13.2f}")

    print("=" * 65)
    print("              THANK YOU FOR ORDERING!")
    print("             COME BACK AGAIN, CUZ!")
    print("=" * 65)