from typing import Union
from fastapi import FastAPI

import config
import os

settings = config.settings[os.getenv('FASTAPI_ENV', 'development')]
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "app_env": settings.app_env,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}