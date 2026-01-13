import uuid
from sqlalchemy import Boolean, Column, String, ForeignKey
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

    role = relationship(
        "Role",
        backref="users",
    )

    role_id = Column(ForeignKey("roles.id"), nullable=False)

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

    requirements_created = relationship(
        "Requirement",
        back_populates="created_by",
        foreign_keys="Requirement.created_by_id",
    )

    requirements_assigned = relationship(
        "Requirement",
        back_populates="assigned_to",
        foreign_keys="Requirement.assigned_to_id",
    )
