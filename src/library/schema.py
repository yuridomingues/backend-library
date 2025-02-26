from typing import Optional
from pydantic import BaseModel


class BookCreate(BaseModel):
    """
    Represents a book creation request.
    """
    id: int
    title: str
    author: str
    genre: str


class BookUpdate(BaseModel):
    """
    Data for updating a book.
    """
    id: int
    title: str
    author: str
    genre: str


class BookChange(BaseModel):
    """
    Data for changing some option of the book.
    """
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
