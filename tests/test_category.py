from src.category import Category
#
#
# def test_category_init(first_category: Any, second_category: Any) -> None:
#     """Тесты для класса Category."""
#     assert first_category.name == "Смартфоны"
#     assert first_category.description == "Смартфоны, как средство не только коммуникации"
#     assert second_category.name == "Телевизоры"
#     assert second_category.description == "Современный телевизор"
#     assert len(first_category.products) == 3
#     assert len(second_category.products) == 1
#     assert first_category.category_count == 2
#     assert second_category.category_count == 2
#     assert first_category.product_count == 4
#     assert second_category.product_count == 4
#
#
# def test_category_products_default_to_empty_list() -> Any:
#     """Проверка, что при отсутствии аргумента products создаётся пустой список."""
#     category = Category("Категория", "Описание")
#     assert category.products == []
#
#
# def test_category_products_passed_as_none() -> Any:
#     """Проверка, что при явной передаче None создаётся пустой список."""
#     category = Category("Категория", "Описание", None)
#     assert category.products == []


import pytest

from src.product import Product


# Предполагаем, что классы Category и Product доступны для импорта
# Если Product не определён, создадим простую версию для тестов
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


def test_category_initialization(sample_category):
    """Проверяет корректность инициализации категории."""
    cat = sample_category
    assert cat.name == "Test Category"
    assert cat.description == "Test Description"
    # Проверяем, что приватный список продуктов содержит ожидаемые объекты
    # (доступ через "name mangling" только для тестирования)
    assert len(cat._Category__products) == 2
    assert cat._Category__products[0].name == "Product1"
    assert cat._Category__products[0].description == "description1"
    assert cat._Category__products[0].price == 5
    assert cat._Category__products[0].quantity == 50
    assert cat._Category__products[1].name == "Product2"
    assert cat._Category__products[1].description == "description2"
    assert cat._Category__products[1].price == 200
    assert cat._Category__products[1].quantity == 150


def test_category_counts_on_creation():
    """Проверяет, что при создании категории увеличиваются счётчики."""
    cat1 = Category("Cat1", "Desc1", [])
    assert Category.category_count == 1
    assert Category.product_count == 0

    products = [Product("P1", '10', 1, 20), Product("P2", '20', 2, 10)]
    cat2 = Category("Cat2", "Desc2", products)
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_add_product(sample_category):
    """Проверяет добавление продукта через метод add_product."""
    cat = sample_category
    initial_count = Category.product_count
    product_3 = Product("Product3", "phone", 300, 7)
    cat.add_product(product_3)
    # Проверяем, что продукт добавлен в приватный список
    assert len(cat._Category__products) == 3
    assert cat._Category__products[-1].name == "Product3"
    assert cat._Category__products[-1].description == "phone"
    assert cat._Category__products[-1].price == 300
    assert cat._Category__products[-1].quantity == 7
    # Проверяем, что общий счётчик продуктов увеличился на 1
    assert Category.product_count == initial_count + 1


def test_products_property(sample_category):
    """Проверяет, что свойство products возвращает корректную строку."""
    cat = sample_category
    expected = "\nProduct1, 5 Остаток: 50\nProduct2, 200 Остаток: 150"
    assert cat.products == expected


def test_private_products_encapsulation():
    """Проверяет, что прямой доступ к __products невозможен."""
    cat = Category("Test", "Desc", [])
    with pytest.raises(AttributeError):
        cat.__products
    # Однако доступ через name mangling возможен, но это не должно поощряться
    # Проверяем, что атрибут существует под "искажённым" именем
    assert hasattr(cat, "_Category__products")


def test_add_product_updates_products_property(sample_category):
    """Проверяет, что после добавления продукта свойство products обновляется."""
    cat = sample_category
    new_product = Product("Product3", 'description3', 300, 7)
    cat.add_product(new_product)
    expected = "\nProduct1, 5 Остаток: 50\nProduct2, 200 Остаток: 150\nProduct3, 300 Остаток: 7"
    assert cat.products == expected
