from fastapi import FastAPI

app = FastAPI()

# Home api or home page 
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Second api 
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}