from src.schemas.product import ProductCreate, ProductResponse
from src.services.category import ProductCategory
from random import choice, randint


def get_product_with_categories(product: ProductCreate) -> ProductResponse:
    return ProductResponse(
        **product.model_dump(),
        categories=_get_product_categories(product)
    )


def _get_product_categories(product: ProductCreate) -> list[str]:
    # TODO: Implement classification model to obtain product categories
    categories: list[str] = ProductCategory.__members__
    return [choice([category for category in categories]) for _ in range(randint(1, 3))]
