from fastapi import APIRouter, Path, HTTPException
from typing import List
from models import Patient, Therapist, Patient_Therapist_Association
from schemas import PatientTherapistLink
from dependencies import db_dependency

router = APIRouter(prefix="/designations", tags=["Designations"])

@router.post("/")
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