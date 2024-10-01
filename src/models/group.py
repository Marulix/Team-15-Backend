from src.models.category import ProductCategory
from enum import Enum


class Group(Enum):
    STUDY = "Study"
    TECHNOLOGY = "Tech"
    CREATIVE = "Creative"
    OTHERS = "Others"
    LAB = "Lab"
    PERSONAL = "Personal"


PRODUCT_GROUPS = {
    Group.STUDY.value: [
        ProductCategory.TEXTBOOKS.value,
        ProductCategory.STUDY_GUIDES.value,
        ProductCategory.NOTEBOOKS.value,
        ProductCategory.CALCULATORS.value,
        ProductCategory.LAB_MATERIALS.value
    ],
    Group.TECHNOLOGY.value: [
        ProductCategory.ELECTRONICS.value,
        ProductCategory.LAPTOPS_TABLETS.value,
        ProductCategory.CHARGERS.value,
        ProductCategory.CALCULATORS.value,
        ProductCategory.THREE_D_PRINTING.value,
        ProductCategory.ROBOTIC_KITS.value
    ],
    Group.CREATIVE.value: [
        ProductCategory.ART_DESIGN.value,
        ProductCategory.THREE_D_PRINTING.value,
        ProductCategory.MUSICAL_INSTRUMENTS.value
    ],
    Group.OTHERS.value: [
        ProductCategory.SPORTS.value,
        ProductCategory.MUSICAL_INSTRUMENTS.value,
        ProductCategory.UNIFORMS.value
    ],
    Group.LAB.value: [
        ProductCategory.LAB_MATERIALS.value,
        ProductCategory.ROBOTIC_KITS.value,
        ProductCategory.THREE_D_PRINTING.value,
        ProductCategory.CALCULATORS.value
    ],
    Group.PERSONAL.value: [
        ProductCategory.UNIFORMS.value,
        ProductCategory.CHARGERS.value,
        ProductCategory.LAPTOPS_TABLETS.value
    ]
}
