from Device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{super().__str__()} | RAM: {self.ram_size}GB | Processor: {self.processor_speed}GHz"

    def run_program(self):
        return "Running a program..."

    def use_keyboard(self):
        return "Typing on keyboard..."
