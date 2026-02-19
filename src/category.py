class Category:
    name: str
    description: str
    products: list


    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []