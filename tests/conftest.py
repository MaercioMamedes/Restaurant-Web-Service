import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from core.database import get_session
from core.main import app
from core.models import Base, Product, User


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    yield Session()

    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def product(session):
    product = Product(
        description='Suco de Laranja 400ml',
        price=7.0,
        type='suco',
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@pytest.fixture
def user(session):
    user = User(
        name='Maercio Mamedes',
        email='maerciomamedes@hotmail.com',
        password='secret_key',
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
