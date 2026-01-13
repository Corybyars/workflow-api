import uuid
from sqlalchemy import String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.models.role import Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[Role] = mapped_column(
        Enum(Role, name="role_enum"),
        nullable=False,
        default=Role.DEVELOPER,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    tasks = relationship(
        "Task",
        back_populates="assigned_user",
    )

    projects = relationship(
        "Project",
        back_populates="owner",
    )
