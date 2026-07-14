"""
Database helpers for CRM tools.
"""

from app.database import SessionLocal



def get_session():

    return SessionLocal()