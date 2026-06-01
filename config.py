BASE_URL = "https://stellarburgers.education-services.ru"

IMPLICIT_WAIT = 3
EXPLICIT_WAIT = 25

INGREDIENTS = [
    {
        "id": "61c0c5a71d1f82001bdaaa6d",
        "name": "Флюоресцентная булка R2-D3",
        "slug": "bun",
    },
    {
        "id": "61c0c5a71d1f82001bdaaa72",
        "name": "Соус Spicy-X",
        "slug": "sauce",
    },
    {
        "id": "61c0c5a71d1f82001bdaaa6f",
        "name": "Мясо бессмертных моллюсков Protostomia",
        "slug": "main",
    },
]

ORDER_INGREDIENT_IDS = [ingredient["id"] for ingredient in INGREDIENTS]
