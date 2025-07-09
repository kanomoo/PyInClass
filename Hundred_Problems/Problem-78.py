class Cashier:
    def __init__(self):
        self.data = {}
        pass

    def add_product(self, name: str, price: float, quantity: int):
        self.data[name] = price,quantity

    def remove_product(self, name: str):
        pass

    def calculate_total(self) -> float:
        pass

    def display_products(self):
        pass