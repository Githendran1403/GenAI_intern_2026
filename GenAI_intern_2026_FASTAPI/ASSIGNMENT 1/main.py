"""
FastAPI - Day 1 Practice Tasks
Assignment 1 - Complete Solutions

Submitted by: Githendran
Date: February 2026
"""

from fastapi import FastAPI

app = FastAPI(title="My E-commerce Store API", version="1.0.0")

# Product Database
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Keyboard", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Notebook", "price": 120, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": False},
    # Q1: Added 3 new products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]


# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to My E-commerce Store API",
        "endpoints": {
            "products": "/products",
            "category_filter": "/products/category/{category_name}",
            "in_stock": "/products/instock",
            "store_summary": "/store/summary",
            "search": "/products/search/{keyword}",
            "deals": "/products/deals"
        }
    }


# Q1: Get all products (now returns 7 products)
@app.get("/products")
def get_all_products():
    """Get all products with total count"""
    return {
        "products": products,
        "total": len(products)
    }


# Q2: Filter products by category
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    """Filter products by category name"""
    result = [p for p in products if p["category"] == category_name]
    
    if not result:
        return {"error": "No products found in this category"}
    
    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }


# Q3: Get only in-stock products
@app.get("/products/instock")
def get_instock():
    """Return only products that are in stock"""
    available = [p for p in products if p["in_stock"] == True]
    
    return {
        "in_stock_products": available,
        "count": len(available)
    }


# Q4: Store summary endpoint
@app.get("/store/summary")
def store_summary():
    """Get complete store summary with statistics"""
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))
    
    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }


# Q5: Search products by keyword (case-insensitive)
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    """Search products by name (case-insensitive)"""
    results = [
        p for p in products 
        if keyword.lower() in p["name"].lower()
    ]
    
    if not results:
        return {"message": "No products matched your search"}
    
    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }


# BONUS: Get cheapest and most expensive products
@app.get("/products/deals")
def get_deals():
    """Get best deal (cheapest) and premium pick (most expensive)"""
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])
    
    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }


# Additional endpoint: Get product by ID
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    """Get a specific product by ID"""
    for product in products:
        if product["id"] == product_id:
            return product
    
    return {"error": "Product not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
