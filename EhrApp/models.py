from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Patient_Therapist_Association(Base):
    __tablename__ = "patient_therapist"
    patient_id = Column(ForeignKey("patient.id"), primary_key=True)
    therapist_id = Column(ForeignKey("therapist.id"), primary_key=True)
    __table_args__ = ((UniqueConstraint("patient_id", "therapist_id", name="patient_therapist_constraint")),)

class Therapist(Base):
    __tablename__ = "therapist"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    active = Column(Boolean, index=True, default=True)
    patients = relationship("Patient", secondary="patient_therapist", back_populates="therapists")

class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    therapists = relationship("Therapist", secondary="patient_therapist", back_populates="patients")
    
class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    