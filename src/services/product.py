from src.schemas.product import ProductCreate, ProductResponse
from src.services.category import get_categories
import openai
from src.config.settings import Settings

openai.api_key = Settings().OPENAI_API_KEY


def get_product_with_categories(product: ProductCreate) -> ProductResponse:
    return ProductResponse(
        **product.model_dump(), categories=_get_product_categories(product)
    )


def _get_product_categories(product: ProductCreate) -> list[str]:
    possible_categories: list[str] = get_categories()
    prompt: str = (
        f"Classify the following product offered in a students marketplace based on its name and description:\n"
        f"Product Name: {product.name}\n"
        f"Description: {product.description}\n"
        f"\nChoose from the following possible categories: {', '.join(iter(map(lambda x: f'{x}', possible_categories)))}.\n"
        f"Respond with a comma-separated list of 2 to 4 categories, strictly matching the options provided, without changing spelling or format. You have to choose from the categories provided."
        f"This is because this is used in a students marketplace and we need to ensure that the product is classified correctly. Remember to only choose from the options provided\n"
        f"If there are no matching categories, please respond with exactly 'LAB MATERIALS' "
    )

    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert product classifier."},
            {"role": "user", "content": prompt},
        ],
    )

    categories: list[str] = completion.choices[0].message.content.strip().split(", ")
    valid_categories: list[str] = [
        category for category in categories if category in possible_categories
    ]

    return valid_categories
