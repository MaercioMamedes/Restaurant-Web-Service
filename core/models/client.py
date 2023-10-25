from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class Client(Base):
    __tablename__ = 'client'

    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped['int'] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='client')
