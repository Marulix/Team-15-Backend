from pydantic import BaseModel

EXAMPLE_NAME: str = "Apple MacBook Pro"
EXAMPLE_DESCRIPTION: str = "Apple MacBook Pro 13-inch with M3 chip"
EXAMPLE_PRICE: str = "1000.00"
EXAMPLE_CONDITION: str = "Barely used, has a small scratch on the back"


class ProductBase(BaseModel):
    name: str
    description: str
    price: str
    condition: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": EXAMPLE_NAME,
                    "description": EXAMPLE_DESCRIPTION,
                    "price": EXAMPLE_PRICE,
                    "condition": EXAMPLE_CONDITION
                }
            ]
        }
    }


class ProductCreate(ProductBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": EXAMPLE_NAME,
                    "description": EXAMPLE_DESCRIPTION,
                    "price": EXAMPLE_PRICE,
                    "condition": EXAMPLE_CONDITION
                }
            ]
        }
    }


class ProductResponse(ProductBase):
    categories: list[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": EXAMPLE_NAME,
                    "description": EXAMPLE_DESCRIPTION,
                    "price": EXAMPLE_PRICE,
                    "condition": EXAMPLE_CONDITION,
                    "categories": [
                        "ELECTRONICS",
                        "LAPTOPS & TABLETS"
                    ]
                }
            ]
        }
    }
