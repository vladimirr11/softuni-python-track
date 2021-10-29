class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.page = 0


class Library:
    def __init__(self, location, books = []) -> None:
        self.books = books
        self.location = location

    def find_book(self, title):
        requested_book = [book for book in self.books if book.title == title]
        if requested_book:
            return requested_book[0]
        return 'some massage'
    
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return 'some massage'
        return 'other massage'


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Reader(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def turn_page(self, page):
        self.page = page
