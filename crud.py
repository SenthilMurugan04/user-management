
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import User
from schemas import UserCreate, UserUpdate


# Create a user
def create_user(db: Session, user_data: UserCreate):
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        city=user_data.city,
        is_active=user_data.is_active
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get all users, with optional filters
def get_users(db: Session, city=None, is_active=None):
    query = db.query(User)

    if city is not None:
        query = query.filter(User.city.ilike(city))

    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    return query.order_by(User.id).all()


# Get a user by ID
def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# Update a user
def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):
    user = get_user_by_id(db, user_id)

    existing_user = db.query(User).filter(
        User.email == user_data.email,
        User.id != user_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user.name = user_data.name
    user.email = user_data.email
    user.age = user_data.age
    user.city = user_data.city
    user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)

    return user


# Delete a user
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}
