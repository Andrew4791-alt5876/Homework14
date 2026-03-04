from src.lawngrass import LawnGrass
from src.product import Product


def test_lawn_grass_initialization(sample_grass: LawnGrass) -> None:
    """Проверка корректности инициализации всех атрибутов."""
    assert sample_grass.name == "Изумрудная лужайка"
    assert sample_grass.description == "Газонная трава для сада"
    assert sample_grass.price == 1500
    assert sample_grass.quantity == 20
    assert sample_grass.country == "Россия"
    assert sample_grass.germination_period == "10-14 дней"
    assert sample_grass.color == "зеленый"


def test_lawn_grass_inheritance(sample_grass: LawnGrass) -> None:
    """Проверка, что LawnGrass наследуется от Product."""
    assert isinstance(sample_grass, Product)
