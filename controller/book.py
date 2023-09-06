from db.db import DB
from model.book import Book
from request.bookCreate import BookCreateRequest


class BookController:
    def get(self, category: str | None = None) -> object:
        if category:
            books = []
            for book in DB:
                if book.get('category').casefold() == category.casefold():
                    books.append(book)
            return books
        return DB

    def find(self, id_book: int):
        for book in DB:
            if book.get('id') == id_book:
                return book

    def create(self, book: BookCreateRequest):
        model = Book(**book.model_dump())
        DB.append(model)
        return DB


    def update(self, id_book: int, book: BookCreateRequest):
        for i in range(len(DB)):
            if DB[i].get('id') == id_book:
                DB[i] = book
        return DB

    def delete(self, id_book: int):
        for i in range(len(DB)):
            if DB[i].get('id') == id_book:
                DB.pop(i)
        return DB
