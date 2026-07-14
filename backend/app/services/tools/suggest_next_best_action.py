"""
CRM Tool: Suggest Next Best Action

Generates recommended follow-up actions
based on HCP interaction summary.
"""

from langchain_core.tools import tool



ACTION_RULES = {

    "sample":
        "Send product samples within 2 business days.",

    "brochure":
        "Email the latest product brochure and clinical evidence.",

    "trial":
        "Share the latest clinical trial publication.",

    "pricing":
        "Arrange a pricing discussion with the sales manager.",

    "follow":
        "Schedule a follow-up visit next week.",

    "interested":
        "Book a detailed product demonstration.",

    "meeting":
        "Send a thank-you email and meeting summary.",
}




@tool
def suggest_next_best_action(
    summary: str
) -> dict:
    """
    Suggest the next best action
    for the sales representative.

    Args:
        summary:
            Interaction summary.

    Returns:
        Recommended action.
    """


    text = (
        summary or ""
    ).lower()



    for keyword, action in ACTION_RULES.items():


        if keyword in text:

            return {

                "success": True,

                "message":
                    "Recommendation generated successfully.",

                "data": {

                    "next_best_action":
                        action

                },
            }



    return {

        "success": True,

        "message":
            "Default recommendation generated.",

        "data": {

            "next_best_action":
                (
                    "Maintain regular engagement with the HCP "
                    "and schedule a follow-up visit."
                )

        },
    }