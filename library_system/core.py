from .utils import track_access, permission_check

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self):
        self.books = []

    @permission_check("Admin")
    def add_book(self, user_role, book):
        self.books.append(book)
        return f"{book.title} added to library."

    @track_access
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.borrowed:
                book.borrowed = True
                return f"You borrowed '{title}'"
        return "Book not available"

    @track_access
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.borrowed:
                book.borrowed = False
                return f"You returned '{title}'"
        return "Book not found"

    # makes Library iterable
    def __getitem__(self, index):
        return self.books[index]


# Duck typing function
def borrow_item(item):
    print(f"Borrowed item: {item.title}")