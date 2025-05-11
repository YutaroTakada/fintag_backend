# FastAPI
from fastapi import FastAPI
from router import csv
from typing import Dict

app = FastAPI()

# routerからのルーティング
app.include_router(csv.router)


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello World"}
