from typing import List, Optional

from fastapi import FastAPI, Query, HTTPException

from .schemas import Category, Product, CartItem, CartRemoveRequest
from .data import (
    get_all_categories,
    get_all_products,
    get_products_by_category,
    get_product_by_id,
)

app = FastAPI()

# In-memory cart storage for this single-user app.
CART: List[CartItem] = []


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FastAPI backend is running"}


# -------------------- Categories & Products --------------------

@app.get("/categories", response_model=List[Category])
def list_categories() -> List[Category]:
    return get_all_categories()


@app.get("/products", response_model=List[Product])
def list_products(
    category_id: Optional[int] = Query(default=None),
    max_price: Optional[float] = Query(default=None),
    search: Optional[str] = Query(default=None),
    available_only: bool = Query(default=True),
) -> List[Product]:

    products = get_all_products()

    if category_id is not None:
        products = [p for p in products if p.category_id == category_id]

    if max_price is not None:
        products = [p for p in products if p.price <= max_price]

    if search:
        s = search.lower()
        products = [
            p
            for p in products
            if s in p.name.lower()
            or (p.brand is not None and s in p.brand.lower())
        ]

    if available_only:
        products = [p for p in products if p.is_available]

    return products


# -------------------- Cart Endpoints --------------------

@app.get("/cart", response_model=List[CartItem])
def get_cart() -> List[CartItem]:
    return CART


@app.post("/cart/add", response_model=List[CartItem])
def add_to_cart(item: CartItem) -> List[CartItem]:
    product = get_product_by_id(item.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Merge if already in cart
    for existing in CART:
        if existing.product_id == item.product_id and existing.unit == item.unit:
            existing.quantity += item.quantity
            break
    else:
        CART.append(item)

    return CART


@app.post("/cart/remove", response_model=List[CartItem])
def remove_from_cart(req: CartRemoveRequest) -> List[CartItem]:
    global CART
    CART = [item for item in CART if item.product_id != req.product_id]
    return CART


@app.post("/cart/clear", response_model=List[CartItem])
def clear_cart() -> List[CartItem]:
    CART.clear()
    return CART
    