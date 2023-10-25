from sqlalchemy import select

from core.models.product import Product
from core.models.user import User

""" use case tests for create tables """


def test_create_product(session):
    new_product = Product(
        description='Suco de Laranja 400ml',
        price=7.0,
        type='suco',
    )
    session.add(new_product)
    session.commit()

    product = session.scalar(
        select(Product).where(Product.description == 'Suco de Laranja 400ml')
    )

    assert product.description == 'Suco de Laranja 400ml'


def test_create_user(session):
    new_user = User(
        name='Maercio Mamedes',
        email='maerciomamedes@hotmail.com',
        password='secret_key',
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.name == 'Maercio Mamedes'))
    assert user.name == 'Maercio Mamedes'
