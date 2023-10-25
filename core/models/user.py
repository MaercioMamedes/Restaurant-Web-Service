from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .client import Client
from .employee import Employee


class User(Base):
    __tablename__ = 'user'

    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    is_superuser: Mapped['bool'] = mapped_column(default=False, nullable=False)
    client: Mapped['Client'] = relationship(back_populates='user')
    employee: Mapped['Employee'] = relationship(back_populates='user')
