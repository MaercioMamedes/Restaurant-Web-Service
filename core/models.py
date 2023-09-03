from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str]
    price: Mapped[float]
    type: Mapped[str]


class User(Base):
    __tablename__ = 'user'

    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    client: Mapped['Client'] = relationship(back_populates='user')
    employee: Mapped['Employee'] = relationship(back_populates='user')


class Client(Base):
    __tablename__ = 'client'

    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped['int'] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='client')


class Employee(Base):
    __tablename__ = 'employee'
    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped['int'] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='employee')
    manager: Mapped[bool]
