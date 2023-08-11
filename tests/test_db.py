from sqlalchemy import select

from core.models import Product


def test_create_product(session):
    new_product = Product(
        description='Suco de Laranja 400ml',
        price=7.0,
        quantity=1,
        type='suco',
    )
    session.add(new_product)
    session.commit()

    product = session.scalar(
        select(Product).where(Product.description == 'Suco de Laranja 400ml')
    )

    assert product.description == 'Suco de Laranja 400ml'
