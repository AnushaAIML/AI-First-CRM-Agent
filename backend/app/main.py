# FastAPI Main Application 
"""
FastAPI Application Entry Point

Responsibilities:
1. Create FastAPI server.
2. Configure CORS.
3. Initialize database.
4. Register API routes.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import router
from app.database import init_db


# ============================================================
# Application Startup / Shutdown
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs during application startup.
    """

    print("Initializing database...")
    init_db()
    print("Database ready.")

    yield

    print("Application shutdown.")


# ============================================================
# FastAPI App
# ============================================================

app = FastAPI(
    title="AI First CRM - HCP Module",
    description="LangGraph powered Healthcare Professional interaction assistant.",
    version="1.0.0",
    lifespan=lifespan,
)


# ============================================================
# CORS Configuration
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Routes
# ============================================================

app.include_router(router)


@app.get("/")
def health_check():
    """
    Basic server health check.
    """

    return {
        "status": "running",
        "message": "AI CRM backend is active",
    }