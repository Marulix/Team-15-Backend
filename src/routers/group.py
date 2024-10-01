import src.services.group as service
from fastapi import APIRouter


router = APIRouter(
    prefix="/groups",
    tags=["groups"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=list[str], status_code=200)
def get_groups():
    return service.get_groups()


@router.get("/{group}", response_model=list[str], status_code=200)
def get_group_categories(group: str):
    return service.get_group_categories(group)
