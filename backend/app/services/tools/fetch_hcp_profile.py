"""
CRM Tool: Fetch HCP Profile

Returns historical CRM information about an HCP.
"""

from langchain_core.tools import tool



HCP_PROFILES = {

    "Dr. Sharma": {

        "specialty":
            "Cardiologist",

        "prescription_tier":
            "Tier-1",

        "compliance_history":
            "Excellent",

    },


    "Dr. Reddy": {

        "specialty":
            "Endocrinologist",

        "prescription_tier":
            "Tier-2",

        "compliance_history":
            "Good",

    },


    "Dr. Kumar": {

        "specialty":
            "General Physician",

        "prescription_tier":
            "Tier-3",

        "compliance_history":
            "Average",

    },

}




@tool
def fetch_hcp_profile(
    hcp_name: str
) -> dict:
    """
    Retrieve historical information for an HCP.

    Args:
        hcp_name:
            Healthcare professional name.

    Returns:
        CRM profile information.
    """


    normalized_name = (
        hcp_name or ""
    ).strip().title()



    profile = HCP_PROFILES.get(

        normalized_name,

        {

            "specialty":
                "Unknown",

            "prescription_tier":
                "Unknown",

            "compliance_history":
                "No History",

        },

    )



    return {

        "success": True,

        "message":
            "HCP profile fetched successfully.",

        "data": {

            "hcp_name":
                normalized_name,

            **profile,

        },

    }