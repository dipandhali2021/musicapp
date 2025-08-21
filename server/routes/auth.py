import uuid 
import bcrypt
from models.user import User
from database import get_db
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from pydantic_schema.user_create import UserCreate
from pydantic_schema.user_login import UserLogin
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/signup',status_code=201)
def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    # check if the user already exists in the database
    user_db=db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    # add the user to the database
    user_db = User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password=bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@router.post('/login')
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.email == user.email).first()
    if  not user_db:
        raise HTTPException(400,'User with this email does not exist')
    if not bcrypt.checkpw(user.password.encode(), user_db.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return user_db
