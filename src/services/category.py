from src.models.category import ProductCategory


def get_categories() -> list[str]:
    return [category.value for category in ProductCategory]
