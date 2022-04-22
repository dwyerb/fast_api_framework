from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel



app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

fake_db = [{'item_name':'foo'},{'item_name':'bar'},{'item_name':'kate'},{'item_name':'barry'}]

@app.get("/")
async  def root():
    return {"message":"get git"}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = int = Path(..., title="The ID of the item to get")
    q: Optional[str] = Query(None, alias="item-query")
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}

        return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")
async def read_item(q: Optional[List[str]] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

@app.post("/stuff/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}