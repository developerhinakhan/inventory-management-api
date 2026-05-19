from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate
from app.models.customer import Customer
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = Customer(
        name=customer.name,
        phone_num=customer.phone_num,
        address=customer.address
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@router.get("/", response_model=List[CustomerResponse])
def get_all_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).filter(Customer.is_active == True).all()
    return customers

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_one_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found!")
    return customer

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer_update: CustomerUpdate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found!")
    if customer_update.name is not None:
        customer.name = customer_update.name
    if customer_update.phone_num is not None:
        customer.phone_num = customer_update.phone_num
    if customer_update.address is not None:
        customer.address = customer_update.address
    db.commit()
    db.refresh(customer)
    return customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found!")
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}