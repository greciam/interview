from fastapi import FastAPI
from db.database import engine, Base
from routers import home, therapists, patients, designations


def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI()
    create_tables()
    return app

app = start_application()

app.include_router(home.router)
app.include_router(patients.router)
app.include_router(therapists.router)
app.include_router(designations.router)
