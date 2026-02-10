from fastapi import FastAPI, Depends, Path, HTTPException
from db.database import engine, SessionLocal
from db.base_class import Base
from typing import Annotated, List
from sqlalchemy.orm import Session
from models import Patient, Therapist, Patient_Therapist_Association
from schemas import TherapistCreate, TherapistRead, PatientCreate, PatientTherapistLink, PatientRead
from routers import home, therapists, patients, designations

def create_tables():         
	Base.metadata.create_all(bind=engine)
        
def start_application():
    app = FastAPI()
    create_tables()
    return app

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app = start_application()

# db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(home.router)
app.include_router(patients.router)
app.include_router(therapists.router)
app.include_router(designations.router)






