from pydantic import BaseModel
from typing import List
from schemas import TherapistResponse

class PatientBase(BaseModel):
    first_name: str
    last_name: str

class PatientResponse(PatientBase):
    id: int
    class Config:
        from_attributes = True

class PatientCreate(PatientBase):
    pass 

class PatientRead(PatientResponse):
    therapists: List[TherapistResponse]