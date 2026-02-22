from library_system import Book, Library, borrow_item

def main():
    library = Library()

    book1 = Book("Python Basics", "John Doe", 300)
    book2 = Book("AI Introduction", "Jane Smith", 250)

    # admin adds books
    print(library.add_book("Admin", book1))
    print(library.add_book("Admin", book2))

    # student tries (should fail)
    print(library.add_book("Student", Book("Hackers Guide", "Mr X", 200)))

    # borrow and return
    print(library.borrow_book("Python Basics"))
    print(library.return_book("Python Basics"))

    # iterable library
    print("\nBooks in library:")
    for book in library:
        print(book)

    # duck typing demo
    class Magazine:
        def __init__(self, title):
            self.title = title

    mag = Magazine("Tech Monthly")
    borrow_item(mag)


if __name__ == "__main__":
    main()