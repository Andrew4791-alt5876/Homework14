from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализатор или конструктор класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, new_product_dict: dict) -> Any:
        """Класс-метод,
        который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product
        """
        return cls(
            name=new_product_dict["name"],
            description=new_product_dict["description"],
            price=new_product_dict["price"],
            quantity=new_product_dict["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер, возвращающий приватный атребут."""
        return self.__price

    @price.setter
    def price(self, new_price: float | int) -> Any:
        """Сеттер, который выполняет логику изменения приватного атребута."""
        if new_price > 0:
            if self.__price > new_price:
                choose_user = input(
                    "Новая цена ниже, если согласны понизить "
                    "цену введите 'y', если нет - 'n': "
                ).lower()
                if choose_user == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self) -> str:
        """Магический метод для отображения информации
        об объекте класса Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Магический метод, который позволяет прибавлять к экземпляру
        класса объект произвольного типа данных."""
        if type(self) is not type(other):
            raise TypeError
        return (self.__price * self.quantity) + (
            other.__price * other.quantity
        )
