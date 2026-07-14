"""
LangGraph Tool Registry

Central place where all AI tools are registered.
"""

from app.services.tools.log_interaction import log_interaction
from app.services.tools.edit_interaction import edit_interaction
from app.services.tools.fetch_hcp_profile import fetch_hcp_profile
from app.services.tools.suggest_next_best_action import (
    suggest_next_best_action,
)
from app.services.tools.validate_compliance import (
    validate_compliance,
)


TOOLS = [
    log_interaction,
    edit_interaction,
    fetch_hcp_profile,
    suggest_next_best_action,
    validate_compliance,
]


__all__ = [
    "TOOLS",
]