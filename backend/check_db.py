from app.database import SessionLocal, Interaction


db = SessionLocal()

records = db.query(Interaction).all()

for item in records:
    print("--------------------------------")
    print("ID:", item.id)
    print("HCP:", item.hcp_name)
    print("Date:", item.interaction_date)
    print("Summary:", item.summary)
    print("Sentiment:", item.sentiment)
    print("Materials:", item.materials_shared)
    print("Compliance:", item.compliance_status)
    print("Next Action:", item.next_best_action)


db.close()