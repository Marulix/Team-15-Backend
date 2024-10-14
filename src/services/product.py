from src.schemas.product import ProductCreate, ProductResponse
from src.services.category import ProductCategory
from random import choice, randint
import openai
from src.config.settings import Settings
from typing import List

openai.api_key = Settings().OPENAI_API_KEY


def get_product_with_categories(product: ProductCreate) -> ProductResponse:
    return ProductResponse(
        **product.model_dump(), categories=_get_product_categories(product)
    )


def _get_product_categories(product: ProductCreate) -> List[str]:
    # Extract all possible categories from the ProductCategory enum
    possible_categories: List[str] = list(ProductCategory.__members__)
    # Construct the prompt
    prompt: str = (
        f"Classify the following product offered in a students marketplace based on its name and description:\n"
        f"Product Name: {product.name}\n"
        f"Description: {product.description}\n"
        f"\nChoose from the following possible categories: {', '.join(possible_categories)}.\n"
        f"Respond with a comma-separated list of 2 to 4 categories, strictly matching the options provided. You have to choose from the categories provided."
        f"This is because this is used in a students marketplace and we need to ensure that the product is classified correctly.\n"
        f"If there are no matching categories, please respond with 'LAB_MATERIALS' "
    )

    # Call the OpenAI API to classify the product
    completion = openai.chat.completions.create(
        model="gpt-4o-mini",  # Use "gpt-4" if required
        messages=[
            {"role": "system", "content": "You are an expert product classifier."},
            {"role": "user", "content": prompt},
        ],
    )

    # Split the categories by comma
    categories: List[str] = completion.choices[0].message.content.strip().split(", ")
    # Validate the categories
    valid_categories: List[str] = [
        category for category in categories if category in possible_categories
    ]

    return valid_categories
