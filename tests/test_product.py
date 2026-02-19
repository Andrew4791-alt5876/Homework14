from typing import Any


def test_product_init(product: Any) -> None:
    '''Тесты для инициализации атрибутов класса Product.'''
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8
