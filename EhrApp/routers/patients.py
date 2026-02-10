from fastapi import APIRouter, Path, HTTPException
from typing import List
from models import Patient
from schemas import PatientRead, PatientCreate
from dependencies import db_dependency


router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get("/", response_model=List[PatientRead])
def get_patients(db: db_dependency):
     return db.query(Patient).all()

@router.get("/{patient_id}/", response_model=PatientRead)
def get_patients_by_id(db: db_dependency, patient_id: int = Path(gt=0)):
     db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
     if db_patient is not None:
          return db_patient
     raise HTTPException(status_code=404, detail="Patient not found")

@router.post("/")
def create_patient(db: db_dependency, patient: PatientCreate):
     db_patient = Patient(**patient.model_dump())
     db.add(db_patient)
     db.commit()
     db.refresh(db_patient)
     return db_patient