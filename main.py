from fastapi import FastAPI

from database import Base, engine

from routes.auth import router as auth_router
from routes.camps import router as camps_router
from routes.victims import router as victims_router
from routes.resources import router as resources_router
from routes.volunteers import router as volunteers_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Disaster Relief & Emergency Resource Management System"
)

app.include_router(auth_router)
app.include_router(camps_router)
app.include_router(victims_router)
app.include_router(resources_router)
app.include_router(volunteers_router)


@app.get("/")
def home():
    return {
        "message": "Disaster Relief & Emergency Resource Management System API"
    }
