from typing import List
from .schemas import Category, Product

# In-memory categories and products.
# Later we will replace this with a real database (SQLite) in A10.

CATEGORIES: List[Category] = [
    Category(id=1, name="Vegetables", description="Fresh vegetables"),
    Category(id=2, name="Fruits", description="Seasonal and imported fruits"),
    Category(id=3, name="Dairy & Eggs", description="Milk, curd, paneer, eggs, etc."),
    Category(id=4, name="Staples & Grains", description="Rice, wheat, pulses, oils"),
    Category(id=5, name="Snacks & Beverages", description="Chips, biscuits, tea, coffee, juices"),
]

PRODUCTS: List[Product] = [
    # Vegetables (category_id = 1)
    Product(id=101, name="Tomato", category_id=1, price=40.0, unit="kg", brand=None, description="Fresh red tomatoes"),
    Product(id=102, name="Potato", category_id=1, price=30.0, unit="kg", brand=None, description="Regular potatoes"),
    Product(id=103, name="Onion", category_id=1, price=35.0, unit="kg", brand=None, description="Red onions"),
    Product(id=104, name="Cucumber", category_id=1, price=50.0, unit="kg", brand=None, description="Green cucumbers"),

    # Fruits (category_id = 2)
    Product(id=201, name="Banana (Dozen)", category_id=2, price=60.0, unit="dozen", brand=None, description="Fresh ripe bananas"),
    Product(id=202, name="Apple (Kashmiri)", category_id=2, price=180.0, unit="kg", brand=None, description="Kashmiri apples"),
    Product(id=203, name="Orange", category_id=2, price=120.0, unit="kg", brand=None, description="Juicy oranges"),
    Product(id=204, name="Grapes (Seedless)", category_id=2, price=150.0, unit="kg", brand=None, description="Green seedless grapes"),

    # Dairy & Eggs (category_id = 3)
    Product(id=301, name="Toned Milk 1L", category_id=3, price=60.0, unit="L", brand="Amul", description="Toned milk, 1 litre pack"),
    Product(id=302, name="Curd 500g", category_id=3, price=45.0, unit="g", brand="Mother Dairy", description="Fresh dahi 500g"),
    Product(id=303, name="Paneer 200g", category_id=3, price=85.0, unit="g", brand="Amul", description="Paneer block 200g"),
    Product(id=304, name="Eggs (6 pack)", category_id=3, price=55.0, unit="pack", brand=None, description="Pack of 6 eggs"),

    # Staples & Grains (category_id = 4)
    Product(id=401, name="Basmati Rice 5kg", category_id=4, price=650.0, unit="pack", brand="India Gate", description="5kg basmati rice"),
    Product(id=402, name="Wheat Flour 5kg", category_id=4, price=280.0, unit="pack", brand="Aashirvaad", description="5kg atta"),
    Product(id=403, name="Toor Dal 1kg", category_id=4, price=160.0, unit="kg", brand=None, description="Toor/Arhar dal"),
    Product(id=404, name="Sunflower Oil 1L", category_id=4, price=160.0, unit="L", brand="Fortune", description="Refined sunflower oil 1L"),

    # Snacks & Beverages (category_id = 5)
    Product(id=501, name="Potato Chips 100g", category_id=5, price=30.0, unit="g", brand="Lays", description="Classic salted chips"),
    Product(id=502, name="Marie Biscuits 200g", category_id=5, price=40.0, unit="g", brand="Britannia", description="Marie biscuits"),
    Product(id=503, name="Tea 250g", category_id=5, price=120.0, unit="g", brand="Tata Tea", description="Tea powder 250g"),
    Product(id=504, name="Instant Coffee 50g", category_id=5, price=180.0, unit="g", brand="Nescafe", description="Instant coffee jar"),
]


def get_all_categories() -> List[Category]:
    return CATEGORIES


def get_all_products() -> List[Product]:
    return PRODUCTS


def get_products_by_category(category_id: int) -> List[Product]:
    return [p for p in PRODUCTS if p.category_id == category_id]


def get_product_by_id(product_id: int) -> Product | None:
    for p in PRODUCTS:
        if p.id == product_id:
            return p
    return None
