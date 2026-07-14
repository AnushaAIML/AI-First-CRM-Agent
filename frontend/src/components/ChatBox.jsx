import { useSelector } from "react-redux";

function ChatBox() {
  const { messages, loading, error } = useSelector(
    (state) => state.chat
  );

  return (
    <div className="chat-history">

      {messages.length === 0 && (
        <div
          style={{
            textAlign: "center",
            color: "#9ca3af",
            marginTop: "80px",
          }}
        >
          <h3>👋 Welcome</h3>

          <p>
            Start by describing an HCP interaction.
          </p>

          <br />

          <p>
            Example:
          </p>

          <p>
            <i>
              Today I met Dr. Sharma. We discussed Product X,
              shared brochures and the response was positive.
            </i>
          </p>
        </div>
      )}

      {messages.map((msg, index) => (
        <div
          key={index}
          className={`message ${msg.role}`}
        >
          <strong>
            {msg.role === "user"
              ? "You"
              : "AI Assistant"}
          </strong>

          <br />
          <br />

          {msg.content}
        </div>
      ))}

      {loading && (
        <div className="message assistant">
          🤖 Thinking...
        </div>
      )}

      {error && (
        <div
          style={{
            color: "red",
            marginTop: "10px",
          }}
        >
          {error}
        </div>
      )}

    </div>
  );
}

export default ChatBox;