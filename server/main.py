from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, Column, Integer, LargeBinary, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid 
import bcrypt
app = FastAPI()

DATABASE_URL = "postgresql://musicapp_user:musicapp_password@localhost:5432/musicapp"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

db=SessionLocal()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

@app.post('/signup')
def signup_user(user: UserCreate):
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

Base.metadata.create_all(bind=engine)

