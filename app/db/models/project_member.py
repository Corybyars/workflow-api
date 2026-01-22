import uuid
import enum
from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, Column, UniqueConstraint, Index, func, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class ProjectRole(enum.Enum):
    PROJECT_MANAGER = "PROJECT_MANAGER"
    BUSINESS_ANALYST = "BUSINESS_ANALYST"
    DEVELOPER = "DEVELOPER"
    STAKEHOLDER = "STAKEHOLDER"
    VIEWER = "VIEWER"

class ProjectMember(Base):
    __tablename__ = "project_member"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        index=True,
        nullable=False)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        index=True,
        nullable=False
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default= func.now(),
        nullable=False,
    )

    role: Mapped[ProjectRole] = mapped_column(
        Enum(ProjectRole),
        nullable=False
    )

    project = relationship(
        "Project",
        back_populates="members",
    )

    user = relationship(
        "User",
        back_populates="project_memberships",
    )

    role = relationship(
        "Role",
        back_populates="project_members",
    )

    members = relationship(
        "ProjectMember",
        back_populates="project",
        cascade="all, delete-orphan",
    )

    project_memberships = relationship(
        "ProjectMember",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    project_members = relationship(
        "ProjectMember",
        back_populates="role",
    )

    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "user_id",
            name="uq_project_members_project_user",
        ),
        Index(
            "ix_project_members_project_id",
            "project_id",
        ),
        Index(
            "ix_project_members_user_id",
            "user_id",
        ),
    )