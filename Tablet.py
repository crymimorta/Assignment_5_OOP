from Device import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()} | Resolution: {self.screen_resolution} | Weight: {self.weight}g"

    def browse_internet(self):
        return "Browsing the internet..."

    def use_touchscreen(self):
        return "Using touchscreen..."
