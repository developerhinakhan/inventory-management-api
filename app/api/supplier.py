from fastapi import HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from app.schemas.supplier import SupplierCreate,SupplierResponse,SupplierUpdate
from app.models.supplier import Supplier
from app.core.database import get_db
from typing import List

router= APIRouter(prefix="/suppliers",tags=["Suppliers"])

@router.post("/",response_model=SupplierResponse)
def create_supplier(supplier:SupplierCreate,db:Session=Depends(get_db)):
    new_supplier= Supplier(
        name=supplier.name,
        phone_num=supplier.phone_num,
        shop_name=supplier.shop_name,
        address=supplier.address
    )
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier

@router.get("/",response_model=List[SupplierResponse])
def get_all_supplier(db:Session=Depends(get_db)):
    all_supplier= db.query(Supplier).filter(Supplier.is_active==True).all()
    return all_supplier

@router.get("/{supplier_id}",response_model=SupplierResponse)
def get_one_supplier(supplier_id:int,db:Session=Depends(get_db)):
    supplier= db.query(Supplier).filter(Supplier.id==supplier_id).first()
    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found!"
        )
    return supplier

@router.put("/{supplier_id}",response_model=SupplierResponse)
def update_supplier(supplier_id:int,supplier_update:SupplierUpdate,db:Session=Depends(get_db)):
    supplier= db.query(Supplier).filter(Supplier.id==supplier_id).first()
    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found!"
        )
    if supplier_update.name is not None:
        supplier.name=supplier_update.name
    if supplier_update.phone_num is not None:
        supplier.phone_num = supplier_update.phone_num
    if supplier_update.shop_name is not None:
        supplier.shop_name = supplier_update.shop_name
    if supplier_update.address is not None:
        supplier.address = supplier_update.address
    db.commit()
    db.refresh(supplier)
    return supplier

@router.delete("/{supplier_id}")
def delete_supplier(supplier_id:int,db:Session=Depends(get_db)):
    supplier= db.query(Supplier).filter(Supplier.id==supplier_id).first()
    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found!"
        )
    db.delete(supplier)
    db.commit()
    return {"message":"Supplier deleted succesfully"}
    