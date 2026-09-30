from menu import menu


def get_yes_or_no(question):
    while True:
        answer = input(question).strip().upper()

        if answer == "Y":
            return True

        elif answer == "N":
            return False

        else:
            print("Please enter Y for Yes or N for No.")


def get_menu_code():
    while True:
        code = input("\nEnter item code: ").strip().upper()

        if code in menu:
            return code

        print("That item code does not exist. Please try again.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be at least 1.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def add_order(orders, code, quantity):
    if code in orders:
        orders[code] += quantity
    else:
        orders[code] = quantity