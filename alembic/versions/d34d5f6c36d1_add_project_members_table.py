"""add project members table

Revision ID: d34d5f6c36d1
Revises: 4febbddfdd62
Create Date: 2026-01-21 18:48:09.089168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd34d5f6c36d1'
down_revision: Union[str, Sequence[str], None] = '4febbddfdd62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
