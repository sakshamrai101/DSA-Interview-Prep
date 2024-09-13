class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, item_name, quantity, price):
        self.total += price * quantity
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        if item_name not in self.items:
            return "Item not in cart."
        
        if quantity >= self.items[item_name]:
            # Remove the item completely if quantity to remove is greater or equal
            self.total -= price * self.items[item_name]
            del self.items[item_name]
        else:
            # Decrease the quantity and adjust total
            self.total -= price * quantity
            self.items[item_name] -= quantity

    def checkout(self, paid):
        if paid < self.total:
            return f"You paid {paid} but cart amount is {self.total}"
        balance = paid - self.total
        return f"Exchange amount: {balance}"


# Test the ShoppingCart
cart1 = ShoppingCart()
cart1.add_item('Condoms', 4, 10)
cart1.add_item('Books', 5, 5)
cart1.add_item('Laptop', 1, 100)
cart1.add_item('Shoes', 1, 25)

# Try removing more items than exist, it should remove the item completely
cart1.remove_item("Condoms", 5, 10)

# Proceed to checkout
print(cart1.checkout(500))
