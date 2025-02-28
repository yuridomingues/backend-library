from src.database import SessionLocal
from src.models import User
from src.auth.exceptions import UserNotFound, InvalidCredentials

def authenticate(username: str, password: str):
    """
    Authenticates a user by their username and password.
    """
    with SessionLocal() as db:
        user = db.query(User).filter(User.username == username).first()
        if not user or not user.check_password(password):
            raise InvalidCredentials
        return user

def get_all_users(user_id: int):
    """
    Retrieves a user by their ID.
    """
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound
        return user
