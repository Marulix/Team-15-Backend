from src.schemas.product import ProductResponse, ProductCreate
import src.services.product as service
from fastapi import APIRouter


router = APIRouter(
    prefix="/products",
    tags=["categories"],
    responses={404: {"detail": "Not found"}},
)


@router.put("/", response_model=ProductResponse, status_code=200)
def product_categories(product: ProductCreate):
    return service.get_product_with_categories(product)
