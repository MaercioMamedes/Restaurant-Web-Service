from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
    type: Mapped[str]
