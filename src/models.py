from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from src.database import engine


Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)


def create_tables():
    Base.metadata.create_all(engine)
