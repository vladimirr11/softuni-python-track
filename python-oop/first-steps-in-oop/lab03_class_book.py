class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book('My book', 'me', '49587404')

print(book.name)
print(book.author)
print(book.pages)
book.name = "dragan"
print(book.name)
