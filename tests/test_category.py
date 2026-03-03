from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(
    category_with_products: Category, product1: Product, product2: Product
) -> None:
    """Проверка инициализации атрибутов категории."""
    assert category_with_products.name == "Электроника"
    assert category_with_products.description == "Разные товары"
    # Проверяем, что приватный список не доступен напрямую
    with pytest.raises(AttributeError):
        _ = category_with_products.__products
    # Проверяем содержимое через свойство products
    products_str = category_with_products.products
    assert str(product1) in products_str
    assert str(product2) in products_str
    assert products_str.endswith("\n")


def test_empty_category_initialization(empty_category: Category) -> None:
    """Проверка инициализации пустой категории."""
    assert empty_category.name == "Пустая"
    assert empty_category.description == "Нет товаров"
    assert empty_category.products == ""  # пустая строка


def test_category_counters_on_creation(
    category_with_products: Category,
    empty_category: Category,
    product1: Product,
    product2: Product,
) -> None:
    """Проверка увеличения счетчиков класса при создании категорий."""
    # После создания category_with_products (2 продукта)
    assert Category.category_count == 2
    assert Category.product_count == 2
    # Создаём ещё одну категорию с одним продуктом
    cat2 = Category("Одежда", "Одежда и обувь", [product1])
    assert Category.category_count == 3
    assert Category.product_count == 3  # 2 + 1
    assert isinstance(cat2, Category)
    # Пустая категория не увеличивает product_count
    empty = Category("Книги", "Ничего нет", [])
    assert Category.category_count == 4
    assert Category.product_count == 3  # осталось 3
    assert isinstance(empty, Category)


def test_add_product(
    category_with_products: Category, product3: Product
) -> None:
    """Добавление продукта в категорию."""
    initial_count = Category.product_count
    category_with_products.add_product(product3)
    # Проверяем, что product_count увеличился
    assert Category.product_count == initial_count + 1
    # Проверяем, что продукт появился в products
    assert str(product3) in category_with_products.products


def test_add_product_invalid_type(category_with_products: Any) -> None:
    """Добавление объекта не Product вызывает TypeError."""
    with pytest.raises(TypeError):
        category_with_products.add_product("не продукт")
    with pytest.raises(TypeError):
        category_with_products.add_product(123)


def test_category_str(category_with_products: Category) -> None:
    """Проверка строкового представления категории."""
    # Сумма quantity = 5 + 10 = 15
    expected = "Электроника, количество продуктов: 15 шт."
    assert str(category_with_products) == expected


def test_category_str_empty(empty_category: Category) -> None:
    """Проверка строкового представления пустой категории."""
    expected = "Пустая, количество продуктов: 0 шт."
    assert str(empty_category) == expected


def test_products_property_multiple(
    category_with_products: Category, product1: Product, product2: Product
) -> None:
    """Свойство products возвращает все продукты через перевод строки."""
    products_str = category_with_products.products
    lines = products_str.splitlines()
    # Должно быть 2 строки (по одной на продукт)
    assert len(lines) == 2
    assert lines[0] == str(product1)
    assert lines[1] == str(product2)


def test_add_product_multiple(
    category_with_products: Category,
    product1: Product,
    product2: Product,
    product3: Product,
) -> None:
    """Добавление нескольких продуктов и проверка счетчика."""
    # Уже есть 2 продукта, product_count = 2
    category_with_products.add_product(product3)
    category_with_products.add_product(product1)  # дубликат, но разрешён
    assert Category.product_count == 4  # было 2, добавили 2
    # Проверяем наличие всех продуктов в строке
    prod_str = category_with_products.products
    assert prod_str.count(str(product1)) == 2  # product1 встречается дважды
    assert str(product2) in prod_str
    assert str(product3) in prod_str


def test_product_count_with_duplicate_products(product1: Product) -> None:
    """Проверка, что один и тот же объект может быть
    в нескольких категориях."""
    cat1 = Category("Кат1", "Описание1", [product1])
    cat2 = Category("Кат2", "Описание2", [product1])
    assert (
        Category.product_count == 2
    )  # product1 учтён дважды (объект один, но ссылки разные)
    assert isinstance(cat1, Category)
    assert isinstance(cat2, Category)
