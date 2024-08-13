from fastapi import FastAPI
from src.common.local_enums import Colors
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,User
 



app=FastAPI()
 


@app.get('/colors/{color_item}')
async def colors(color: Colors):

    if color == Colors.GREEN:
        return {'color name': color, 'message':'you selected green'}
    
    if color  == Colors.BLUE:
        return {'color name': color, 'message': 'you selected blue'}
    
    else:
        return {'color name': color , 'message':'i like red'}





@app.get('/',description='this is my first route in fastapi', deprecated=True)
async def base_get_route():
    return{'message':'Hello, World!'}

@app.post('/')
async def post():
    return {'message':'hello from the post route'}

@app.put('/{id}')
async def put():
    return {'message':'hello from the put route'}

# @app.get('/items')
# async def list_items():
#     return {'message': 'list item route '}

# @app.get('/items/{item_id}')
# async def get_item(item_id:int):
#     return {'item':item_id}


@app.get('/items/{item_id}')
async def read_items(item_id,skip: int=0, limit: int=10,short:bool=False):
    if short:
        return {'item_id':item_id,'skip': skip, 'limit': limit , 'short':short}
    if not short:
        return {'message':'short == false'}