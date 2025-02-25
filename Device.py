class Device:
    def __init__(self, name: str, price: float, stock: int, warranty: int):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def display_info(self):
        return f"Device: {self.name} | Price: {self.price}$ | Stock: {self.stock} | Warranty: {self.warranty} months"

    def __str__(self):
        return self.display_info()

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
        return f"New discounted price: {self.price}$"

    def is_available(self, amount):
        return amount <= self.stock

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return f"Stock updated. Remaining: {self.stock}"
        return "Not enough stock available."

