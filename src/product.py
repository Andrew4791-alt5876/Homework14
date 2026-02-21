class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализатор или конструктор."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product_dict):
        return cls(
            name=new_product_dict["name"],
            description=new_product_dict["description"],
            price=new_product_dict["price"],
            quantity=new_product_dict["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if self.__price > new_price:
                choose_user = input("Новая цена ниже, если согласны понизить цену введите 'y', если нет - 'n': ").lower()
                if choose_user == 'y':
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
