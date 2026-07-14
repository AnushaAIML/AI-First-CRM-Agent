"""
CRM Tool: Validate Compliance

Checks interaction summary for compliance violations
and updates compliance status in PostgreSQL.
"""

from langchain_core.tools import tool
from sqlalchemy.exc import SQLAlchemyError

from app.database import Interaction, SessionLocal



PROHIBITED_PHRASES = {

    "off-label",

    "guaranteed cure",

    "100% cure",

    "cash incentive",

    "free gift",

    "gift card",

    "kickback",

}




@tool
def validate_compliance(
    interaction_id: int,
    summary: str,
) -> dict:
    """
    Validate CRM interaction compliance.

    Args:
        interaction_id:
            Database interaction ID.

        summary:
            Interaction summary.

    Returns:
        Compliance validation result.
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



        if not interaction:

            return {

                "success": False,

                "message":
                    "Interaction not found.",

                "data": None,

            }



        text = (
            summary or ""
        ).lower()



        violations = [

            phrase

            for phrase in PROHIBITED_PHRASES

            if phrase in text

        ]



        status = (
            "Flagged"
            if violations
            else "Approved"
        )



        interaction.compliance_status = status



        db.commit()

        db.refresh(
            interaction
        )



        return {

            "success": True,

            "message":
                "Compliance validation completed.",

            "data": {

                "interaction_id":
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
                    status,

                "next_best_action":
                    interaction.next_best_action,

                "violations":
                    violations,

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



    finally:

        db.close()