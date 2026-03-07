from abc import ABC
from typing import Any

import pytest

from src.base_product import BaseProduct


class ConcreteProduct(BaseProduct):
    """Конкретная реализация BaseProduct для тестов."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @classmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "ConcreteProduct":
        return cls(*args, **kwargs)


class TestBaseProduct:
    """Тесты для абстрактного базового класса BaseProduct."""

    def test_base_product_is_abstract(self) -> None:
        """Проверяет, что BaseProduct наследует ABC."""
        assert issubclass(BaseProduct, ABC)
        assert isinstance(BaseProduct, type(ABC))

    def test_new_product_is_abstract_method(self) -> None:
        """Проверяет, что new_product помечен как абстрактный метод."""
        assert hasattr(BaseProduct.new_product, "__isabstractmethod__")
        assert BaseProduct.new_product.__isabstractmethod__ is True

    def test_cannot_instantiate_base_product(self) -> None:
        """Проверяет, что нельзя создать экземпляр абстрактного класса."""
        with pytest.raises(TypeError) as exc_info:
            BaseProduct()  # type: ignore[abstract]
        error_msg = str(exc_info.value)
        assert "Can't instantiate abstract class BaseProduct" in error_msg

    def test_concrete_product_can_be_instantiated(self) -> None:
        """Проверяет создание конкретной реализации."""
        product = ConcreteProduct("Test Product", 99.99)
        assert isinstance(product, ConcreteProduct)
        assert product.name == "Test Product"
        assert product.price == 99.99

    def test_new_product_implementation(self) -> None:
        """Проверяет работу метода класса new_product."""
        product = ConcreteProduct.new_product("Test Product", 99.99)
        assert isinstance(product, ConcreteProduct)
        assert product.name == "Test Product"
        assert product.price == 99.99

    def test_subclass_without_implementation_remains_abstract(self) -> None:
        """Подкласс без реализации остаётся абстрактным."""

        class IncompleteProduct(BaseProduct):
            pass

        with pytest.raises(TypeError) as exc_info:
            IncompleteProduct()  # type: ignore[abstract]
        error_msg = str(exc_info.value)
        assert (
            "Can't instantiate abstract class IncompleteProduct" in error_msg
        )
        assert "new_product" in error_msg
