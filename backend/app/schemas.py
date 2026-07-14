# Pydantic Schemas 
"""
Pydantic schemas for validating API requests and responses.
"""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class InteractionBase(BaseModel):
    """Common fields shared by all interaction schemas."""

    hcp_name: str = Field(..., min_length=2, max_length=255)
    interaction_date: date
    summary: str = Field(..., min_length=5)
    sentiment: str
    materials_shared: List[str] = Field(default_factory=list)
    compliance_status: str = "Pending"
    next_best_action: str = ""


class InteractionCreate(InteractionBase):
    """Schema used when creating a new interaction."""
    pass


class InteractionUpdate(BaseModel):
    """Schema used when updating an existing interaction."""

    hcp_name: Optional[str] = None
    interaction_date: Optional[date] = None
    summary: Optional[str] = None
    sentiment: Optional[str] = None
    materials_shared: Optional[List[str]] = None
    compliance_status: Optional[str] = None
    next_best_action: Optional[str] = None


class InteractionResponse(InteractionBase):
    """Schema returned by the API."""

    id: int

    model_config = ConfigDict(from_attributes=True)