from pydantic import BaseModel


class BookCreateRequest(BaseModel):
    id: int
    title: str
    author: str
    category: str
