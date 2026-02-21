from typing import Any

from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициализатор или конструктор."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self) -> Any:
        products_str = ""
        for product in self.__products:
            products_str += f"\n{product.name}, {product.price} Остаток: {product.quantity}"
        return products_str

    def add_product(self, product: Product) -> None:
        Category.product_count += 1
        return self.__products.append(product)
