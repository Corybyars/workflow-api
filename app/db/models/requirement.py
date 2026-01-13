import uuid
import enum
from sqlalchemy import Column, String, Text, Enum, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class RequirementType(enum.Enum):
    FUNCTIONAL = "FUNCTIONAL"
    NON_FUNCTIONAL = "NON_FUNCTIONAL"
    CONSTRAINT = "CONSTRAINT"
    RISK = "RISK"


class RequirementPriority(enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class RequirementStatus(enum.Enum):
    DRAFT = "DRAFT"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class Requirement(Base):
    __tablename__ = "requirements"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    type: Mapped[RequirementType] = mapped_column(
        Enum(RequirementType),
        nullable=False,
    )

    priority: Mapped[RequirementPriority] = mapped_column(
        Enum(RequirementPriority),
        nullable=False,
    )

    status: Mapped[RequirementStatus] = mapped_column(
        Enum(RequirementStatus),
        nullable=False,
        default=RequirementStatus.DRAFT,
    )

    created_by_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    assigned_to_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )

    # Relationships

    project = relationship(
        "Project",
        back_populates="requirements",
    )

    created_by = relationship(
        "User",
        back_populates="requirements_created",
        foreign_keys=[created_by_id],
    )

    assigned_to = relationship(
        "User",
        back_populates="requirements_assigned",
        foreign_keys=[assigned_to_id],
    )

    tasks = relationship(
        "Task",
        back_populates="requirements",
    )

