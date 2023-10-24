from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from core.settings import Settings

""" session instantiation with the database """


engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
