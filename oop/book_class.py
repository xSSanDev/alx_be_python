# Define the Book class
class Book:
    # Constructor to initialize the Book instance with title, author, and year
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor to print a message when the Book instance is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation method to return a formatted string for the Book instance
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation method to return a string that recreates the Book instance
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"