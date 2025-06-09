from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSON  # ✅ Postgres JSON support
from database import Base  # ✅ Updated for your PYTHONPATH
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    company = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    portfolio = Column(String, nullable=False)
    password = Column(String, nullable=False)
    verified = Column(Boolean, default=False)
    onboarding = Column(JSON, default=dict)  # ✅ Onboarding tracking
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
