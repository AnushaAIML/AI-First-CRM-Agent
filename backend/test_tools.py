from app.services.tools import (
    log_interaction,
    edit_interaction,
    fetch_hcp_profile,
    suggest_next_best_action,
    validate_compliance,
)

print("=" * 60)
print("Testing log_interaction")

result = log_interaction.invoke({
    "hcp_name": "Dr. Sharma",
    "interaction_date": "2026-07-14",
    "summary": "Doctor interested in product brochure and requested samples.",
    "sentiment": "Positive",
    "materials_shared": ["Brochure", "Clinical Study"],
})

print(result)

interaction_id = result["id"]

print("=" * 60)
print("Testing edit_interaction")

print(
    edit_interaction.invoke({
        "interaction_id": interaction_id,
        "updates": {
            "summary": "Doctor requested additional clinical trial data."
        },
    })
)

print("=" * 60)
print("Testing fetch_hcp_profile")

print(
    fetch_hcp_profile.invoke({
        "hcp_name": "Dr. Sharma"
    })
)

print("=" * 60)
print("Testing suggest_next_best_action")

print(
    suggest_next_best_action.invoke({
        "summary": "Doctor requested product samples."
    })
)

print("=" * 60)
print("Testing validate_compliance")

print(
    validate_compliance.invoke({
        "interaction_id": interaction_id,
        "summary": "Doctor discussed off-label use."
    })
)

print("=" * 60)
print("ALL TOOLS PASSED")