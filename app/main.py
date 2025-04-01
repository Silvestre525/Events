from fastapi import FastAPI
from .api.v1 import users, auth, events  # Asegúrate de que events.py existe en api/v1/
from .core.database import Base, engine

# Crear tablas (solo para desarrollo, en producción usa migraciones)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Eventos",
    description="API para gestión de eventos",
    version="1.0.0"
)

# Incluye los routers con prefijos y tags organizados
app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Autenticación"]
)

app.include_router(
    users.router,
    prefix="/api/v1/users",
    tags=["Usuarios"]
)

app.include_router(
    events.router,  # Asumiendo que events.py sigue la estructura que te mostré
    prefix="/api/v1/events",
    tags=["Eventos"]
)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Bienvenido a la API de Eventos"}