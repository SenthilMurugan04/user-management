
from typing import Optional

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db, Base
import models
import crud
from schemas import UserCreate, UserUpdate, UserResponse


# Create database tables automatically
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="User Management API",
    description="Beginner-friendly FastAPI project with SQLite",
    version="1.0.0"
)


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to User Management API"}


# 1. Create User
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user)


# 2. Get All Users + Bonus Filters
@app.get("/users", response_model=list[UserResponse])
def get_all_users(
    city: Optional[str] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    return crud.get_users(db, city, is_active)


# 3. Get User by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_user_by_id(db, user_id)


# 4. Update User
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_user(db, user_id, user)


# 5. Delete User
@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_user(db, user_id)
