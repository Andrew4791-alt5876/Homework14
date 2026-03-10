from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_init_empty_products(reset_counts: None) -> None:
    """Тест инициализации категории без продуктов."""
    category = Category("Электроника", "Разные устройства", [])
    assert category.name == "Электроника"
    assert category.description == "Разные устройства"
    # Проверяем приватный атрибут через property
    assert category.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_init_with_products(
    reset_counts: None, sample_product: Product, another_product: Product
) -> None:
    """Тест инициализации категории с продуктами."""
    products = [sample_product, another_product]
    category = Category("Электроника", "Разные устройства", products)
    assert category.name == "Электроника"
    assert category.description == "Разные устройства"
    # Проверяем через property (должны быть строки продуктов)
    expected_products = f"{sample_product}\n{another_product}\n"
    assert category.products == expected_products
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_count_increment(reset_counts: None) -> None:
    """Проверка увеличения счетчика категорий."""
    cat1 = Category("Категория 1", "Описание 1", [])
    assert Category.category_count == 1
    cat2 = Category("Категория 2", "Описание 2", [])
    assert Category.category_count == 2
    assert isinstance(cat1, Category) is True
    assert isinstance(cat2, Category) is True


def test_product_count_increment_on_init(
    reset_counts: None, sample_product: Product
) -> None:
    """Проверка увеличения счетчика продуктов при
    создании категории с продуктами."""
    Category("Категория", "Описание", [sample_product])
    assert Category.product_count == 1
    # Добавим еще одну категорию с двумя продуктами
    p1 = Product("A", "desc", 10.0, 1)
    p2 = Product("B", "desc", 20.0, 2)
    Category("Другая", "Описание", [p1, p2])
    assert Category.product_count == 3


def test_add_product_valid(
    reset_counts: None, sample_product: Product
) -> Any:
    """Тест добавления корректного продукта."""
    category = Category("Электроника", "Описание", [])
    category.add_product(sample_product)
    # Проверяем, что продукт добавлен в список
    assert (
        sample_product in category._Category__products  # type: ignore
    )  # доступ к приватному атрибуту для теста
    assert category.products == f"{sample_product}\n"
    assert Category.product_count == 1


def test_add_product_invalid_type(reset_counts: None) -> Any:
    """Тест добавления объекта неверного типа (должен вызывать TypeError)."""
    category = Category("Электроника", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")  # type: ignore


def test_add_product_multiple(
    reset_counts: None, sample_product: Product, another_product: Product
) -> None:
    """Тест добавления нескольких продуктов и подсчет product_count."""
    category = Category("Электроника", "Описание", [])
    category.add_product(sample_product)
    category.add_product(another_product)
    assert Category.product_count == 2
    assert category.products == f"{sample_product}\n{another_product}\n"


def test_products_property_empty(reset_counts: None) -> None:
    """Проверка свойства products для пустой категории."""
    category = Category("Пустая", "Описание", [])
    assert category.products == ""


def test_products_property_with_products(
    reset_counts: None, sample_product: Product, another_product: Product
) -> None:
    """Проверка свойства products для категории с продуктами."""
    category = Category(
        "Электроника", "Описание", [sample_product, another_product]
    )
    expected = f"{sample_product}\n{another_product}\n"
    assert category.products == expected


def test_str_method(reset_counts: None) -> None:
    """Тест строкового представления категории."""
    p1 = Product("Товар1", "Описание1", 100.0, 3)
    p2 = Product("Товар2", "Описание2", 200.0, 5)
    category = Category("Категория", "Описание", [p1, p2])
    expected = "Категория, количество продуктов: 8 шт."  # 3+5=8
    assert str(category) == expected


def test_str_method_empty(reset_counts: None) -> None:
    """Тест строкового представления пустой категории."""
    category = Category("Пустая", "Описание", [])
    expected = "Пустая, количество продуктов: 0 шт."
    assert str(category) == expected


def test_middle_price_non_empty(reset_counts: None) -> None:
    """Тест среднего ценника для категории с продуктами."""
    p1 = Product("A", "desc", 100.0, 1)
    p2 = Product("B", "desc", 200.0, 2)
    p3 = Product("C", "desc", 300.0, 3)
    category = Category("Тест", "Описание", [p1, p2, p3])
    # Средняя цена = (100 + 200 + 300) / 3 = 200.0
    assert category.middle_price() == 200.0


def test_middle_price_rounding(reset_counts: None) -> None:
    """Тест округления среднего ценника до двух знаков."""
    p1 = Product("A", "desc", 100.123, 1)
    p2 = Product("B", "desc", 200.456, 2)
    category = Category("Тест", "Описание", [p1, p2])
    # (100.123 + 200.456) / 2 = 300.579 / 2 = 150.2895 -> округление до 150.29
    assert category.middle_price() == 150.29


def test_middle_price_empty(reset_counts: None) -> None:
    """Тест среднего ценника для пустой категории (должен вернуть 0.0)."""
    category = Category("Пустая", "Описание", [])
    assert category.middle_price() == 0.0


def test_private_products_accessible_only_via_property(
    reset_counts: None, sample_product: Product
) -> None:
    """Проверка, что список продуктов приватный и
    доступен только через property."""
    category = Category("Электроника", "Описание", [sample_product])
    with pytest.raises(AttributeError):
        _ = (
            category.__products
        )  # должно вызывать AttributeError из-за name mangling
    # Но можно проверить, что через property возвращается строка, а не список
    assert isinstance(category.products, str)


def test_category_count_persistent_across_instances(
    reset_counts: None,
) -> None:
    """Проверка, что category_count увеличивается с каждой новой категорией."""
    assert Category.category_count == 0
    Category("Кат1", "Описание1", [])
    assert Category.category_count == 1
    Category("Кат2", "Описание2", [])
    assert Category.category_count == 2
