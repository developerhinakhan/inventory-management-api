from fastapi import FastAPI
from app.core.database import engine,Base
from app.api.auth import router

Base.metadata.create_all(bind=engine)

app= FastAPI(
    title="Inventory Managment System",
    description="Professional Inventory api",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Inventory Management System is running!"}

