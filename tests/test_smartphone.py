from src.product import Product
from src.smartphone import Smartphone


def test_smartphone_initialization(sample_phone: Smartphone) -> None:
    """Проверка корректности инициализации всех атрибутов."""
    assert sample_phone.name == "iPhone 15"
    assert sample_phone.description == "Смартфон Apple"
    assert sample_phone.price == 100000
    assert sample_phone.quantity == 5
    assert sample_phone.efficiency == 95.5
    assert sample_phone.model == "15 Pro"
    assert sample_phone.memory == 256
    assert sample_phone.color == "черный"


def test_smartphone_inheritance(sample_phone: Smartphone) -> None:
    """Проверка, что Smartphone наследуется от Product."""
    assert isinstance(sample_phone, Product)
