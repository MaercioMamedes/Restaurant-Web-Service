from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models import Product, User
from core.schemas import ProductList, ProductPublic, ProductSchema
from core.security import get_current_user

router = APIRouter(prefix='/produtos', tags=['produtos'])


@router.post('/', response_model=ProductPublic, status_code=201)
def create_product(
    product: ProductSchema,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    # endpoint create product

    if not current_user:
        raise HTTPException(status_code=400, detail='Not enough permissions')

    else:
        db_product = session.scalar(
            select(Product).where(Product.description == product.description)
        )

        if db_product:
            raise HTTPException(
                status_code=400,
                detail='description product already registered',
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


@router.get('/', response_model=ProductList)
def read_products(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    # endpoint list products
    products = session.scalars(select(Product).offset(skip).limit(limit)).all()

    return {'products': products}


@router.get('/{product_id}', response_model=ProductPublic)
def read_product(product_id: int, session: Session = Depends(get_session)):
    # endpoint get product by id

    db_product = session.scalar(
        select(Product).where(Product.id == product_id)
    )

    if db_product is not None:
        return db_product
    else:
        raise HTTPException(status_code=400, detail='Produto não cadastrado')


@router.put('/{product_id}', response_model=ProductPublic)
def update_product(
    product_id: int,
    product: ProductSchema,
    session: Session = Depends(get_session),
):
    # endpoint update product

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


@router.delete('/{product_id}')
def delete_product(
    product_id: int,
    session: Session = Depends(get_session),
):
    # endpoint delete product

    db_product = session.scalar(
        select(Product).where(Product.id == product_id)
    )
    session.delete(db_product)
    session.commit()
    return {'detail': 'Produto excluído com sucesso'}
