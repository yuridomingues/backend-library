from fastapi import APIRouter

from src.library import service
from src.library.exceptions import BookNotFound
from src.library.schema import BookChange, BookCreate, BookUpdate

router = APIRouter()

@router.get("/books")
def get_books():
    """
    Get all books.
    """
    return service.get_all_books()

@router.get("/books/{book_id}")
def get_books_per_id(book_id: int):
    """
    Retrieves a book by its ID.
    """
    try:
        service.get_book_by_id(book_id)

    except BookNotFound:
        return {"message": "Book not found"}

@router.delete("/books/{book_id}")
def remove_books_per_id(book_id: int):
    """
    Removes a book by its id.
    """
    try:
        service.remove_books_per_id(book_id)

    except BookNotFound:
        return {"message": "Book not found"}

@router.put("/books/{book_id}")
def update_books_per_id(book_id: int, book_update: BookUpdate):
    """
    Update a book with the given book_id using the provided book_update.
    """
    try:
        service.update_books_per_id(book_id, book_update)
    except BookNotFound:
        return {"message": "Book not found"}

@router.patch("/books/{book_id}")
def patch_books_per_id(book_id: int, book_change: BookChange):
    """
    Change the details of a book based on its ID.
    """
    try:
        service.patch_books_per_id(book_id, book_change)
    except BookNotFound:
        return {"message": "Book not found"}

@router.post("/books/{book_id}")
def add_books(book_id: int, book_create: BookCreate):
    """
    Add a new book to the library
    """
    try:
        service.add_books(book_id, book_create)
    except BookNotFound:
        return {"message": "Book added successfully"}
