"""
CRM Tool: Edit Interaction

Updates an existing HCP interaction in PostgreSQL.
"""

from datetime import date
from typing import Any

from langchain_core.tools import tool
from sqlalchemy.exc import SQLAlchemyError

from app.database import Interaction, SessionLocal



@tool
def edit_interaction(
    interaction_id: int,
    updates: dict[str, Any],
) -> dict:
    """
    Update an existing HCP interaction.

    Args:
        interaction_id:
            Interaction database ID.

        updates:
            Fields to modify.

    Returns:
        Updated interaction details.
    """

    db = SessionLocal()


    try:

        interaction = (
            db.query(Interaction)
            .filter(
                Interaction.id == interaction_id
            )
            .first()
        )


        if interaction is None:

            return {
                "success": False,
                "message": "Interaction not found.",
                "data": None,
            }



        allowed_fields = {
            "hcp_name",
            "interaction_date",
            "summary",
            "sentiment",
            "materials_shared",
            "compliance_status",
            "next_best_action",
        }



        updated_fields = []


        for field, value in updates.items():

            if field not in allowed_fields:
                continue


            if (
                field == "interaction_date"
                and isinstance(value, str)
            ):

                value = date.fromisoformat(value)



            setattr(
                interaction,
                field,
                value
            )

            updated_fields.append(field)



        db.commit()

        db.refresh(
            interaction
        )



        return {

            "success": True,

            "message":
                "Interaction updated successfully.",

            "data": {

                "id":
                    interaction.id,

                "hcp_name":
                    interaction.hcp_name,

                "interaction_date":
                    str(
                        interaction.interaction_date
                    ),

                "summary":
                    interaction.summary,

                "sentiment":
                    interaction.sentiment,

                "materials_shared":
                    interaction.materials_shared,

                "compliance_status":
                    interaction.compliance_status,

                "next_best_action":
                    interaction.next_best_action,

                "updated_fields":
                    updated_fields,
            },
        }



    except SQLAlchemyError as e:

        db.rollback()

        return {
            "success": False,
            "message": str(e),
            "data": None,
        }



    finally:

        db.close()