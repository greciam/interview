from fastapi import APIRouter

router = APIRouter(tags=["Home"])

@router.get("/")
def home():
     return {"message": "Welcome to the Interview Project"}
