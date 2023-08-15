from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models import Product
from core.schemas import ProductSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'success'}


@app.post('/produto/', response_model=ProductSchema, status_code=201)
def create_product(
    product: ProductSchema, session: Session = Depends(get_session)
):
    db_product = session.scalar(
        select(Product).where(Product.description == product.description)
    )

    if db_product:
        raise HTTPException(
            status_code=400, detail='description product already registered'
        )

    db_product = Product(
        description=product.description,
        price=product.price,
        type=product.type,
    )

    session.add(db_product)
    session.commit()
    session.refresh(db_product)

    return db_product
