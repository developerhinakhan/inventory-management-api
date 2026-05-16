from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.auth import router as auth_router
from app.api.category import router as category_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management System",
    description="Professional Inventory API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(category_router)

@app.get("/")
def home():
    return {"message": "Inventory Management System is running!"}