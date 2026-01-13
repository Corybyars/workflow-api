from enum import Enum as Enum
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Role(Enum):
    DEVELOPER = "Developer"
    PM = "Project Manager"
    BA = "Business Analyst"
    STAKEHOLDER = "Stake Holder"

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)