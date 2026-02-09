from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Creates database engine and establishes connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Creates database session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Helps create ORM models
Base = declarative_base()