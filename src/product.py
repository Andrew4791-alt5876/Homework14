class Product:
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product_1 = Product('яблоко', 'спелое красное яблоко', 100.0, 100)
    product_2 = Product('ананас', 'спелый из Африки', 200.0, 10)

    print(product_1.name)
    print(product_2.name)
    print(product_1.description)
    print(product_2.description)
    print(product_1.price)
    print(product_2.price)
    print(product_1.quantity)
    print(product_2.quantity)
