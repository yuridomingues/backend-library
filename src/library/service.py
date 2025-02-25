from src.library.exceptions import BookNotFound
from src.library.schema import BookChange, BookCreate, BookUpdate

# List of books
books = [
    {
        'id': 1,
        'title': 'Lúcia já-vou-indo',
        'author': 'Maria Heloísa Penteado',
        'genre': "Children\'s Fiction"
    },
    {
        'id': 2,
        'title': 'A Biblioteca da Meia-Noite',
        'author': 'Matt Haig',
        'genre': 'Science Fiction'
    },
    {
        'id': 3,
        'title': 'The Picture of Dorian Gray',
        'author': 'Oscar Wilde',
        'genre': 'Classic Fiction'
    },
    {
        'id': 4,
        'title': 'Psicose',
        'author': 'Robert Bloch',
        'genre': 'Thriller'
    },
    {
        'id': 5,
        'title': '1984',
        'author': 'George Orwell',
        'genre': 'Dystopian'
    },
]


def get_all_books() -> list[dict]:
    """
    Retrieves all books from the library.
    """
    return books


def get_book_by_id(book_id: int) -> dict | None:
    """
    Retrieve a book from the library by its ID.
    """
    for book in books:
        if book["id"] == book_id:
            return book

    raise BookNotFound

def remove_books_per_id(book_id: int) -> dict:
    """
    Removes a book by its id.
    """
    for book in books.copy():
        if book['id'] == book_id:
            books.remove(book)
            return {"message": "Book removed successfully"}
    raise BookNotFound

def update_books_per_id(book_id: int, book_update: BookUpdate):
    """
    Updates the details of a book with the provided ID
    """
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['genre'] = book_update.genre
            return {"message": "Book updated successfully"}
    raise BookNotFound

def patch_books_per_id(book_id: int, book_change: BookChange):
    """
    Change some detail of the book with the provided ID.
    """
    for book in books:
        if book['id'] == book_id:
            if book_change.title is not None:
                book['title'] = book_change.title
            if book_change.author is not None:
                book['author'] = book_change.author
            if book_change.genre is not None:
                book['genre'] = book_change.genre
            return {"message": "Book changed successfully"}
    raise BookNotFound

def add_books(book_id: int, book_create: BookCreate):
    """
    Add a new book to the library
    """
    new_book = {
        'id': book_id,
        'title': book_create.title,
        'author': book_create.author,
        'genre': book_create.genre
    }
    books.append(new_book)
    return {"message": "Book added successfully"}
