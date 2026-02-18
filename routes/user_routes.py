from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas.user_schema import UserSchema
from repositories import user_repo

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return user_repo.create_user(db, user.name, user.email)

@router.get("/", response_model=list[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)

@router.get("/{user_id}", response_model=UserSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
