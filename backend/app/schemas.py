from typing import List, Optional
from pydantic import BaseModel


# ---------- Category ----------

class Category(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# ---------- Product ----------

class Product(BaseModel):
    id: int
    name: str
    category_id: int
    price: float
    unit: str = "pcs"  # e.g. "kg", "g", "L", "ml", "pcs"
    is_available: bool = True
    brand: Optional[str] = None
    description: Optional[str] = None


# ---------- Cart Item ----------

class CartItem(BaseModel):
    product_id: int
    quantity: float = 1
    unit: str = "pcs"  # should usually match product.unit

class CartRemoveRequest(BaseModel):
    product_id: int


# ---------- Grocery List ----------

class GroceryList(BaseModel):
    id: int
    name: str
    items: List[CartItem]
