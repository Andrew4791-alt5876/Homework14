import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category() -> Category:
    """Создаёт категорию с двумя продуктами."""
    products = [Product("Product1", "description1", 5, 50), Product("Product2", "description2", 200, 150)]
    return Category("Test Category", "Test Description", products)


@pytest.fixture
def sample_product() -> Product:
    """Фикстура, возвращающая продукт с начальной ценой 100."""
    return Product("Тестовый товар", "Описание", 100.0, 5)
