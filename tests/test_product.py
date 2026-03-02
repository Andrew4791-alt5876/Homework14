from typing import Any

import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.product import Product


def test_product_initialization(sample_product: Product) -> None:
    """Проверка инициализации атрибутов продукта."""
    assert sample_product.name == "Тестовый продукт"
    assert sample_product.description == "Описание тестового продукта"
    assert sample_product.price == 100.0  # через геттер
    assert sample_product.quantity == 10


def test_new_product_classmethod() -> None:
    """Проверка создания продукта из словаря."""
    data = {"name": "Словарный продукт", "description": "Создан через classmethod", "price": 200.0, "quantity": 3}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Словарный продукт"
    assert product.description == "Создан через classmethod"
    assert product.price == 200.0
    assert product.quantity == 3


def test_price_property_getter(sample_product: Product) -> None:
    """Геттер возвращает приватный атрибут."""
    assert sample_product.price == 100.0


def test_price_setter_increase(sample_product: Product) -> None:
    """Установка большей цены (без подтверждения)."""
    sample_product.price = 150.0
    assert sample_product.price == 150.0


def test_price_setter_decrease_with_confirmation_yes(sample_product: Product, monkeypatch: MonkeyPatch) -> None:
    """Установка меньшей цены с подтверждением 'y'."""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 80.0
    assert sample_product.price == 80.0


def test_price_setter_decrease_with_confirmation_no(sample_product: Product, monkeypatch: MonkeyPatch) -> None:
    """Установка меньшей цены с отказом 'n'."""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 80.0
    assert sample_product.price == 100.0  # цена не изменилась


def test_price_setter_negative_or_zero(sample_product: Product, capsys: Any) -> None:
    """Попытка установить отрицательную или нулевую цену."""
    sample_product.price = -10
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert sample_product.price == 100.0  # цена осталась прежней
    sample_product.price = 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert sample_product.price == 100.0


def test_product_str(sample_product: Product) -> None:
    """Проверка строкового представления."""
    expected = "Тестовый продукт, 100.0 руб. Остаток: 10 шт."
    assert str(sample_product) == expected


def test_product_add_same_type(sample_product: Product, another_product: Product) -> None:
    """Сложение двух продуктов возвращает сумму их стоимостей."""
    expected = (100.0 * 10) + (50.0 * 5)  # 1000 + 250 = 1250
    assert sample_product + another_product == expected


def test_product_add_different_type(sample_product: Product) -> None:
    """Сложение продукта с объектом другого класса вызывает TypeError."""

    class OtherClass:
        pass

    with pytest.raises(TypeError):
        _ = sample_product + OtherClass()


def test_product_add_with_non_product(sample_product: Product) -> None:
    """Сложение с числом, строкой и т.д. вызывает TypeError."""
    with pytest.raises(TypeError):
        _ = sample_product + 100
    with pytest.raises(TypeError):
        _ = sample_product + "строка"
    with pytest.raises(TypeError):
        _ = sample_product + None


def test_product_add_self(sample_product: Product) -> None:
    """Сложение продукта с самим собой удваивает стоимость."""
    expected = 2 * (100.0 * 10)
    assert sample_product + sample_product == expected


def test_product_add_zero_quantity(sample_product: Product) -> None:
    """Если у одного из продуктов quantity = 0, результат равен стоимости другого."""
    zero_product = Product("Ноль", "Нулевое количество", price=100, quantity=0)
    expected = sample_product.price * sample_product.quantity
    assert sample_product + zero_product == expected
