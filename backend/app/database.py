# Database Connection 
"""
Database configuration and ORM models.

This file:
1. Connects to PostgreSQL.
2. Defines the Interaction table.
3. Creates database sessions.
4. Initializes tables on application startup.
"""

import json
from datetime import date
from typing import Any

from sqlalchemy import Column, Date, Integer, String, Text, TypeDecorator, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings


# -----------------------------
# Store Python lists as JSON
# -----------------------------
class JSONList(TypeDecorator):
    """Converts Python lists to JSON strings for database storage."""

    impl = Text
    cache_ok = True

    def process_bind_param(self, value: Any, dialect):
        return json.dumps(value or [])

    def process_result_value(self, value: Any, dialect):
        return json.loads(value) if value else []


# -----------------------------
# PostgreSQL Connection
# -----------------------------
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()


# -----------------------------
# Interaction Table
# -----------------------------
class Interaction(Base):
    """Stores HCP interaction logs."""

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255), nullable=False)

    interaction_date = Column(
        Date,
        default=date.today,
        nullable=False,
    )

    summary = Column(Text, nullable=False)

    sentiment = Column(String(50), nullable=False)

    materials_shared = Column(
        JSONList,
        default=list,
        nullable=False,
    )

    compliance_status = Column(
        String(50),
        default="Pending",
        nullable=False,
    )

    next_best_action = Column(
        Text,
        default="",
        nullable=False,
    )


# -----------------------------
# Initialize Database
# -----------------------------
def init_db():
    """Create all tables if they don't already exist."""
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()