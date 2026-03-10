from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициализатор или конструктор класса Category."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """Подсчет продуктов в категории."""
        if isinstance(product, Product):
            Category.product_count += 1
            self.__products.append(product)
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Вывод продуктов в категории."""
        products = ""
        for product in self.__products:
            products += f"{product}\n"
        return products

    def __str__(self) -> str:
        """Вывод информации о категории."""
        quantity_sum = 0
        for product in self.__products:
            quantity_sum += product.quantity
        return f"{self.name}, количество продуктов: {quantity_sum} шт."

    def middle_price(self) -> float:
        """Метод, который подсчитывает средний ценник всех товаров."""
        price_sum = 0
        for product in self.__products:
            price_sum += product.price
        try:
            return round(price_sum / len(self.__products), 2)
        except ZeroDivisionError:
            return 0.0
