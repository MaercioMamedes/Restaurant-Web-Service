"""exclude column quantity from Product Model

Revision ID: f20624057da6
Revises: e9340ff65123
Create Date: 2023-08-11 21:50:05.429340

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'f20624057da6'
down_revision: Union[str, None] = 'e9340ff65123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
