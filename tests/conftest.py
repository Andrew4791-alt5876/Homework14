import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сбрасывает счётчики Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_category():
    """Создаёт категорию с двумя продуктами."""
    products = [
        Product("Product1", 'description1', 5, 50),
        Product("Product2", 'description2', 200, 150)
    ]
    return Category("Test Category", "Test Description", products)


@pytest.fixture
def sample_product():
    """Фикстура, возвращающая продукт с начальной ценой 100."""
    return Product("Тестовый товар", "Описание", 100.0, 5)
