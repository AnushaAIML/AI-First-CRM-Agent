import "./App.css";

import InteractionPanel from "./components/InteractionPanel";
import ChatBox from "./components/ChatBox";
import InteractionForm from "./components/InteractionForm";

function App() {
  return (
    <div className="app">

      <header className="app-header">
        <div>
          <h1>AI CRM Agent</h1>
          <p>
            AI-Powered Healthcare Professional Interaction Management
          </p>
        </div>
      </header>

      <main className="dashboard">

        {/* LEFT PANEL */}

        <section className="left-panel">
          <InteractionPanel />
        </section>

        {/* RIGHT PANEL */}

        <section className="right-panel">

          <div className="chat-header">
            <h2>AI Assistant</h2>
            <p>
              Ask the AI to log, edit, validate or analyze interactions.
            </p>
          </div>

          <ChatBox />

          <InteractionForm />

        </section>

      </main>

    </div>
  );
}

export default App;