# library_management.py

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a library managing a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Return a book by title if it exists in the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or already returned

    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(book)
