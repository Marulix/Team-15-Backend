from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: str
    condition: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Apple MacBook Pro",
                    "description": "Apple MacBook Pro 13-inch with M3 chip",
                    "price": "1000.00",
                    "condition": "Barely used, has a small scratch on the back",
                }
            ]
        }
    }


class ProductCreate(ProductBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Apple MacBook Pro",
                    "description": "Apple MacBook Pro 13-inch with M3 chip",
                    "price": "1000.00",
                    "condition": "Barely used, has a small scratch on the back",
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
                    "name": "Apple MacBook Pro",
                    "description": "Apple MacBook Pro 13-inch with M3 chip",
                    "price": "1000.00",
                    "condition": "Barely used, has a small scratch on the back",
                    "categories": [
                        "ELECTRONICS",
                        "LAPTOPS & TABLETS"
                    ]
                }
            ]
        }
    }
