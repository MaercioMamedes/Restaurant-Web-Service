from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Consumer(Base):
    __tablename__ = 'consumer'

    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped['int'] = mapped_column(ForeignKey('user.id'))
    user: Mapped[str('User')] = relationship(
        back_populates='consumer', single_parent=True
    )
