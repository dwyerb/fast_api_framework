from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async  def root():
    return {"message":"get git"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return{"item id":item_id}
