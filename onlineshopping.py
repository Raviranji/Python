class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.__cart_items = {}          # Encapsulated cart items
        self.__total_amount = 0.0       # Private total amount

    # Add item to cart
    def add_item(self, item_name, price):
        if price <= 0:
            print("Invalid price. Price must be greater than 0.")
            return

        self.__cart_items[item_name] = price
        self.__total_amount += price
        print("Item added successfully")

    # Remove item from cart
    def remove_item(self, item_name):
        if item_name in self.__cart_items:
            self.__total_amount -= self.__cart_items[item_name]
            del self.__cart_items[item_name]
            print("Item removed successfully")
        else:
            print("Item not found in cart")

    # Apply discount
    def apply_discount(self, code):
        if code == "SAVE10" and self.__total_amount >= 1000:
            discount = self.__total_amount * 0.10
            self.__total_amount -= discount
            print("Discount applied successfully")

        elif code == "SAVE20" and self.__total_amount >= 2000:
            discount = self.__total_amount * 0.20
            self.__total_amount -= discount
            print("Discount applied successfully")

        elif code in ["SAVE10", "SAVE20"]:
            print("Discount code not applicable for current total")

        else:
            print("Invalid discount code")

    # Checkout process
    def checkout(self):
        if not self.__cart_items:
            print("Checkout failed: Cart is empty")
            return

        if self.__total_amount < 500:
            print("Checkout failed: Minimum order amount is 500")
            return

        print("\nCheckout successful")
        print("Items Purchased:")
        for item, price in self.__cart_items.items():
            print(f"{item}: {price}")

        print(f"Total Payable Amount: {self.__total_amount:.2f}")


# ---------------- MAIN PROGRAM ----------------

customer = input("Enter customer name: ")
cart = ShoppingCart(customer)

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Apply Discount")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        try:
            price = float(input("Enter price: "))
            cart.add_item(item, price)
        except ValueError:
            print("Invalid price input")

    elif choice == "2":
        item = input("Enter item name to remove: ")
        cart.remove_item(item)

    elif choice == "3":
        code = input("Enter discount code: ")
        cart.apply_discount(code)

    elif choice == "4":
        cart.checkout()

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please try again.")
