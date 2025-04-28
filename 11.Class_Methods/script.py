class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

book1 = Book("Python for Beginners")
book2 = Book("Advanced Python")

print(f"Total books: {Book.total_books}")
