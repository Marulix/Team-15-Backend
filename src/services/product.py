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

    prompt: str = (
        f"Classify the following product offered in a students marketplace based on its name and description:\n"
        f"Product Name: {product.name}\n"
        f"Description: {product.description}\n"
        f"\nChoose from the following possible categories: {', '.join(possible_categories)}.\n"
        f"Respond with a comma-separated list of 1 to 3 categories, strictly matching the options provided."
    )

    # Call the OpenAI API to classify the product
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change to "gpt-4" if needed
        messages=[
            {"role": "system", "content": "You are an expert product classifier."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
        max_tokens=50,
    )

    # Extract the categories from the model's response
    categories: List[str] = response.choices[0].message["content"].strip().split(", ")

    valid_categories: List[str] = [
        cat for cat in categories if cat in possible_categories
    ]

    return valid_categories
