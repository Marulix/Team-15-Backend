from src.schemas.product import ProductCreate, ProductResponse
import src.services.category as service
import src.services.product as product_service
from fastapi import APIRouter
from random import choice, randint

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {
        "detail": "Not found"
    }},
)


@router.get("/all", response_model=list[str], status_code=200)
def get_all_categories():
    return service.get_categories()


@router.put("/product/test", response_model=list[str], status_code=200)
def test_product_categories(product: ProductCreate):
    return [
        choice([category for category in service.get_categories()])
        for _ in range(randint(1, 3))
    ]


@router.put("/product", response_model=list[str], status_code=200)
def get_product_categories(product: ProductCreate):
    product: ProductResponse = product_service.get_product_with_categories(
        product)
    return product.categories
