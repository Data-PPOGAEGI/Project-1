from os import strerror
from typing import Optional
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    sex: str
    age: str
    location: str
    dsbjt: str
    mainc: str
    subc: str
    rate: float

@app.get('/')
async def home():
    return 'Hello World'

@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    return item

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host = '0.0.0.0', port = 8000)