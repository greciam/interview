from pydantic import BaseModel
from typing import List


class PatientTherapistLink(BaseModel):
    patient_id: int
    therapist_id: int

class TherapistBase(BaseModel):
    first_name: str
    last_name: str
    active: bool = True

class PatientBase(BaseModel):
    first_name: str
    last_name: str

class PatientResponse(PatientBase):
    id: int
    class Config:
        from_attributes = True

class TherapistResponse(TherapistBase):
    id: int
    class Config:
        from_attributes = True

class PatientCreate(PatientBase):
    pass 

class TherapistCreate(TherapistBase):
    pass

class PatientRead(PatientResponse):
    therapists: List[TherapistResponse]

class TherapistRead(TherapistResponse):
    patients: List[PatientResponse]

