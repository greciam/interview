from pydantic import BaseModel

class PatientTherapistLink(BaseModel):
    patient_id: int
    therapist_id: int