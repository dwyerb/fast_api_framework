from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

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
    item = {"item_id": item_id}
    if q:
        item.update({'q':q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}

        return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")
async def read_item(skip: int =0, limit: int=10):
    return fake_db[skip: skip + limit]