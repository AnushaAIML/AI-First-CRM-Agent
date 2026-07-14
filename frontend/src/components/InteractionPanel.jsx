import { useSelector } from "react-redux";

function Field({ label, value, textarea = false }) {
  return (
    <div style={{ marginBottom: "18px" }}>
      <label
        style={{
          display: "block",
          marginBottom: "6px",
          fontWeight: 600,
          color: "#374151",
        }}
      >
        {label}
      </label>

      {textarea ? (
        <textarea
          rows={3}
          value={value || ""}
          readOnly
        />
      ) : (
        <input
          value={value || ""}
          readOnly
        />
      )}
    </div>
  );
}

function InteractionPanel() {
  const form = useSelector(
    (state) => state.chat.formState
  );

  const materials = Array.isArray(form.materials_shared)
    ? form.materials_shared.join(", ")
    : form.materials_shared || "";

  return (
    <>

      <h2 className="card-title">
        Interaction Details
      </h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "18px",
        }}
      >

        <Field
          label="HCP Name"
          value={form.hcp_name}
        />

        <Field
          label="Interaction Type"
          value={form.interaction_type}
        />

        <Field
          label="Interaction Date"
          value={form.interaction_date}
        />

        <Field
          label="Interaction Time"
          value={form.interaction_time}
        />

      </div>

      <Field
        label="Attendees"
        value={form.attendees}
      />

      <Field
        label="Topics Discussed"
        value={form.summary}
        textarea
      />

      <Field
        label="Materials Shared"
        value={materials}
      />

      <Field
        label="Samples Distributed"
        value={form.samples_distributed}
      />

      <Field
        label="Observed HCP Sentiment"
        value={form.sentiment}
      />

      <Field
        label="Outcomes"
        value={form.outcomes}
        textarea
      />

      <Field
        label="Follow-up Actions"
        value={form.next_best_action}
        textarea
      />

      <Field
        label="Compliance Status"
        value={form.compliance_status}
      />

    </>
  );
}

export default InteractionPanel;