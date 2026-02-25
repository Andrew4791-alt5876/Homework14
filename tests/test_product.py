import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from src.product import Product


class TestProduct:
    def test_init(self, sample_product: Product) -> None:
        """Проверка инициализации продукта."""
        assert sample_product.name == "Телефон"
        assert sample_product.description == "Смартфон"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10

    def test_new_product(self, sample_product_dict: dict) -> None:
        """Проверка создания продукта из словаря."""
        product = Product.new_product(sample_product_dict)
        assert product.name == "Ноутбук"
        assert product.description == "Мощный ноутбук"
        assert product.price == 120000.0
        assert product.quantity == 5
        assert isinstance(product, Product)

    def test_price_getter(self, sample_product: Product) -> None:
        """Геттер возвращает корректное значение."""
        assert sample_product.price == 50000.0

    def test_price_setter_increase(self, sample_product: Product) -> None:
        """Увеличение цены без подтверждения."""
        sample_product.price = 60000.0
        assert sample_product.price == 60000.0

    def test_price_setter_decrease_without_confirmation(
        self, sample_product: Product, monkeypatch: MonkeyPatch
    ) -> None:
        """Понижение цены с отказом пользователя (ввод 'n') — цена не меняется."""
        # Мокаем ввод пользователя: 'n'
        monkeypatch.setattr("builtins.input", lambda _: "n")
        sample_product.price = 40000.0
        assert sample_product.price == 50000.0  # цена осталась прежней

    def test_price_setter_decrease_with_confirmation(self, sample_product: Product, monkeypatch: MonkeyPatch) -> None:
        """Понижение цены с согласием пользователя (ввод 'y') — цена меняется."""
        monkeypatch.setattr("builtins.input", lambda _: "y")
        sample_product.price = 40000.0
        assert sample_product.price == 40000.0

    def test_price_setter_negative(self, sample_product: Product, capsys: CaptureFixture[str]) -> None:
        """Установка отрицательной цены — выводится сообщение и цена не меняется."""
        sample_product.price = -1000.0
        captured = capsys.readouterr()
        assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
        assert sample_product.price == 50000.0

    def test_price_setter_zero(self, sample_product: Product, capsys: CaptureFixture[str]) -> None:
        """Установка нулевой цены — сообщение и цена не меняется."""
        sample_product.price = 0
        captured = capsys.readouterr()
        assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
        assert sample_product.price == 50000.0

    def test_str(self, sample_product: Product) -> None:
        """Проверка строкового представления."""
        expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(sample_product) == expected

    def test_add(self) -> None:
        """Проверка сложения двух продуктов."""
        p1 = Product("A", "desc", 100.0, 2)  # 200
        p2 = Product("B", "desc", 50.0, 3)  # 150
        assert p1 + p2 == 350.0

    def test_add_with_different_products(self) -> None:
        p1 = Product("A", "desc", 100.0, 5)  # 500
        p2 = Product("B", "desc", 200.0, 1)  # 200
        assert p1 + p2 == 700.0

    def test_private_price_access(self, sample_product: Product) -> None:
        """Проверка, что напрямую к __price обратиться нельзя."""
        with pytest.raises(AttributeError):
            _ = sample_product.__price
