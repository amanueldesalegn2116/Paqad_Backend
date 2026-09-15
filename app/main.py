from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.database import init_db, SessionLocal
from app.routers import institutions, projects, evidence, discrepancies, verification, reports, analytics, chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database and seed data on startup."""
    init_db()
    # Seed mock data
    from app.seed.seed_data import seed_database
    db = SessionLocal()
    try:
        seeded = seed_database(db)
        if seeded:
            print("[OK] Database seeded with mock data")
        else:
            print("[OK] Database already contains data")
    finally:
        db.close()
    yield


settings = get_settings()

app = FastAPI(
    title="Paqad API",
    description="Civic transparency and accountability platform API",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS
origins = [o.strip() for o in settings.allowed_origins.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(institutions.router)
app.include_router(projects.router)
app.include_router(evidence.router)
app.include_router(discrepancies.router)
app.include_router(verification.router)
app.include_router(reports.router)
app.include_router(analytics.router)
app.include_router(chat.router)


@app.get("/")
def root():
    return {
        "name": "Paqad API",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
