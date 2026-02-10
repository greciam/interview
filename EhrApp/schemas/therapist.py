from pydantic import BaseModel
from typing import List
from schemas import PatientResponse

class TherapistBase(BaseModel):
    first_name: str
    last_name: str
    active: bool = True

class TherapistCreate(TherapistBase):
    pass

class TherapistResponse(TherapistBase):
    id: int
    class Config:
        from_attributes = True

class TherapistRead(TherapistResponse):
    patients: List[PatientResponse]

