from fastapi import FastAPI
from route.book import app as book_route

app = FastAPI()


@app.get("/")
def root():
    return {'message': 'Hello World'}


app.mount('/api', book_route)
