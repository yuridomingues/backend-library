from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from src.database import engine


Base = declarative_base()

class Book(Base):
    """
    Book parameters
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)


def create_tables():
    """
    Create a simple database
    """
    Base.metadata.create_all(engine)

class User(Base):
    """
    User parameters
    """
    __table_name__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    cpf = Column(Integer, nullable=False)