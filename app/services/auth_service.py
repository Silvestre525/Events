from sqlalchemy.orm import Session
from ..models import User
from ..core.security import verify_password, create_access_token

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_user_token(user: User):
    return create_access_token(data={"sub": user.email})