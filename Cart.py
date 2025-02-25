class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            return f"Added {amount}x {device.name} to the cart."
        return "Not enough stock available."

    def remove_device(self, device, amount):
        for i, (d, a) in enumerate(self.items):
            if d == device:
                if amount >= a:
                    self.items.pop(i)
                else:
                    self.items[i] = (d, a - amount)
                self.total_price -= device.price * amount
                return "Item removed from the cart."
        return "Item not found in cart."

    def get_total_price(self):
        return f"Total Cart Price: {self.total_price}$"

    def print_items(self):
        if not self.items:
            return "Cart is empty."
        return '\n'.join([f"{amount}x {device.name} - {device.price * amount}$" for device, amount in self.items])

    def checkout(self):
        if not self.items:
            return "Cart is empty. Add items before checkout."
        receipt = "\nReceipt:\n" + self.print_items() + f"\nTotal: {self.total_price}$\nThank you for your purchase!"
        self.items.clear()
        self.total_price = 0
        return receipt