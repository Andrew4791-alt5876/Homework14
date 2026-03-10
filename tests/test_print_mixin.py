import pytest
from _pytest.capture import CaptureFixture

from src.print_mixin import PrintMixin


class Product(PrintMixin):
    """Тестовый класс, использующий миксин."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()


class TestPrintMixin:
    """Тесты для PrintMixin."""

    @pytest.mark.parametrize(
        "name, description, price, quantity, expected_repr",
        [
            (
                "Test",
                "A test product",
                10.99,
                5,
                "Product(Test, A test product, 10.99, 5)",
            ),
            (
                "Another",
                "Another product",
                99.99,
                0,
                "Product(Another, Another product, 99.99, 0)",
            ),
        ],
    )
    def test_repr(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        expected_repr: str,
    ) -> None:
        """Проверяет, что __repr__ возвращает строку в ожидаемом формате."""
        product = Product(name, description, price, quantity)
        assert repr(product) == expected_repr

    @pytest.mark.parametrize(
        "name, description, price, quantity",
        [
            ("Test", "A test product", 10.99, 5),
            ("Another", "Another product", 99.99, 0),
        ],
    )
    def test_init_prints_repr(
        self,
        capsys: CaptureFixture[str],
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Проверяет, что при создании объекта вызывается print(repr(self))."""
        Product(name, description, price, quantity)
        captured = capsys.readouterr()
        expected_repr = f"Product({name}, {description}, {price}, {quantity})"
        assert captured.out.strip() == expected_repr

    @pytest.mark.parametrize(
        "name, description, price, quantity",
        [
            ("Test", "A test product", 10.99, 5),
            ("Another", "Another product", 99.99, 0),
        ],
    )
    def test_attributes_set_correctly(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Проверяет, что атрибуты действительно установлены в экземпляре."""
        product = Product(name, description, price, quantity)
        assert product.name == name
        assert product.description == description
        assert product.price == price
        assert product.quantity == quantity
