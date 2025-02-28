from fastapi import APIRouter

from src.auth.schema import UserCadaster, UserLogin

router = APIRouter()

# CRUD

@router.get("/register")
def register():
    """
    Return UserCadaster method
    """
    return UserCadaster()

@router.get("/login")
def login():
    """
    Return UserLogin method
    """
    return UserLogin()
