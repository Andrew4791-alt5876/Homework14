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
            products_str += (f"\n{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_str

    def add_product(self, product: Product) -> None:
        Category.product_count += 1
        self.__products.append(product)
