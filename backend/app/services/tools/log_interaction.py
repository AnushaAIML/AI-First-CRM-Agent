"""
CRM Tool: Log Interaction
"""

from datetime import date

from langchain_core.tools import tool
from sqlalchemy.exc import SQLAlchemyError

from app.database import Interaction
from app.services.tools.db import get_session



@tool
def log_interaction(
    hcp_name: str,
    interaction_date: str,
    summary: str,
    sentiment: str,
    materials_shared: str | None = None,
):
    """
    Save HCP interaction into CRM.
    """

    db = get_session()

    try:

        # Handle natural language dates from LLM
        if (
            not interaction_date
            or interaction_date.lower() in [
                "today",
                "current date",
                "now",
            ]
        ):
            parsed_date = date.today()

        else:
            parsed_date = date.fromisoformat(
                interaction_date
            )


        interaction = Interaction(

            hcp_name=hcp_name,

            interaction_date=parsed_date,

            summary=summary,

            sentiment=sentiment,

            materials_shared=materials_shared,

            compliance_status="Pending",

        )


        db.add(interaction)

        db.commit()

        db.refresh(interaction)



        return {

            "success": True,

            "message":
                "Interaction logged successfully.",

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

            },

        }



    except SQLAlchemyError as e:

        db.rollback()


        return {

            "success": False,

            "message":
                str(e),

            "data": None,

        }



    except ValueError as e:

        return {

            "success": False,

            "message":
                f"Invalid date format: {str(e)}",

            "data": None,

        }



    finally:

        db.close()