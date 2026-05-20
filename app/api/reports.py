from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.product import Product
from app.models.inventory import Inventory
from app.models.supplier import Supplier
from app.models.customer import Customer
from typing import List

router= APIRouter(prefix="/reports",tags=["Reports"])

@router.get("/low-stock")
def get_low_stock_products(db:Session=Depends(get_db)):
    products= db.query(Product).filter(Product.is_active==True).all()
    low_stock_products=[]
    for product in products:
        last_inventory= db.query(Inventory).filter(Inventory.product_id==product.id).order_by(Inventory.id.desc()).first()
        current_stock= last_inventory.current_stock if last_inventory else 0
        if current_stock <= product.min_stock_level:
            low_stock_products.append({
                "product_id":product.id,
                "product_name":product.name,
                "current_stock":current_stock,
                "min_stock_level":product.min_stock_level
            })
    return low_stock_products
        
        
@router.get("/total-profit")
def get_total_profit(db: Session = Depends(get_db)):
    inventory_out = db.query(Inventory).filter(
        Inventory.transaction_type == "OUT"
    ).all()
    total_profit = 0
    for record in inventory_out:
        product = db.query(Product).filter(
            Product.id == record.product_id
        ).first()
        if product:
            profit_per_item = product.sale_price - product.cost_price
            total_profit += profit_per_item * record.quantity
    return {
        "total_profit": total_profit,
        "currency": "PKR"
    }
    
    
@router.get("/top-products")
def get_top_products(db:Session=Depends(get_db)):
    products= db.query(Product).filter(Product.is_active==True).all()
    product_sales=[]
    for product in products:
        total_sold= db.query(Inventory).filter(
            Inventory.product_id==product.id,
            Inventory.transaction_type=="OUT"
        ).all()
        quantity_sold= sum(record.quantity for record in total_sold)
        product_sales.append({
            "Product id": product.id,
            "Product name": product.name,
            "total_sold": quantity_sold
        })
    sorted_products=sorted(
        product_sales,
        key=lambda x:x["total_sold"],
        reverse= True
    )
    return sorted_products[:5]


@router.get("/supplier-debts")
def get_supplier_debts(db: Session = Depends(get_db)):
    suppliers = db.query(Supplier).filter(
        Supplier.is_active == True
    ).all()
    return [{"supplier_id": s.id, "supplier_name": s.name} for s in suppliers]


@router.get("/customer-debts")
def get_customer_debts(db: Session = Depends(get_db)):
    customers = db.query(Customer).filter(
        Customer.is_active == True
    ).all()
    return [{"customer_id": c.id, "customer_name": c.name} for c in customers]