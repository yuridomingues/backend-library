from sqlalchemy.orm import Session
from src.database import SessionLocal, Book
from src.library.exceptions import BookNotFound
from src.library.schema import BookChange, BookCreate, BookUpdate

def get_all_books():
    """
    Retrieves all books from the database.
    """
    with SessionLocal() as db:
        return db.query(Book).all()

def get_book_by_id(book_id: int):
    """
    Retrieves a book by its ID.
    """
    with SessionLocal() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise BookNotFound
        return book

def remove_books_per_id(book_id: int):
    """
    Removes a book by its ID.
    """
    with SessionLocal() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise BookNotFound

        db.delete(book)
        db.commit()
        return {"message": "Book removed successfully"}

def update_books_per_id(book_id: int, book_update: BookUpdate):
    """
    Updates all fields of a book by its ID.
    """
    with SessionLocal() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise BookNotFound

        book.title = book_update.title
        book.author = book_update.author
        book.genre = book_update.genre

        db.commit()
        db.refresh(book)  # updates the object with data from the database
        return {"message": "Book updated successfully"}

def patch_books_per_id(book_id: int, book_change: BookChange):
    """
    Updates only the fields that were sent.
    """
    with SessionLocal() as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise BookNotFound

        if book_change.title is not None:
            book.title = book_change.title
        if book_change.author is not None:
            book.author = book_change.author
        if book_change.genre is not None:
            book.genre = book_change.genre

        db.commit()
        db.refresh(book)
        return {"message": "Book changed successfully"}

def add_books(book_id: int, book_create: BookCreate):
    """
    Adds a new book to the table.
    """
    with SessionLocal() as db:
        # If the ID is not auto-increment, we need to check if it already exists
        book_exists = db.query(Book).filter(Book.id == book_id).first()
        if book_exists:
            return {"message": "Book ID already exists"}

        new_book = Book(
            id=book_id,
            title=book_create.title,
            author=book_create.author,
            genre=book_create.genre
        )

        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        return {"message": "Book added successfully"}
