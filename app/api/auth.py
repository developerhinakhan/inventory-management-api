from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate,UserResponse
from app.services.auth_service import hash_password,verify_password
from app.core.security import create_access_token

router= APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user:UserCreate, db:Session=Depends(get_db)):
    existing_user= db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "Email already exists"
        )
    hashed= hash_password(user.password)
    new_user= User(
        name=user.name,
        email=user.email,
        role=user.role,
        password= hashed
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(user:UserCreate,db:Session=Depends(get_db)):
    db_user= db.query(User).filter(User.email==user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
        
    if not verify_password(user.password,db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong password!"
        )
    
    token= create_access_token({"sub":db_user.email,"role": db_user.role })
    return{"access_token": token,"token_type": "bearer"}
         
        
    