from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get('/')
def read():
    return {'Hello': 'World'}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id}

@app.post('/items/')
def create_item(item: Item):
    return {'item': item}

if __name__ == '__main__':
    uvicorn.run(app)