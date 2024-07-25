from fastapi import FastAPI, Path, Query
from controller.book import BookController
from request.bookCreate import BookCreateRequest
from response.book import ResourceBook

app = FastAPI()
book_controller = BookController()
book_resource = ResourceBook()


@app.get("/ping")
def ping():
    return {'message': 'pong'}


@app.get("/book")
def all_books(category: str | None = Query(min_length=1, default=None)):
    return book_controller.get(category)


@app.get("/book/{id_book}")
def find_book(id_book: int = Path(gt=0)):
    book = book_controller.find(id_book)
    return book_resource.to_json(book)


@app.post("/book")
async def create_book(book: BookCreateRequest):
    return book_controller.create(book)


@app.put("/book/{id_book}")
async def update_book(book: BookCreateRequest, id_book: int = Path(gt=0)):
    return book_controller.update(id_book, book)


@app.delete("/book/{id_book}")
async def delete_book(id_book: int = Path(gt=0)):
    return book_controller.delete(id_book)
