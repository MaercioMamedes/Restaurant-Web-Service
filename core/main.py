from fastapi import FastAPI

from core.routes import auth, products, users

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)


@app.get('/')
def read_root():
    # endpoint home
    return {'message': 'success'}
