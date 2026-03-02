import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product1() -> Product:
    """Фикстура продцкта №1."""
    return Product("Samsung Galaxy S23 Ultra", "Description1", 180000.0, 5)


@pytest.fixture
def product2() -> Product:
    """Фикстура продцкта №2."""
    return Product("Iphone 15", "Description2", 210000.0, 8)


@pytest.fixture
def product3() -> Product:
    """Фикстура продцкта №3."""
    return Product("Xiaomi Redmi Note 11", "Description3", 31000.0, 14)


@pytest.fixture
def category_with_products(product1: Product, product2: Product, product3: Product) -> Category:
    """Категория с тремя продуктами для тестов."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def empty_category() -> Category:
    """Пустая категория."""
    return Category("Пустая", "Описание пустой категории", [])


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для создания обычного продукта."""
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def sample_product_dict() -> dict:
    """Фикстура с данными для создания продукта через new_product."""
    return {"name": "Ноутбук", "description": "Мощный ноутбук", "price": 120000.0, "quantity": 5}


@pytest.fixture
def sample_phone() -> Smartphone:
    """Фикстура для создания типового объекта Smartphone."""
    return Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000,
        quantity=5,
        efficiency=95.5,
        model="15 Pro",
        memory=256,
        color="черный",
    )


@pytest.fixture
def sample_grass() -> LawnGrass:
    """Фикстура для создания типового объекта LawnGrass."""
    return LawnGrass(
        name="Изумрудная лужайка",
        description="Газонная трава для сада",
        price=1500,
        quantity=20,
        country="Россия",
        germination_period="10-14 дней",
        color="зеленый",
    )
