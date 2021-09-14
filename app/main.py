from typing import Optional,List

from fastapi import Depends, FastAPI
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
async def get_actus(limit: int = 100, offset: int = 0):
    if limit > 100:
        limit = 100
    return await api_client.get_actus(limit=limit, offset=offset)