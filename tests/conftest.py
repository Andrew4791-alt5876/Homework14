import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для создания базового продукта"""
    return Product(
        name="Тестовый продукт",
        description="Описание тестового продукта",
        price=100.0,
        quantity=10,
    )


@pytest.fixture
def another_product() -> Product:
    """Фикстура для другого продукта (для сложения)"""
    return Product(
        name="Другой продукт",
        description="Другое описание",
        price=50.0,
        quantity=5,
    )


@pytest.fixture
def product1() -> Product:
    """Фикстура для первого продукта."""
    return Product("Товар 1", "Описание 1", 100.0, 5)


@pytest.fixture
def product2() -> Product:
    """Фикстура для второго продукта."""
    return Product("Товар 2", "Описание 2", 200.0, 10)


@pytest.fixture
def product3() -> Product:
    """Фикстура для третьего продукта."""
    return Product("Товар 3", "Описание 3", 300.0, 1)


@pytest.fixture
def category_with_products(product1: Product, product2: Product) -> Category:
    """Фикстура категории с двумя продуктами."""
    return Category("Электроника", "Разные товары", [product1, product2])


@pytest.fixture
def empty_category() -> Category:
    """Фикстура пустой категории."""
    return Category("Пустая", "Нет товаров", [])


@pytest.fixture(autouse=True)
def reset_counts() -> None:
    """Сбрасывает счетчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


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
