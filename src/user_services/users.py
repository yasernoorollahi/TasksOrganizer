from fastapi import FastAPI

app=FastAPI()

@app.get('/',description='this is my first route in fastapi', deprecated=True)
async def base_get_route():
    return{'message':'Hello, World!'}

@app.post('/')
async def post():
    return {'message':'hello from the post route'}

@app.put('/{id}')
async def put():
    return {'message':'hello from the put route'}