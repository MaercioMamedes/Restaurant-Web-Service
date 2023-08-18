from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models import Product, User
from core.schemas import ProductPublic, ProductSchema, UserPublic, UserSchema

app = FastAPI()

"""------------------ PRODUCTS VIEWS --------------------------"""


@app.get('/')
def read_root():
    # endpoint home
    return {'message': 'success'}


@app.get('/produtos/')
def read_products(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    # endpoint list products
    products = session.scalars(select(Product).offset(skip).limit(limit)).all()

    return {'products': products}


@app.get('/produtos/{product_id}', status_code=200)
def read_product(product_id: int, session: Session = Depends(get_session)):
    # endpoint get product by id

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
    # endpoint create product

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


@app.put('/produtos/{product_id}', response_model=ProductPublic)
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


@app.delete('/produtos/{product_id}')
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


"""  ------------ USERS VIEWS ------------------  """


@app.post('/usuarios/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.name == user.name))

    if db_user is None:
        new_user = User(
            name=user.name, email=user.email, password=user.password
        )

        session.add(new_user)
        session.commit()

        return new_user

    else:
        raise HTTPException(detail='Usuário já cadastrado', status_code=400)


@app.get('/usuarios/{user_id}', status_code=200)
def read_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is not None:

        return {'id': db_user.id, 'name': db_user.name, 'email': db_user.email}

    else:
        raise HTTPException(detail='usuário não encontrado', status_code=404)


@app.put('/usuarios/{user_id}', response_model=UserPublic, status_code=200)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is not None:
        db_user.name = user.name
        db_user.email = user.email
        db_user.password = user.password

        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    else:
        raise HTTPException(detail='Usuário não cadastrado', status_code=404)


@app.delete('/usuarios/{user_id}', status_code=200)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is not None:
        session.delete(db_user)
        session.commit()
        return {'detail': 'Usuário excluído com sucesso'}

    else:
        raise HTTPException(detail='Usuário não cadastrado', status_code=404)
