import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from core.database import get_session
from core.main import app
from core.models.base import Base
from core.models.product import Product
from core.models.user import User
from core.security import get_password_hash

""" test scenario settings """


@pytest.fixture
def session():
    """instantiating a mock session for an in-memory database"""

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
    """HTTP client for test requests"""

    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def product(session):
    """Instantiating a test product"""

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
    """Instantiating a test user"""

    password = 'secret_key'
    user = User(
        name='Test User',
        email='test_user@test.com',
        password=get_password_hash(password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    user.clean_password = 'secret_key'

    return user


@pytest.fixture
def list_users(session):
    """Creating a list of users for testing"""

    for i in range(10):
        password = f'secret_key{i}'
        user = User(
            name=f'Test User_{i}',
            email=f'test_user_{i}@test.com',
            password=get_password_hash(password),
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        user.clean_password = f'secret_key{i}'

    return session.scalars(select(User)).all()


@pytest.fixture
def other_user(session, list_users):

    return list_users[1]


@pytest.fixture
def token(client, user):
    """authentication token for the test user"""
    response = client.post(
        '/token/',
        data={'username': user.email, 'password': user.clean_password},
    )

    return response.json()['access_token']
