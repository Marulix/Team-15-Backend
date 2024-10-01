import src.services.category as service
from fastapi import APIRouter


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=list[str], status_code=200)
def get_categories():
    return service.get_categories()
