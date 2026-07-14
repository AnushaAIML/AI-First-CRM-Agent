# 🧠 AI CRM Agent for Pharmaceutical Field Representatives

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![Redux](https://img.shields.io/badge/Redux-Toolkit-764ABC?style=for-the-badge&logo=redux)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)

</p>

An AI-powered CRM Assistant that enables pharmaceutical representatives to record Healthcare Professional (HCP) interactions using natural language. The agent automatically extracts structured information, updates CRM records, validates compliance, recommends follow-up actions, and auto-fills the interaction form.

---

# ✨ Features

- 🤖 AI-powered conversation using **Llama 3.3 70B (Groq)**
- 🧠 LangGraph Agent with tool-calling
- 📝 Auto-extracts HCP interaction details from natural language
- 📋 Automatically fills CRM form fields
- ✏️ Edit previously logged interactions
- 📊 Stores interactions in PostgreSQL
- ✅ Compliance validation
- 💡 AI-generated Next Best Action
- 💬 Professional React Chat Interface
- ⚡ FastAPI REST Backend

---

# 🏗 Architecture

```text
                    User
                     │
                     ▼
          React + Redux Frontend
                     │
                 Axios API
                     │
                     ▼
             FastAPI Backend
                     │
                     ▼
          LangGraph AI Agent
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Log Interaction  Edit Record  Compliance Check
      │              │              │
      └──────────────┼──────────────┘
                     │
                     ▼
             PostgreSQL Database
```

---

# ⚙️ Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | React, Redux Toolkit, Axios |
| Backend | FastAPI |
| AI Framework | LangGraph, LangChain |
| LLM | Groq (Llama 3.3 70B Versatile) |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Language | Python |

---

# 📂 Project Structure

```
AI-CRM-Agent/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── database/
│   ├── tools/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── features/
│   ├── store/
│   └── api/
│
└── README.md
```

---

# 🔄 AI Workflow

```
User Prompt
      │
      ▼
Llama 3.3 (Groq)
      │
      ▼
LangGraph Agent
      │
Tool Selection
      │
      ▼
CRM Tool Execution
      │
      ▼
PostgreSQL
      │
      ▼
Updated Form + AI Response
```

---

# 📌 Supported AI Capabilities

- Natural Language Understanding
- Tool Calling
- Conversation Memory
- Structured Information Extraction
- CRM Form Auto-Population
- Follow-up Recommendation
- Compliance Validation

---

# 🚀 Running the Project

## Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 📸 Screenshots

## Dashboard

> *(Add your dashboard screenshot here)*

---

## AI Conversation

> *(Add chat screenshot here)*

---

## Auto-filled CRM Form

> *(Add interaction form screenshot here)*

---

# 🎯 Future Improvements

- 🎙 Voice-to-Text Interaction
- 📄 PDF Report Generation
- 📅 Calendar Integration
- 📧 Email Follow-ups
- 👥 Authentication & Role Management
- 📊 Analytics Dashboard

---

# 👩‍💻 Author

**Anusha Raj**

AI / ML Engineer | Generative AI | Agentic AI | LangGraph | FastAPI | React

---

⭐ If you found this project helpful, consider giving it a **Star**.
