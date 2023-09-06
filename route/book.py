from fastapi import FastAPI
from controller.book import BookController
from request.bookCreate import BookCreateRequest

app = FastAPI()
book_controller = BookController()


@app.get("/ping")
def ping():
    return {'message': 'pong'}


@app.get("/book")
def all_books(category: str | None = None):
    return book_controller.get(category)


@app.get("/book/{id_book}")
def find_book(id_book: int):
    return book_controller.find(id_book)


@app.post("/book")
async def create_book(book: BookCreateRequest):
    return book_controller.create(book)


@app.put("/book/{id_book}")
async def update_book(id_book: int, book: BookCreateRequest):
    return book_controller.update(id_book, book)


@app.delete("/book/{id_book}")
async def delete_book(id_book: int):
    return book_controller.delete(id_book)
