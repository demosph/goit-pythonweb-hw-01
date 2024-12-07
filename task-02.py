from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# Принцип SRP: Клас Book для зберігання інформації про книгу
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип ISP: Інтерфейс для бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def list_books(self):
        pass


# Принцип OCP та LSP: Клас Library реалізує інтерфейс LibraryInterface
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        return self.books


# Принцип DIP: Клас LibraryManager залежить від абстракції LibraryInterface
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.list_books()
        if books:
            for book in books:
                logger.info(book)
        else:
            logger.info("Library is empty.")


# Основна програма
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
