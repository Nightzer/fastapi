from fastapi import FastAPI
from db import BOOKS, Book

app = FastAPI()


@app.get("/ping")
def ping():
    return {'message': 'pong'}


@app.get("/book")
def all_books(category: str | None = None):
    if category:
        books = []
        for book in BOOKS:
            if book.get('category').casefold() == category.casefold():
                books.append(book)
        return books
    return BOOKS


@app.get("/book/{id_book}")
def find_book(id_book: int):
    for book in BOOKS:
        if book.get('id') == id_book:
            return book


@app.post("/book")
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS


@app.put("/book/{id_book}")
async def update_book(id_book: int, book: Book):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('id') == id_book:
            BOOKS[i] = book
    return BOOKS


@app.delete("/book/{id_book}")
async def delete_book(id_book: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('id') == id_book:
            BOOKS.pop(i)
    return BOOKS
