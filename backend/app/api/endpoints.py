"""
API Endpoints for AI-First CRM Agent.

Provides:
1. Chat endpoint for LangGraph interaction.
2. Interaction history endpoint.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from app.database import Interaction, get_db
from app.services.agent_graph import run_agent


router = APIRouter(
    prefix="/api",
    tags=["CRM AI Agent"],
)


# ============================================================
# Request Schema
# ============================================================

class ChatRequest(BaseModel):
    """
    Incoming chat request.
    """

    message: str

    thread_id: str

    form_state: dict = Field(
        default_factory=dict
    )


# ============================================================
# AI Chat Endpoint
# ============================================================

@router.post("/chat")
def chat(request: ChatRequest):
    """
    Send user messages to LangGraph agent.

    The agent decides:
    - whether tools are required
    - what action to perform
    - what response to return
    """

    response = run_agent(
        user_message=request.message,
        thread_id=request.thread_id,
        form_state=request.form_state,
    )

    return {
        "assistant_message": response["assistant_message"],
        "form_state": response["form_state"],
    }


# ============================================================
# Interaction History Endpoint
# ============================================================

@router.get("/interactions")
def get_interactions(
    db: Session = Depends(get_db),
):
    """
    Retrieve stored HCP interaction history.
    """

    interactions = (
        db.query(Interaction)
        .order_by(Interaction.id.desc())
        .all()
    )

    return [
        {
            "id": item.id,
            "hcp_name": item.hcp_name,
            "interaction_date": str(item.interaction_date),
            "summary": item.summary,
            "sentiment": item.sentiment,
            "materials_shared": item.materials_shared,
            "compliance_status": item.compliance_status,
            "next_best_action": item.next_best_action,
        }
        for item in interactions
    ]