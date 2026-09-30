
class Restaurant:

    # Constructor
    def __init__(self):
        self.name = "D HOUSE"

        # Menu attribute
        self.menu = {
            "A1": {"name": "lobster Thermidor", "price": 780.00},
            "A2": {"name": "Garlic Butter Prawns", "price": 650.00},
            "A3": {"name": "Fish Fillet", "price": 480.00},
            "A4": {"name": "Seared Scallops", "price": 450.00},
            "B1": {"name": "Beef Carpaccio", "price": 999.00},
            "B2": {"name": "Beef Steak", "price": 890.00},
            "B3": {"name": "Beef Wellington", "price": 1299.00},
            "C1": {"name": "Porchetta", "price": 399.00},
            "C2": {"name": "Parmesan-Crusted Pork Loin", "price": 450.00},
            "C3": {"name": "Pork Steak", "price": 380.00},
            "D1": {"name": "Mango Basil Spritz", "price": 129.00},
            "D2": {"name": "Pineapple Ginger Fizz", "price": 129.00}
        }

        # Stores customer orders
        self.orders = {}

    # ------------------------------------------------
    # PRINT WELCOME
    # ------------------------------------------------
    def print_welcome(self):
        print("\n" + "=" * 60)
        print("                     D' HOUSE")
        print("Where great food meets good vibes and good company.")
        print("=" * 60)
        print("                    Welcome Cuz!")
        print("=" * 60)

    # ------------------------------------------------
    # PRINT MENU
    # ------------------------------------------------
    def print_menu(self):
        print("\n" + "=" * 60)
        print("                      OUR MENU")
        print("=" * 60)

        print(f"{'CODE':<8}{'ITEM':<35}{'PRICE':>12}")
        print("-" * 60)

        for code, item in self.menu.items():
            print(
                f"{code:<8}"
                f"{item['name']:<35}"
                f"₱{item['price']:>10.2f}"
            )

        print("=" * 60)

    # ------------------------------------------------
    # GET YES OR NO
    # ------------------------------------------------
    def get_yes_or_no(self, question):
        while True:
            answer = input(question).strip().upper()

            if answer == "Y":
                return True

            elif answer == "N":
                return False

            else:
                print("Please enter Y for Yes or N for No.")

    # ------------------------------------------------
    # GET MENU CODE
    # ------------------------------------------------
    def get_menu_code(self):
        while True:
            code = input("\nEnter item code: ").strip().upper()

            if code in self.menu:
                return code

            print("That item code does not exist. Please try again.")

    # ------------------------------------------------
    # GET QUANTITY
    # ------------------------------------------------
    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity

                print("Quantity must be at least 1.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    # ------------------------------------------------
    # ADD ORDER
    # ------------------------------------------------
    def add_order(self, code, quantity):
        if code in self.orders:
            self.orders[code] += quantity
        else:
            self.orders[code] = quantity

    # ------------------------------------------------
    # CALCULATE SUBTOTAL
    # ------------------------------------------------
    def calculate_subtotal(self):
        subtotal = 0

        for code, quantity in self.orders.items():
            price = self.menu[code]["price"]
            subtotal += price * quantity

        return subtotal

    # ------------------------------------------------
    # GET DISCOUNT
    # ------------------------------------------------
    def get_discount(self, subtotal):
        print("\n" + "-" * 60)
        print("                    DISCOUNTS")
        print("-" * 60)
        print("1 - No Discount")
        print("2 - Student Discount (5%)")
        print("3 - Senior/PWD Discount (20%)")
        print("-" * 60)

        while True:
            choice = input("Choose discount: ").strip()

            if choice == "1":
                return "No Discount", 0

            elif choice == "2":
                discount = subtotal * 0.05
                return "Student Discount", discount

            elif choice == "3":
                discount = subtotal * 0.20
                return "Senior/PWD Discount", discount

            else:
                print("Invalid choice. Please choose 1, 2, or 3.")

    # ------------------------------------------------
    # GET PAYMENT
    # ------------------------------------------------
    def get_payment(self, total):
        while True:
            try:
                print(f"\nAmount Due: ₱{total:.2f}")
                payment = float(input("Cash Received: ₱"))

                if payment >= total:
                    return payment

                print("Not enough cash. Please enter a sufficient amount.")

            except ValueError:
                print("Invalid amount. Please enter a valid number.")

    # ------------------------------------------------
    # PRINT ORDER SUMMARY
    # ------------------------------------------------
    def print_order_summary(self):
        print("\n" + "-" * 60)
        print("                 CURRENT ORDER")
        print("-" * 60)

        for code, quantity in self.orders.items():
            item = self.menu[code]
            total = item["price"] * quantity

            print(
                f"{item['name']:<30}"
                f"x{quantity:<5}"
                f"₱{total:.2f}"
            )

        print("-" * 60)

    # ------------------------------------------------
    # PRINT RECEIPT
    # ------------------------------------------------
    def print_receipt(
        self,
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

        for code, quantity in self.orders.items():
            item = self.menu[code]
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
        print("            THANK YOU FOR ORDERING!")
        print("             COME BACK AGAIN, CUZ!")
        print("=" * 65)

    # ------------------------------------------------
    # RUN RESTAURANT SYSTEM
    # ------------------------------------------------
    def run(self):

        self.print_welcome()
        self.print_menu()

        # Ask if customer wants to order
        if not self.get_yes_or_no(
            "\nWould you like to order? [Y/N]: "
        ):
            print("\nThank you for visiting D' House!")
            print("Have a great day!")
            return

        # Ordering loop
        while True:

            self.print_menu()

            code = self.get_menu_code()
            quantity = self.get_quantity()

            self.add_order(code, quantity)

            item = self.menu[code]
            item_total = item["price"] * quantity

            print("\nItem Added Successfully!")
            print(
                f"{quantity} x {item['name']} "
                f"= ₱{item_total:.2f}"
            )

            self.print_order_summary()

            if not self.get_yes_or_no(
                "\nWould you like to order another item? [Y/N]: "
            ):
                break

        # Calculate subtotal
        subtotal = self.calculate_subtotal()

        print("\nYour order is complete!")
        print(f"Subtotal: ₱{subtotal:.2f}")

        # Apply discount
        discount_name, discount_amount = self.get_discount(subtotal)

        total = subtotal - discount_amount

        # Get payment
        payment = self.get_payment(total)

        # Print receipt
        self.print_receipt(
            subtotal,
            discount_name,
            discount_amount,
            total,
            payment
        )