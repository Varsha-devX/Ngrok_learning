from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas.user_schema import UserCreate, UserResponse
from repositories import user_repo

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_repo.create_user(db, user.name, user.email)

@router.get("/", response_model=list[UserResponse])
def get_all(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
