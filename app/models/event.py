from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..core.database import Base
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer,primary_key=True)
    title = Column(String(50), nullable=False, index=True)
    description = Column(String(255), nullable=True)
    location = Column(String(100), nullable=True)
    category = Column(String(50), nullable=True)
    date = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id')) 

    user = relationship('User', back_populates='event')