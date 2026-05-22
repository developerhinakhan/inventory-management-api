# Inventory Management System API:
A professional REST API built with FastAPI and PostgreSQL for managing inventory, suppliers, customers and generating reports.

## Tech Stack

- **Python** --- Programming language
- **FastAPI** --- Web framework
- **PostgreSQL** --- Database
- **SQLAlchemy** --- ORM
- **JWT** --- Authentication
- **Pydantic** --- Data validation

## Features

- User authentication with JWT tokens
- Role based access (Admin/Staff)
- Category management
- Product management
- Inventory tracking (Stock IN/OUT)
- Low stock alerts
- Supplier management
- Customer management
- Reports (Profit, Top Products, Low Stock)

## Installation

**1. Clone the repository**
git clone https://github.com/developerhinakhan/inventory-management-api.git
cd inventory-management-api

**2. Create virtual environment**
python -m venv myenv
source myenv/Scripts/activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Setup environment variables**
cp .env.example .env
Edit .env file with your credentials!

**5. Run the server**
uvicorn main:app --reload

**6. Open Swagger UI**
http://127.0.0.1:8000/docs


## API Endpoints

### Auth
- POST /auth/register
- POST /auth/login

### Categories
- GET /categories
- POST /categories
- GET /categories/{id}
- PUT /categories/{id}
- DELETE /categories/{id}

### Products
- GET /products
- POST /products
- GET /products/{id}
- PUT /products/{id}
- DELETE /products/{id}

### Inventory
- POST /inventories/stock-in
- POST /inventories/stock-out
- GET /inventories
- GET /inventories/{product_id}

### Suppliers
- GET /suppliers
- POST /suppliers
- GET /suppliers/{id}
- PUT /suppliers/{id}
- DELETE /suppliers/{id}

### Customers
- GET /customers
- POST /customers
- GET /customers/{id}
- PUT /customers/{id}
- DELETE /customers/{id}

### Reports
- GET /reports/low-stock
- GET /reports/total-profit
- GET /reports/top-products
- GET /reports/supplier-debts
- GET /reports/customer-debts

## Developer

**Hina Noor**
Python Backend Developer
GitHub: developerhinakhan