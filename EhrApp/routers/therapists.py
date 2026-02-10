from fastapi import APIRouter, Path, HTTPException
from typing import List
from models import Therapist
from schemas import TherapistRead, TherapistCreate
from dependencies import db_dependency


router = APIRouter(prefix="/therapists", tags=["Therapists"])

@router.get("/", response_model=List[TherapistRead])
def get_therapists(db: db_dependency):
     return db.query(Therapist).all()

@router.get("/{therapist_id}/", response_model=TherapistRead)
def get_therapist_by_id(db: db_dependency, therapist_id: int = Path(gt=0)):   
     db_therapist = db.query(Therapist).filter(Therapist.id == therapist_id).first()
     if db_therapist is not None:
          return db_therapist
     raise HTTPException(status_code=404, detail="Therapist not found")

@router.post("/", response_model=TherapistRead)
def create_therapist(db: db_dependency, therapist: TherapistCreate):
     db_therapist = Therapist(**therapist.model_dump())
     db.add(db_therapist)
     db.commit()
     db.refresh(db_therapist)
     return db_therapist