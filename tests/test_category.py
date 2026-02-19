from src.category import Category


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор"
    assert len(first_category.products) == 3
    assert len(second_category.products) == 1
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 4
    assert second_category.product_count == 4

def test_category_products_default_to_empty_list():
    """Проверка, что при отсутствии аргумента products создаётся пустой список."""
    category = Category("Категория", "Описание")
    assert category.products == []

def test_category_products_passed_as_none():
    """Проверка, что при явной передаче None создаётся пустой список."""
    category = Category("Категория", "Описание", None)
    assert category.products == []
