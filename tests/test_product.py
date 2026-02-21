from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from src.product import Product


def test_product_creation() -> None:
    """Проверка создания продукта."""
    p = Product("Ноутбук", "Игровой", 1500.0, 3)
    assert p.name == "Ноутбук"
    assert p.description == "Игровой"
    assert p.price == 1500.0
    assert p.quantity == 3


def test_new_product_classmethod() -> None:
    """Проверка создания продукта из словаря."""
    data = {"name": "Мышь", "description": "Беспроводная", "price": 25.0, "quantity": 10}
    p = Product.new_product(data)
    assert p.name == "Мышь"
    assert p.description == "Беспроводная"
    assert p.price == 25.0
    assert p.quantity == 10


def test_price_getter(sample_product: Product) -> None:
    """Проверка, что геттер возвращает цену."""
    assert sample_product.price == 100.0


def test_set_higher_price(sample_product: Product) -> None:
    """Установка более высокой цены (без подтверждения)."""
    sample_product.price = 150.0
    assert sample_product.price == 150.0


def test_set_equal_price(sample_product: Product) -> None:
    """Установка той же цены (без подтверждения)."""
    sample_product.price = 100.0
    assert sample_product.price == 100.0


def test_set_lower_price_with_consent(monkeypatch: MonkeyPatch, sample_product: Product) -> None:
    """Снижение цены при согласии пользователя (ввод 'y')."""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 80.0
    assert sample_product.price == 80.0


def test_set_lower_price_without_consent(monkeypatch: MonkeyPatch, sample_product: Product) -> None:
    """Снижение цены при отказе пользователя (ввод 'n') — цена не меняется."""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 80.0
    assert sample_product.price == 100.0


def test_set_lower_price_invalid_input(monkeypatch: MonkeyPatch, sample_product: Product) -> None:
    """Снижение цены при неверном вводе (не 'y') — цена не меняется."""
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    sample_product.price = 80.0
    assert sample_product.price == 100.0


def test_set_non_positive_price(sample_product: Product, capsys: CaptureFixture[str]) -> None:
    """Попытка установить неположительную цену — цена не меняется, выводится сообщение."""
    sample_product.price = -20
    assert sample_product.price == 100.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
