# FastAPI Assignment 1 - E-commerce Store API

**Submitted by:** Githendran  
**Internship:** GenAI Intern 2026  
**Date:** February 2026

## Assignment Overview

This assignment implements a complete E-commerce Store API using FastAPI with 5 main tasks + 1 bonus task.

## Tasks Completed

### βœ… Q1: Add 3 More Products
- Added Laptop Stand, Mechanical Keyboard, and Webcam
- Total products now: 7
- Endpoint: `GET /products`

### βœ… Q2: Category Filter Endpoint
- Filter products by category
- Endpoint: `GET /products/category/{category_name}`
- Examples:
  - `/products/category/Electronics`
  - `/products/category/Stationery`

### βœ… Q3: Show Only In-Stock Products
- Returns only available products
- Endpoint: `GET /products/instock`
- Includes count of in-stock items

### βœ… Q4: Store Info Endpoint
- Complete store summary with statistics
- Endpoint: `GET /store/summary`
- Shows: total products, in-stock count, out-of-stock count, categories

### βœ… Q5: Search Products by Name
- Case-insensitive search
- Endpoint: `GET /products/search/{keyword}`
- Examples:
  - `/products/search/mouse`
  - `/products/search/BOOK`

### βœ… BONUS: Cheapest & Most Expensive Product
- Shows best deal and premium pick
- Endpoint: `GET /products/deals`

## How to Run

### 1. Install FastAPI and Uvicorn
```bash
pip install fastapi uvicorn
```

### 2. Run the Server
```bash
cd "GenAI_intern_2026_FASTAPI/ASSIGNMENT 1"
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
| GET | `/` | Welcome message with all endpoints |
| GET | `/products` | Get all products (total: 7) |
| GET | `/products/category/{category_name}` | Filter by category |
| GET | `/products/instock` | Get only in-stock products |
| GET | `/store/summary` | Store statistics |
| GET | `/products/search/{keyword}` | Search products |
| GET | `/products/deals` | Best deal & premium pick |
| GET | `/products/{product_id}` | Get product by ID |

## Testing Checklist

- [x] Q1 β€" `/products` returns total: 7
- [x] Q2 β€" `/products/category/Electronics` works
- [x] Q3 β€" `/products/instock` shows only available products
- [x] Q4 β€" `/store/summary` shows full store overview
- [x] Q5 β€" `/products/search/mouse` returns Wireless Mouse
- [x] Q5 β€" `/products/search/BOOK` also works (case-insensitive)
- [x] All endpoints tested in Swagger UI at `/docs`
- [x] BONUS β€" `/products/deals` returns cheapest and most expensive

## Screenshots

All output screenshots are included in this folder:
- `Q1_Output.png` - All products endpoint
- `Q2_Output.png` - Category filter
- `Q3_Output.png` - In-stock products
- `Q4_Output.png` - Store summary
- `Q5_Output.png` - Search functionality
- `Bonus_Output.png` - Deals endpoint

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn (ASGI server)

## Repository Structure

```
GenAI_intern_2026_FASTAPI/
└── ASSIGNMENT 1/
    β"œβ"€β"€ main.py
    β"œβ"€β"€ README.md
    β"œβ"€β"€ Q1_Output.png
    β"œβ"€β"€ Q2_Output.png
    β"œβ"€β"€ Q3_Output.png
    β"œβ"€β"€ Q4_Output.png
    β"œβ"€β"€ Q5_Output.png
    └── Bonus_Output.png
```

## Notes

- All endpoints are working and tested
- Code is clean, organized, and well-commented
- Case-insensitive search implemented
- Error handling included for edge cases

---

**GitHub Repository:** https://github.com/Githendran1403/GenAI_intern_2026
