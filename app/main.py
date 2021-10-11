from typing import Optional,List

from fastapi import Depends, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from api_client import ApiClient


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_client = ApiClient()

@app.get("/actualites")
async def get_actus(limit: int = Query(le = 10, gt = 0, default=10), offset: int = Query(gt = 0, default=0)):
    if limit > 10:
        limit = 10
    return await api_client.get_actus(limit=limit, offset=offset)