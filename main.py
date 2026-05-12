from fastapi import FastAPI

app= FastAPI(
    title="Inventory Managment System",
    description="Professional Inventory api",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Inventory Management System is running!"}