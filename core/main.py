from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models import Product
from core.schemas import ProductPublic, ProductSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'success'}


@app.get('/produtos/{product_id}', status_code=200)
def read_product(product_id: int, session: Session = Depends(get_session)):
    db_product = session.scalar(
        select(Product).where(Product.id == product_id)
    )

    if db_product is not None:
        return db_product
    else:
        raise HTTPException(status_code=400, detail='Produto não cadastrado')


@app.post('/produtos/', response_model=ProductPublic, status_code=201)
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


@app.get('/produtos/')
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    products = session.scalars(select(Product).offset(skip).limit(limit)).all()

    return {'products': products}


@app.put('/produtos/{product_id}', response_model=ProductPublic)
def update_product(
    product_id: int,
    product: ProductSchema,
    session: Session = Depends(get_session),
):

    db_product = session.scalar(
        select(Product).where(Product.id == product_id)
    )

    if db_product is not None:

        db_product.description = product.description
        db_product.price = product.price
        db_product.type = product.type

        session.add(db_product)
        session.commit()
        session.refresh(db_product)

        return db_product


@app.delete('/produtos/{product_id}')
def delete_product(
    product_id: int,
    session: Session = Depends(get_session),
):
    db_product = session.scalar(
        select(Product).where(Product.id == product_id)
    )
    session.delete(db_product)
    session.commit()
    return {'detail': 'Produto excluído com sucesso'}
