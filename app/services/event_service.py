# app/services/event_service.py
from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate

class EventService:
    @staticmethod
    def get_event(db: Session, event_id: int):
        return db.query(Event).filter(Event.id == event_id).first()

    @staticmethod
    def get_events(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Event).offset(skip).limit(limit).all()

    @staticmethod
    def create_event(db: Session, event: EventCreate):
        db_event = Event(**event.dict())
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

    @staticmethod
    def update_event(db: Session, event_id: int, event: EventUpdate):
        db_event = db.query(Event).filter(Event.id == event_id).first()
        if not db_event:
            return None
        for key, value in event.dict(exclude_unset=True).items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
        return db_event

    @staticmethod
    def delete_event(db: Session, event_id: int):
        db_event = db.query(Event).filter(Event.id == event_id).first()
        if not db_event:
            return False
        db.delete(db_event)
        db.commit()
        return True