# csvファイルを読み込むAPIの開発。

# FastAPI
from fastapi import APIRouter
import polars as pl
from typing import Dict, Any

router = APIRouter()


# csvファイルを読み込むAPI
@router.get("/csv")
def read_csv(file_path: str) -> Dict[str, Any]:
    # csvファイルを読み込む
    df = pl.read_csv(file_path)
    return {"data": df.to_dict()}
