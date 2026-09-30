from display import (
    print_welcome,
    print_menu,
    print_order_summary,
    print_receipt
)

from ordering import (
    get_yes_or_no,
    get_menu_code,
    get_quantity,
    add_order
)

from billing import (
    calculate_subtotal,
    get_discount,
    get_payment
)

from menu import menu


def main():
    orders = {}

    print_welcome()
    print_menu()

    # Ask if customer wants to order
    if not get_yes_or_no(
        "\nWould you like to order? [Y/N]: "
    ):
        print("\nThank you for visiting D' HOUSE!")
        print("Have a great day!")
        return

    # Ordering loop
    while True:
        print_menu()

        code = get_menu_code()
        quantity = get_quantity()

        add_order(orders, code, quantity)

        item = menu[code]
        item_total = item["price"] * quantity

        print("\nItem Added Successfully!")
        print(
            f"{quantity} x {item['name']} "
            f"= ₱{item_total:.2f}"
        )

        print_order_summary(orders)

        if not get_yes_or_no(
            "\nWould you like to order another item? [Y/N]: "
        ):
            break

    # Calculate order
    subtotal = calculate_subtotal(orders)

    print("\nYour order is complete!")
    print(f"Subtotal: ₱{subtotal:.2f}")

    # Apply discount
    discount_name, discount_amount = get_discount(subtotal)

    total = subtotal - discount_amount

    # Get payment
    payment = get_payment(total)

    # Print final receipt
    print_receipt(
        orders,
        subtotal,
        discount_name,
        discount_amount,
        total,
        payment
    )


if __name__ == "__main__":
    main()