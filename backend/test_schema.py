from app.schemas import InteractionCreate

interaction = InteractionCreate(
    hcp_name="Dr. Sharma",
    interaction_date="2026-07-14",
    summary="Doctor showed interest in the new diabetes therapy.",
    sentiment="Positive",
    materials_shared=["Brochure", "Clinical Study"],
)

print(interaction.model_dump())