from pydantic import BaseModel, Field


class BookCreateRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    category: str = Field(min_length=3)
    rating: int = Field(gt=-1, lt=6)


    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'Yo',
                'category': 'Python',
                'rating': 3
            }
        }
