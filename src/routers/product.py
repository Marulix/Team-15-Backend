from src.schemas.product import ProductResponse, ProductCreate
import src.services.product as service
from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {
        "detail": "Not found"
    }},
)


@router.put("/add-categories", response_model=ProductResponse, status_code=200)
def add_categories_to_product(product: ProductCreate):
    return service.get_product_with_categories(product)
