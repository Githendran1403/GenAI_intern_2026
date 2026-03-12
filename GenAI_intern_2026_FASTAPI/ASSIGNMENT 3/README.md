# FastAPI Assignment 3 - CRUD Operations

**Submitted by:** Githendran  
**Internship:** GenAI Intern 2026  
**Date:** February 2026

## Assignment Overview

This assignment implements complete CRUD operations (Create, Read, Update, Delete) for an E-commerce Store API using FastAPI.

## Tasks Completed

### βœ… Q1: Add 2 New Products Using POST
- Added Laptop Stand (₹1299, Electronics)
- Added Sticky Notes (₹49, Stationery)
- Duplicate name validation implemented
- Endpoint: `POST /products`
- Status: 201 Created (success), 400 Bad Request (duplicate)

### βœ… Q2: Restock the USB Hub Using PUT
- Updated USB Hub (ID 3) stock status
- Changed price from ₹799 to ₹649
- Multiple field updates in single call
- Endpoint: `PUT /products/{product_id}`
- Query params: `price`, `in_stock`

### βœ… Q3: Delete a Product and Handle Missing IDs
- Deleted Pen Set (ID 4) permanently
- 404 error handling for missing products
- Endpoint: `DELETE /products/{product_id}`
- Status: 200 OK (success), 404 Not Found (missing)

### βœ… Q4: Full CRUD Sequence - Smart Watch Lifecycle
Complete workflow:
1. POST - Add Smart Watch
2. GET - Verify addition
3. PUT - Update price
4. GET - Confirm update
5. DELETE - Remove product
6. GET - Verify deletion

### βœ… Q5: Build GET /products/audit - Inventory Summary
- Total products count
- In-stock count
- Out-of-stock product names
- Total stock value (price Γ— 10 for in-stock items)
- Most expensive product
- Endpoint: `GET /products/audit`

### βœ… BONUS: Apply Category-Wide Discount
- Apply discount to all products in a category
- Endpoint: `PUT /products/discount`
- Query params: `category`, `discount_percent` (1-99)
- Returns updated products with old and new prices

## How to Run

### 1. Install Dependencies
```bash
pip install fastapi uvicorn
```

### 2. Run the Server
```bash
cd "GenAI_intern_2026_FASTAPI/ASSIGNMENT 3"
uvicorn main:app --reload
```

Or run directly:
```bash
python main.py
```

### 3. Access the API

- **API Base URL:** http://127.0.0.1:8000
- **Swagger UI (Interactive Docs):** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/products` | Get all products |
| GET | `/products/audit` | Inventory summary |
| GET | `/products/{id}` | Get product by ID |
| POST | `/products` | Add new product |
| PUT | `/products/{id}` | Update product |
| PUT | `/products/discount` | Apply category discount |
| DELETE | `/products/{id}` | Delete product |

## Testing Checklist

### Q1 - POST Operations
- [x] POST `/products` - Laptop Stand added (ID 5, status 201)
- [x] POST `/products` - Sticky Notes added (ID 6, status 201)
- [x] POST `/products` - Duplicate "Wireless Mouse" returns 400

### Q2 - PUT Operations
- [x] PUT `/products/3?in_stock=true` - USB Hub restocked
- [x] PUT `/products/3?price=699` - Price updated
- [x] PUT `/products/3?in_stock=true&price=649` - Both fields updated
- [x] PUT `/products/99?price=100` - Returns 404

### Q3 - DELETE Operations
- [x] DELETE `/products/4` - Pen Set deleted
- [x] GET `/products` - Total reduced to 3
- [x] DELETE `/products/4` again - Returns 404
- [x] DELETE `/products/99` - Returns 404

### Q4 - Full CRUD Lifecycle
- [x] POST Smart Watch
- [x] GET to verify
- [x] PUT to update price
- [x] GET to confirm
- [x] DELETE to remove
- [x] GET to verify deletion

### Q5 - Audit Endpoint
- [x] GET `/products/audit` - Returns correct summary
- [x] Placed ABOVE `/products/{product_id}` in code

### Bonus - Discount
- [x] PUT `/products/discount?category=Electronics&discount_percent=10`
- [x] All Electronics prices reduced by 10%
- [x] Returns updated count and product details

## Example Requests

### Add Product (POST)
```json
POST /products
{
  "name": "Laptop Stand",
  "price": 1299,
  "category": "Electronics",
  "in_stock": true
}
```

### Update Product (PUT)
```
PUT /products/3?in_stock=true&price=649
```

### Delete Product (DELETE)
```
DELETE /products/4
```

### Apply Discount (PUT)
```
PUT /products/discount?category=Electronics&discount_percent=10
```

## Screenshots

All output screenshots are included in this folder:
- `Q1_Output.png` - POST operations
- `Q2_Output.png` - PUT operations
- `Q3_Output.png` - DELETE operations
- `Q4_Output.png` - Full CRUD lifecycle
- `Q5_Output.png` - Audit endpoint
- `Bonus_Output.png` - Category discount

## Technologies Used

- Python 3.x
- FastAPI
- Pydantic (data validation)
- Uvicorn (ASGI server)

## Key Features

- Auto-generated product IDs
- Duplicate name validation
- Multiple field updates in single request
- Comprehensive error handling (404, 400)
- Category-wide operations
- Inventory audit and analytics

## Repository Structure

```
GenAI_intern_2026_FASTAPI/
└── ASSIGNMENT 3/
    β"œβ"€β"€ main.py
    β"œβ"€β"€ README.md
    β"œβ"€β"€ requirements.txt
    β"œβ"€β"€ Q1_Output.png
    β"œβ"€β"€ Q2_Output.png
    β"œβ"€β"€ Q3_Output.png
    β"œβ"€β"€ Q4_Output.png
    β"œβ"€β"€ Q5_Output.png
    └── Bonus_Output.png
```

---

**GitHub Repository:** https://github.com/Githendran1403/GenAI_intern_2026
