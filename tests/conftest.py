import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category() -> Category:
    """Фикстура для первой категории."""
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    """Фикстура для первой категории."""
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def product() -> Product:
    """Фикстура продукта"""
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
