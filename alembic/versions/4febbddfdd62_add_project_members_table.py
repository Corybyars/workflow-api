"""add project members table

Revision ID: 4febbddfdd62
Revises: bc49633eba27
Create Date: 2026-01-21 18:42:06.511473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4febbddfdd62'
down_revision: Union[str, Sequence[str], None] = 'bc49633eba27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
