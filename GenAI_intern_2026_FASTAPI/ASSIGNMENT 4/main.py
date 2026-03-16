"""
FastAPI - Day 5 Cart System Practice
Assignment 4 - Shopping Cart System

Submitted by: Githendran
Date: February 2026
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="E-commerce Cart System API", version="4.0.0")

# ─── Product Database ───────────────────────────────────────────────
products = [
    {"id": 1, "name": "Wireless Mouse",     "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook",           "price": 99,  "category": "Stationery",  "in_stock": True},
    {"id": 3, "name": "USB Hub",            "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set",            "price": 49,  "category": "Stationery",  "in_stock": True},
]

# ─── Cart & Orders (reset on server restart) ────────────────────────
cart   = []   # list of cart items
orders = []   # list of placed orders
order_id_counter = 1


# ─── Pydantic Models ────────────────────────────────────────────────
class CheckoutRequest(BaseModel):
    customer_name: str
    delivery_address: str


# ─── Root ───────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "message": "Welcome to E-commerce Cart System API",
        "assignment": "Assignment 4 - Day 5",
        "endpoints": {
            "products": "GET /products",
            "cart":     ["POST /cart/add", "GET /cart", "DELETE /cart/{product_id}"],
            "checkout": "POST /cart/checkout",
            "orders":   "GET /orders"
        }
    }


# ─── Products ───────────────────────────────────────────────────────
@app.get("/products")
def get_all_products():
    return {"products": products, "total": len(products)}


# ─── Q1: Add item to cart ────────────────────────────────────────────
@app.post("/cart/add")
def add_to_cart(product_id: int, quantity: int = 1):
    """Add a product to the cart or update quantity if already exists"""

    # Find product
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")

    # Q3: Reject out-of-stock products
    if not product["in_stock"]:
        raise HTTPException(status_code=400, detail=f"{product['name']} is out of stock")

    # Q4: If already in cart, update quantity
    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            item["subtotal"] = item["unit_price"] * item["quantity"]
            return {
                "message": "Cart updated",
                "cart_item": item
            }

    # New item — add to cart
    cart_item = {
        "product_id":   product_id,
        "product_name": product["name"],
        "quantity":     quantity,
        "unit_price":   product["price"],
        "subtotal":     product["price"] * quantity
    }
    cart.append(cart_item)

    return {
        "message": "Added to cart",
        "cart_item": cart_item
    }


# ─── Q2: View cart ───────────────────────────────────────────────────
@app.get("/cart")
def view_cart():
    """View all items in the cart with grand total"""
    if not cart:
        return {"message": "Cart is empty"}

    grand_total = sum(item["subtotal"] for item in cart)

    return {
        "items":       cart,
        "item_count":  len(cart),
        "grand_total": grand_total
    }


# ─── Q5: Remove item from cart ───────────────────────────────────────
@app.delete("/cart/{product_id}")
def remove_from_cart(product_id: int):
    """Remove a product from the cart"""
    for i, item in enumerate(cart):
        if item["product_id"] == product_id:
            removed = cart.pop(i)
            return {
                "message": f"'{removed['product_name']}' removed from cart",
                "removed_item": removed
            }

    raise HTTPException(status_code=404, detail="Product not found in cart")


# ─── Q5 + Bonus: Checkout ────────────────────────────────────────────
@app.post("/cart/checkout")
def checkout(request: CheckoutRequest):
    """Checkout all items in the cart and place orders"""
    global order_id_counter

    # Bonus: Reject empty cart checkout
    if not cart:
        raise HTTPException(status_code=400, detail="CART_EMPTY: Cannot checkout with an empty cart")

    placed_orders = []

    # Create one order per cart item
    for item in cart:
        order = {
            "order_id":        order_id_counter,
            "customer_name":   request.customer_name,
            "delivery_address": request.delivery_address,
            "product":         item["product_name"],
            "quantity":        item["quantity"],
            "unit_price":      item["unit_price"],
            "subtotal":        item["subtotal"]
        }
        orders.append(order)
        placed_orders.append(order)
        order_id_counter += 1

    grand_total = sum(o["subtotal"] for o in placed_orders)

    # Clear cart after checkout
    cart.clear()

    return {
        "message":      "Checkout successful!",
        "customer_name": request.customer_name,
        "orders_placed": placed_orders,
        "grand_total":  grand_total
    }


# ─── Q5: View all orders ─────────────────────────────────────────────
@app.get("/orders")
def get_orders():
    """View all placed orders"""
    if not orders:
        return {"message": "No orders placed yet"}

    return {
        "orders":       orders,
        "total_orders": len(orders)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
