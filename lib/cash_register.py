#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            # Calculate the discount and apply it
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Print success message with updated total (cast to int for dollar precision)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            # Print error message if no discount is available
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

