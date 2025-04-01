from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

# ----------------------------
# Esquema Base (compartido)
# ----------------------------
class EventBase(BaseModel):
    title: str = Field(..., max_length=100, example="Concierto de Rock")
    description: Optional[str] = Field(
        None, 
        example="Evento musical al aire libre",
        max_length=500
    )
    start_date: datetime = Field(..., example="2025-05-15T20:00:00")
    end_date: datetime = Field(..., example="2025-05-15T23:00:00")

    @validator('end_date')
    def validate_dates(cls, end_date, values):
        if 'start_date' in values and end_date <= values['start_date']:
            raise ValueError("La fecha de fin debe ser posterior a la de inicio")
        return end_date

# ----------------------------
# Creación (POST)
# ----------------------------
class EventCreate(EventBase):
    location: str = Field(..., example="Estadio Nacional")

    class Config:
        schema_extra = {
            "example": {
                "title": "Concierto de Rock",
                "description": "Evento con bandas internacionales",
                "start_date": "2025-05-15T20:00:00",
                "end_date": "2025-05-15T23:00:00",
                "location": "Estadio Nacional"
            }
        }

# ----------------------------
# Actualización (PATCH/PUT)
# ----------------------------
class EventUpdate(BaseModel):
    title: Optional[str] = Field(
        None, 
        max_length=100, 
        example="Concierto VIP"
    )
    description: Optional[str] = Field(
        None, 
        max_length=500,
        example="Evento con acceso exclusivo"
    )
    start_date: Optional[datetime] = Field(
        None, 
        example="2025-05-16T20:00:00"
    )
    end_date: Optional[datetime] = Field(
        None, 
        example="2025-05-16T23:00:00"
    )
    location: Optional[str] = Field(
        None, 
        example="Estadio Monumental"
    )

    class Config:
        schema_extra = {
            "example": {
                "title": "Concierto VIP",
                "location": "Estadio Monumental"
            }
        }

# ----------------------------
# Respuesta (GET)
# ----------------------------
class EventResponse(EventBase):
    id: int = Field(..., example=1)
    location: str = Field(..., example="Estadio Nacional")
    created_at: datetime = Field(..., example="2025-01-01T00:00:00")
    updated_at: Optional[datetime] = Field(
        None, 
        example="2025-01-02T00:00:00"
    )

    class Config:
        orm_mode = True

# ----------------------------
# Eliminación (DELETE)
# ----------------------------
class EventDeleteResponse(BaseModel):
    message: str = Field(..., example="Evento eliminado correctamente")
    id: int = Field(..., example=1)