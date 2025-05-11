# FastAPI
from fastapi import FastAPI
from router import csv

app = FastAPI()

# routerからのルーティング
app.include_router(csv.router)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
