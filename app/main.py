from typing import Optional,List

from fastapi import Depends, FastAPI
from api_client import ApiClient


app = FastAPI()

api_client = ApiClient()

@app.get("/actualites")
async def get_actus():
    return await api_client.get_actus()