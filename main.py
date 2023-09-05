from fastapi import FastAPI
from route import app as route_app

app = FastAPI()


@app.get("/")
def root():
    return {'message': 'Hello World'}


app.mount('/api', route_app)
