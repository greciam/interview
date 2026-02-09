from fastapi import FastAPI, Depends, Path, HTTPException
from db.database import engine, SessionLocal
from db.base_class import Base
from typing import Annotated, List
from sqlalchemy.orm import Session
from models import Patient, Therapist, Patient_Therapist_Association
from schemas import TherapistCreate, TherapistRead, PatientCreate, PatientTherapistLink, PatientRead

def create_tables():         
	Base.metadata.create_all(bind=engine)
        
def start_application():
    app = FastAPI()
    create_tables()
    return app

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = start_application()

db_dependency = Annotated[Session, Depends(get_db)]


# Get Requests

@app.get("/")
def home():
     return {"message": "Welcome to the Interview Project"}

@app.get("/therapists/", response_model=List[TherapistRead])
def get_therapists(db: db_dependency):
     return db.query(Therapist).all()

@app.get("/therapists/{therapist_id}/", response_model=TherapistRead)
def get_therapist_by_id(db: db_dependency, therapist_id: int = Path(gt=0)):   
     db_therapist = db.query(Therapist).filter(Therapist.id == therapist_id).first()
     if db_therapist is not None:
          return db_therapist
     raise HTTPException(status_code=404, detail="Therapist not found")

@app.get("/patients/", response_model=List[PatientRead])
def get_patients(db: db_dependency):
     return db.query(Patient).all()

@app.get("/patients/{patient_id}/", response_model=PatientRead)
def get_patients_by_id(db: db_dependency, patient_id: int = Path(gt=0)):
     db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
     if db_patient is not None:
          return db_patient
     raise HTTPException(status_code=404, detail="Patient not found")


# Post Requests

@app.post("/therapist/")
def create_therapist(db: db_dependency, therapist: TherapistCreate):
     db_therapist = Therapist(**therapist.model_dump())
     db.add(db_therapist)
     db.commit()
     db.refresh(db_therapist)
     return db_therapist

@app.post("/patient/")
def create_patient(db: db_dependency, patient: PatientCreate):
     db_patient = Patient(**patient.model_dump())
     db.add(db_patient)
     db.commit()
     db.refresh(db_patient)
     return db_patient

@app.post("/designation/")
def add_therapist_to_patient(db: db_dependency, designation: PatientTherapistLink):
     db_patient = db.query(Patient).filter(Patient.id == designation.patient_id).first()
     db_therapist = db.query(Therapist).filter(Therapist.id == designation.therapist_id).first()
     if db_patient and db_therapist is not None:
          params = Patient_Therapist_Association(**designation.model_dump())
          db.add(params)
          db.commit()
          db.refresh(params)
          return params
     raise HTTPException(status_code=404, detail="Patient or Therapist not found")