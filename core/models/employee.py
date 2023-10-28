from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Employee(Base):
    __tablename__ = 'employee'
    id: Mapped['int'] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped['int'] = mapped_column(ForeignKey('user.id'))
    user: Mapped[str('User')] = relationship(
        back_populates='employee', single_parent=True
    )
    manager: Mapped[bool]
