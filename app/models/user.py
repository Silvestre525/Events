from sqlalchemy import Column, Integer, String, ForeignKey
from ..core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    email = Column(String(50),nullable=False, index=True)
    password = Column(String(50),nullable=False, index=True)

    # Clave foránea (obligatoria para la relación)
    role_id = Column(Integer, ForeignKey('role.id')) 
    
    role = relationship('Role', back_populates='users')

    event = relationship('Event', back_populates='user')

    
