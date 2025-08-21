from fastapi import Depends, HTTPException
from models.user import User
from pydantic_schema.user_create import UserCreate
import uuid 
import bcrypt
from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post('/signup')
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