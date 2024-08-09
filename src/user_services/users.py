from fastapi import FastAPI
from common.enums import Colors




app=FastAPI()


@app.get('/colors/{color_item}')
async def colors(color_item: Colors):

    if color_item == Colors.GREEN:
        return {'color name': color_item, 'message':'you selected green'}
    
    if color_item  == Colors.BLUE:
        return {'color name': color_item, 'message': 'you selected blue'}
    
    else:
        return {'color name': color_item , 'message':'i like red'}



@app.get('/',description='this is my first route in fastapi', deprecated=True)
async def base_get_route():
    return{'message':'Hello, World!'}

@app.post('/')
async def post():
    return {'message':'hello from the post route'}

@app.put('/{id}')
async def put():
    return {'message':'hello from the put route'}

@app.get('/items')
async def list_items():
    return {'message': 'list item route '}

@app.get('/items/{item_id}')
async def get_item(item_id:int):
    return {'item':item_id}