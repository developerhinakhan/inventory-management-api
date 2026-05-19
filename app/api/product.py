from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from typing import List

router= APIRouter(prefix="/products", tags=["Products"])

@router.post("/",response_model=ProductResponse)
def create_product(product: ProductCreate,db:Session=Depends(get_db)):
    new_product= Product(
        name= product.name,
        description= product.description,
        sku= product.sku,
        category_id= product.category_id,
        sale_price= product.sale_price,
        cost_price= product.cost_price,
        min_stock_level= product.min_stock_level
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/",response_model=List[ProductResponse])
def get_products(db:Session=Depends(get_db)):
    products= db.query(Product).filter(Product.is_active==True).all()
    return products

@router.get("/{product_id}",response_model=ProductResponse)
def get_one_product(product_id: int,db:Session=Depends(get_db)):
    product= db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    return product

@router.put("/{product_id}",response_model=ProductResponse)
def update_product(product_id:int,product_update:ProductUpdate,db:Session=Depends(get_db)):
    product= db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    if product_update.name is not None:
        product.name = product_update.name
    if product_update.description is not None:
        product.description = product_update.description
    if product_update.sku is not None:
        product.sku = product_update.sku
    if product_update.category_id is not None:
        product.category_id = product_update.category_id
    if product_update.sale_price is not None:
        product.sale_price = product_update.sale_price
    if product_update.cost_price is not None:
        product.cost_price = product_update.cost_price
    if product_update.min_stock_level is not None:
        product.min_stock_level = product_update.min_stock_level
    db.commit()
    db.refresh(product)
    return product
    
@router.delete("/{product_id}")
def delete_product(product_id: int,db:Session=Depends(get_db)):
    product= db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message":"Product deleted succesfully"}
