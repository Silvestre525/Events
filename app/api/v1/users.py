from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas.user import UserCreate, UserOut
from ...services import user_services
from ...core.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(db, user)