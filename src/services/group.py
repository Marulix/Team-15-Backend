from src.models.group import PRODUCT_GROUPS


def get_group_categories(group: str) -> list[str]:
    return PRODUCT_GROUPS[group]


def get_groups() -> list[str]:
    return list(PRODUCT_GROUPS.keys())
