# library_system.py

# Define the base class Book
class Book:
    # Constructor to initialize the Book instance with title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Define the derived class EBook that inherits from Book
class EBook(Book):
    # Constructor to initialize the EBook instance with title, author, and file size
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

# Define the derived class PrintBook that inherits from Book
class PrintBook(Book):
    # Constructor to initialize the PrintBook instance with title, author, and page count
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

# Define the Library class to manage a collection of books
class Library:
    # Constructor to initialize the Library instance with an empty list of books
    def __init__(self):
        self.books = []

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)

    # Method to list all books in the library
    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")