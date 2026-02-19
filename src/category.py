from src.product import Product


class Category:
    name: str
    description: str
    products: list
    amount_categories = 0
    amount_goods = 0


    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.amount_categories += 1
        Category.amount_goods += len(products) if products else 0