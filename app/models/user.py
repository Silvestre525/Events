from sqlalchemy import Column, Integer, String
from ..core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    email = Column(String(50),nullable=False, index=True)
    password = Column(String(50),nullable=False, index=True)
    
    role = relationship('Role', back_populates='users')

    