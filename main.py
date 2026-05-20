from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.auth import router as auth_router
from app.api.category import router as category_router
from app.api.product import router as product_router
from app.api.inventory import router as inventory_router
from app.api.supplier import router as supplier_router
from app.api.customer import router as customer_router
from app.api.reports import router as report_router
 
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management System",
    description="Professional Inventory API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(supplier_router)
app.include_router(customer_router)
app.include_router(report_router)

@app.get("/")
def home():
    return {"message": "Inventory Management System is running!"}