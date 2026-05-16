from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from app.core.database import engine,Base,get_db
from app.api.auth import router
from app.schemas.category import CategoryCreate,CategoryResponse
from app.models.category import Category
from typing import List

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


@app.post("/categories",response_model=CategoryResponse)
def create_category(category:CategoryCreate,db:Session=Depends(get_db)):
    new_category= Category(name=category.name)
    db.add(new_category)
    db.commit()    
    db.refresh(new_category)
    return new_category

@app.get("/categories",response_model=List[CategoryResponse])
def get_category(db:Session=Depends(get_db)):
    category= db.query(Category).filter(Category.is_active==True).all()
    return category

@app.get("/category/{category_id}",response_model=CategoryResponse)
def get_one_category(category_id:int,db:Session=Depends(get_db)):
    category= db.query(Category).filter(Category.id==category_id).first()
    if not category:
        raise HTTPException(status_code=404,detail="Category not found!")
    return category

@app.put("/category/{category_id},",response_model=CategoryResponse)
def update_category(category_id: int,category_update:CategoryCreate,db:Session=Depends(get_db)):
    category= db.query(Category).filter(Category.id==category_id).first()
    if not category:
        raise HTTPException(status_code=404,detail="Category not found")
    category.name= category_update.name
    db.commit()
    db.refresh(category)
    return category

@app.delete("/category/{category_id}",status_code=status.HTTP_200_OK)
def del_one_category(category_id:int,db:Session=Depends(get_db)):
    category= db.query(Category).filter(Category.id==category_id).first()
    if not category:
        raise HTTPException(status_code=404,detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message":"Category deleted succesfully"}