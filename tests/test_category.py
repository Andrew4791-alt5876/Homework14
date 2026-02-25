import pytest

from src.category import Category
from src.product import Product


class TestCategory:

    def test_category_initialization(
        self, category_with_products: Category, product1: Product, product2: Product, product3: Product
    ) -> None:
        """Проверка инициализации категории с продуктами."""
        assert category_with_products.name == "Смартфоны"
        assert category_with_products.description == (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        )
        # Проверяем, что приватный атрибут __products содержит переданные продукты
        # Доступ через свойство products (строковое представление) — косвенно
        products_str = category_with_products.products
        assert product1.name in products_str
        assert product2.name in products_str
        assert product3.name in products_str
        # Проверка счетчиков класса
        assert Category.category_count > 0  # точное значение зависит от порядка тестов
        assert Category.product_count >= 3  # можно проверить, что увеличилось как минимум на 3

    def test_empty_category_initialization(self, empty_category: Category) -> None:
        """Проверка создания пустой категории."""
        assert empty_category.name == "Пустая"
        assert empty_category.description == "Описание пустой категории"
        assert empty_category.products == ""  # свойство возвращает пустую строку
        # Счетчики должны быть корректны (но с учетом других тестов)
        # В изоляции можно проверить, что product_count не увеличился

    def test_add_product(self, empty_category: Category, product1: Product) -> None:
        """Проверка добавления продукта в категорию."""
        old_product_count = Category.product_count
        empty_category.add_product(product1)
        assert product1.name in empty_category.products
        assert Category.product_count == old_product_count + 1

    def test_products_property(
        self, category_with_products: Category, product1: Product, product2: Product, product3: Product
    ) -> None:
        """Проверка, что свойство products возвращает правильную строку."""
        expected_lines = [f"{product1}", f"{product2}", f"{product3}"]
        expected = "\n".join(expected_lines) + "\n"
        # Убираем лишний перевод строки в конце, если свойство его добавляет
        assert category_with_products.products == expected

    def test_str_method(self, category_with_products: Category) -> None:
        """Проверка метода __str__."""
        expected = "Смартфоны, количество продуктов: 27 шт."
        assert str(category_with_products) == expected

    def test_private_products_access(self, category_with_products: Category) -> None:
        """Проверка, что к __products нельзя обратиться напрямую."""
        with pytest.raises(AttributeError):
            _ = category_with_products.__products

    def test_category_count_increment(self) -> None:
        """Проверка увеличения счётчика категорий при создании новых экземпляров."""
        initial_count = Category.category_count
        cat1 = Category("Категория 1", "Описание 1", [])
        assert Category.category_count == initial_count + 1
        assert isinstance(cat1, Category)
        cat2 = Category("Категория 2", "Описание 2", [])
        assert Category.category_count == initial_count + 2
        assert isinstance(cat2, Category)

    def test_product_count_increment_on_creation(self, product1: Product, product2: Product) -> None:
        """Проверка увеличения счётчика продуктов при создании категории с продуктами."""
        initial_count = Category.product_count
        cat = Category("Тест", "Описание", [product1, product2])
        assert Category.product_count == initial_count + 2
        assert isinstance(cat, Category)

    def test_product_count_increment_on_add(
        self, empty_category: Category, product1: Product, product2: Product
    ) -> None:
        """Проверка увеличения счётчика продуктов при добавлении."""
        initial_count = Category.product_count
        empty_category.add_product(product1)
        assert Category.product_count == initial_count + 1
        empty_category.add_product(product2)
        assert Category.product_count == initial_count + 2
