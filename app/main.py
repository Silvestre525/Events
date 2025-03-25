from fastapi import FastAPI
from .api.v1 import users, auth
from .core.database import Base, engine

Base.metadata.create_all(bind=engine)  # Crea tablas (en desarrollo)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "API de Eventos"}