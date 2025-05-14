class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = {}  # Using a hash table (dictionary)

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print(f"Book '{title}' added.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed.title}' removed.")
        else:
            print("Book ID not found!")

    def search_book(self, book_id):
        if book_id in self.books:
            print(self.books[book_id])
        else:
            print("Book not found.")

    def check_out(self, book_id):
        if book_id in self.books:
            if self.books[book_id].available:
                self.books[book_id].available = False
                print(f"Book '{self.books[book_id].title}' checked out.")
            else:
                print("Book is already checked out.")
        else:
            print("Book ID not found!")

    def check_in(self, book_id):
        if book_id in self.books:
            if not self.books[book_id].available:
                self.books[book_id].available = True
                print(f"Book '{self.books[book_id].title}' checked in.")
            else:
                print("Book is already available.")
        else:
            print("Book ID not found!")

    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books.values():
                print(book)


# Example usage:
library = Library()
library.add_book("101", "1984", "George Orwell")
library.add_book("102", "To Kill a Mockingbird", "Harper Lee")
library.display_books()
library.check_out("101")
library.search_book("101")
library.check_in("101")
library.remove_book("102")
library.display_books()
