"""
FastAPI - Day 4 Practice Tasks
Assignment 3 - CRUD Operations (POST, PUT, DELETE)

Submitted by: Githendran
Date: February 2026
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="E-commerce Store CRUD API", version="3.0.0")

# Product Model
class Product(BaseModel):
    name: str
    price: int
    category: str
    in_stock: bool

# Initial Product Database
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
]

# Counter for auto-generating IDs
next_id = 5


# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to E-commerce Store CRUD API",
        "assignment": "Assignment 3 - Day 4",
        "endpoints": {
            "GET": ["/products", "/products/{id}", "/products/audit"],
            "POST": ["/products"],
            "PUT": ["/products/{id}", "/products/discount"],
            "DELETE": ["/products/{id}"]
        }
    }


# GET all products
@app.get("/products")
def get_all_products():
    """Get all products with total count"""
    return {
        "products": products,
        "total": len(products)
    }


# Q5: GET /products/audit - Inventory Summary (MUST be above /{product_id})
@app.get("/products/audit")
def get_audit():
    """Get complete inventory audit summary"""
    in_stock_products = [p for p in products if p["in_stock"]]
    out_of_stock_products = [p for p in products if not p["in_stock"]]
    
    # Calculate total stock value (price × 10 for in-stock items)
    total_stock_value = sum(p["price"] * 10 for p in in_stock_products)
    
    # Find most expensive product
    most_expensive = max(products, key=lambda p: p["price"]) if products else None
    
    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock_products),
        "out_of_stock_names": [p["name"] for p in out_of_stock_products],
        "total_stock_value": total_stock_value,
        "most_expensive": {
            "name": most_expensive["name"],
            "price": most_expensive["price"]
        } if most_expensive else None
    }


# BONUS: PUT /products/discount - Apply category-wide discount (MUST be above /{product_id})
@app.put("/products/discount")
def apply_discount(category: str, discount_percent: int):
    """Apply discount to all products in a category"""
    if discount_percent < 1 or discount_percent > 99:
        raise HTTPException(status_code=400, detail="Discount must be between 1 and 99")
    
    updated_products = []
    
    for product in products:
        if product["category"] == category:
            old_price = product["price"]
            new_price = int(old_price * (1 - discount_percent / 100))
            product["price"] = new_price
            updated_products.append({
                "name": product["name"],
                "old_price": old_price,
                "new_price": new_price
            })
    
    if not updated_products:
        return {
            "message": f"No products found in category '{category}'",
            "updated_count": 0
        }
    
    return {
        "message": f"{discount_percent}% discount applied to {category}",
        "updated_count": len(updated_products),
        "updated_products": updated_products
    }


# GET product by ID
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    """Get a specific product by ID"""
    for product in products:
        if product["id"] == product_id:
            return product
    
    raise HTTPException(status_code=404, detail="Product not found")


# Q1: POST - Add new product
@app.post("/products", status_code=201)
def add_product(product: Product):
    """Add a new product to the store"""
    global next_id
    
    # Check for duplicate name
    for existing_product in products:
        if existing_product["name"].lower() == product.name.lower():
            raise HTTPException(
                status_code=400, 
                detail=f"Product '{product.name}' already exists"
            )
    
    # Create new product with auto-generated ID
    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "in_stock": product.in_stock
    }
    
    products.append(new_product)
    next_id += 1
    
    return {
        "message": "Product added",
        "product": new_product
    }


# Q2: PUT - Update product
@app.put("/products/{product_id}")
def update_product(
    product_id: int, 
    price: Optional[int] = None, 
    in_stock: Optional[bool] = None,
    name: Optional[str] = None,
    category: Optional[str] = None
):
    """Update product details"""
    for product in products:
        if product["id"] == product_id:
            # Update fields if provided
            if price is not None:
                product["price"] = price
            if in_stock is not None:
                product["in_stock"] = in_stock
            if name is not None:
                product["name"] = name
            if category is not None:
                product["category"] = category
            
            return {
                "message": "Product updated",
                "product": product
            }
    
    raise HTTPException(status_code=404, detail="Product not found")


# Q3: DELETE - Remove product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Delete a product from the store"""
    for i, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(i)
            return {
                "message": f"Product '{deleted_product['name']}' deleted",
                "deleted_product": deleted_product
            }
    
    raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
