from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.inventory import Inventory
from app.schemas.inventory import StockIn,StockOut, InventoryResponse
from app.models.product import Product
from typing import List

router = APIRouter(prefix="/inventories", tags=["Inventories"])

@router.post("/stock-in",response_model=InventoryResponse)
def stock_in(stock:StockIn,db:Session=Depends(get_db)):
    product= db.query(Product).filter(Product.id==stock.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    last_inventory= db.query(Inventory).filter(Inventory.product_id==stock.product_id).order_by(Inventory.id.desc()).first()
    current_stock= last_inventory.current_stock if last_inventory else 0
    new_stock_level= current_stock + stock.quantity
    new_inventory= Inventory(
        product_id= stock.product_id,
        quantity= stock.quantity,
        transaction_type= "IN",
        current_stock= new_stock_level
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


@router.post("/stock-out",response_model=InventoryResponse)
def stock_out(stock:StockOut, db:Session=Depends(get_db)):
    product= db.query(Product).filter(Product.id==stock.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    last_inventory= db.query(Inventory).filter(Inventory.product_id==stock.product_id).order_by(Inventory.id.desc()).first()
    current_stock= last_inventory.current_stock if last_inventory else 0
    if stock.quantity > current_stock:
        raise HTTPException(
            status_code=400,
            detail=f"Not enough stock! Available:{current_stock}"
        )
    new_stock_level= current_stock-stock.quantity
    if new_stock_level <= product.min_stock_level:
        print(f"Low stock alert {product.name} has only {new_stock_level} left!")
    new_inventory= Inventory(
        product_id= stock.product_id,
        quantity= stock.quantity,
        transaction_type= "OUT",
        current_stock= new_stock_level
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


@router.get("/",response_model=List[InventoryResponse])
def get_inventory(db:Session=Depends(get_db)):
    inventory= db.query(Inventory).all()
    return inventory


@router.get("/{product_id}",response_model=InventoryResponse)
def get_product_stock(product_id:int,db:Session=Depends(get_db)):
    inventory= db.query(Inventory).filter(Inventory.product_id==product_id).order_by(Inventory.id.desc()).first()
    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="No stock record found!"
        )
    return inventory