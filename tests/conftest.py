import pytest
from fastapi.testclient import TestClient

from core.main import app

# from sqlalchemy import create_engine, select
# from sqlalchemy.orm import sessionmaker


# from core.models import Base


"""@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)
"""


@pytest.fixture
def client():
    return TestClient(app)
