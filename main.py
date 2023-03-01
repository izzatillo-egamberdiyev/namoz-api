from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder

from namoz import ParsingNamoz
from typing import Union

app = FastAPI()

fake_db = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/namoz/{item_id}")
async def read_item(item_id):
    try:
        vaqtlar = await ParsingNamoz(item_id)
    # return {"item_id": item_id}
        return vaqtlar
    except:
        return {'error': "Notog'ri shaxar"}

@app.get('/name/')
async def get_name(name: str = 'Izzatillo', last_name: str='Egamberdiyev'):
    return f'{name} {last_name}'

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/desc/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
