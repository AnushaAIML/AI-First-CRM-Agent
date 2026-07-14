import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { sendMessage } from "../features/chat/chatSlice";

function InteractionForm() {
  const dispatch = useDispatch();

  const loading = useSelector(
    (state) => state.chat.loading
  );

  const [prompt, setPrompt] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!prompt.trim()) return;

    dispatch(sendMessage(prompt));

    setPrompt("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        display: "flex",
        gap: "10px",
        padding: "15px",
        borderTop: "1px solid #ddd",
      }}
    >
      <textarea
        rows={2}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Describe your HCP interaction..."
        style={{
          flex: 1,
          resize: "none",
          padding: "10px",
          borderRadius: "8px",
        }}
      />

      <button
        type="submit"
        disabled={loading}
        style={{
          width: "120px",
        }}
      >
        {loading ? "Sending..." : "Send"}
      </button>
    </form>
  );
}

export default InteractionForm;