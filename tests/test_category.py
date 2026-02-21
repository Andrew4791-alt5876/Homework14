import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(sample_category: Category) -> None:
    """Проверяет корректность инициализации категории."""
    cat = sample_category
    assert cat.name == "Test Category"
    assert cat.description == "Test Description"
    # Проверяем, что приватный список продуктов содержит ожидаемые объекты
    # (доступ через "name mangling" только для тестирования)
    assert len(cat._Category__products) == 2  # type: ignore[attr-defined]
    assert cat._Category__products[0].name == "Product1"  # type: ignore[attr-defined]
    assert cat._Category__products[0].description == "description1"  # type: ignore[attr-defined]
    assert cat._Category__products[0].price == 5  # type: ignore[attr-defined]
    assert cat._Category__products[0].quantity == 50  # type: ignore[attr-defined]
    assert cat._Category__products[1].name == "Product2"  # type: ignore[attr-defined]
    assert cat._Category__products[1].description == "description2"  # type: ignore[attr-defined]
    assert cat._Category__products[1].price == 200  # type: ignore[attr-defined]
    assert cat._Category__products[1].quantity == 150  # type: ignore[attr-defined]


def test_category_counts_on_creation() -> None:
    """Проверяет, что при создании категорий правильно увеличиваются счётчики."""
    # Принудительно сбрасываем счётчики, чтобы избежать влияния других тестов
    Category.category_count = 0
    Category.product_count = 0

    Category("Cat1", "Desc1", [])
    assert Category.category_count == 1
    assert Category.product_count == 0

    products = [Product("P1", "DescP1", 10, 1), Product("P2", "DescP2", 20, 2)]
    Category("Cat2", "Desc2", products)
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_add_product(sample_category: Category) -> None:
    """Проверяет добавление продукта через метод add_product."""
    cat = sample_category
    initial_count = Category.product_count
    product_3 = Product("Product3", "phone", 300, 7)
    cat.add_product(product_3)
    # Проверяем, что продукт добавлен в приватный список
    assert len(cat._Category__products) == 3  # type: ignore[attr-defined]
    assert cat._Category__products[-1].name == "Product3"  # type: ignore[attr-defined]
    assert cat._Category__products[-1].description == "phone"  # type: ignore[attr-defined]
    assert cat._Category__products[-1].price == 300  # type: ignore[attr-defined]
    assert cat._Category__products[-1].quantity == 7  # type: ignore[attr-defined]
    # Проверяем, что общий счётчик продуктов увеличился на 1
    assert Category.product_count == initial_count + 1


def test_products_property(sample_category: Category) -> None:
    """Проверяет, что свойство products возвращает корректную строку."""
    cat = sample_category
    expected = "\nProduct1, 5 Остаток: 50\nProduct2, 200 Остаток: 150"
    assert cat.products == expected


def test_private_products_encapsulation() -> None:
    """Проверяет, что прямой доступ к __products невозможен."""
    cat = Category("Test", "Desc", [])
    with pytest.raises(AttributeError):
        cat.__products
    # Однако доступ через name mangling возможен, но это не должно поощряться
    # Проверяем, что атрибут существует под "искажённым" именем
    assert hasattr(cat, "_Category__products")


def test_add_product_updates_products_property(sample_category: Category) -> None:
    """Проверяет, что после добавления продукта свойство products обновляется."""
    cat = sample_category
    new_product = Product("Product3", "description3", 300, 7)
    cat.add_product(new_product)
    expected = "\nProduct1, 5 Остаток: 50\nProduct2, 200 Остаток: 150\nProduct3, 300 Остаток: 7"
    assert cat.products == expected
