# Paqad Backend

**Civic Transparency & Accountability Platform — API Server**

Paqad tracks public commitments and infrastructure projects from announcement to evidence and verification. This is the backend API powering both the web and mobile applications.

## Tech Stack

- **Framework**: FastAPI (Python)
- **Database**: SQLite (dev) / PostgreSQL (production via Supabase)
- **ORM**: SQLAlchemy
- **Validation**: Pydantic v2
- **Server**: Uvicorn

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py             # Settings & environment config
│   ├── database.py           # Database connection & session
│   ├── models/               # SQLAlchemy ORM models
│   │   ├── institution.py
│   │   ├── project.py
│   │   ├── evidence.py
│   │   ├── discrepancy.py
│   │   ├── verification.py
│   │   └── report.py
│   ├── schemas/              # Pydantic request/response schemas
│   ├── routers/              # API route handlers
│   │   ├── institutions.py
│   │   ├── projects.py
│   │   ├── evidence.py
│   │   ├── discrepancies.py
│   │   ├── verification.py
│   │   ├── reports.py
│   │   └── analytics.py
│   ├── services/             # Business logic & analytics
│   └── seed/                 # Mock data seeding
│       └── seed_data.py      # 15 realistic Ethiopian projects
├── requirements.txt
└── .env.example
```

## Core Workflow

```
Government Commitment → Structured Project → Evidence Collection
→ Monitoring → Discrepancy Detection → Verification Request
→ Institutional Response → Accountability Status
```

## Status State Machine

`Reported → Documented → Monitoring → Verification Requested → Partially Verified → Verified → Conflicting Evidence → Unresolved`

## Key Design Principles

- **Evidence-driven**: Never labels anything "fraud" or "false" automatically
- **Neutral states**: Uses factual evidence statuses, not accusations
- **Transparent**: Every claim is linked to its source

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /api/v1/projects` | List all projects (filter by status, region, search) |
| `GET /api/v1/projects/{id}` | Project detail with full metadata |
| `GET /api/v1/projects/{id}/timeline` | Accountability timeline |
| `GET /api/v1/evidence` | All evidence items (filter by project, source type) |
| `GET /api/v1/discrepancies` | Detected discrepancies |
| `GET /api/v1/verification-requests` | Verification request tracking |
| `GET /api/v1/reports` | Public citizen reports |
| `POST /api/v1/reports` | Submit a new citizen report |
| `GET /api/v1/analytics/dashboard` | Dashboard statistics |
| `GET /api/v1/analytics/charts` | Chart data (status distribution, budget, trends) |
| `GET /api/v1/institutions` | List tracked institutions |

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dev server
python -m uvicorn app.main:app --port 8000 --reload

# API docs
open http://localhost:8000/docs
```

## Mock Data

The server auto-seeds 15 realistic Ethiopian infrastructure projects on first startup, including:
- Addis Ababa–Djibouti Railway Maintenance
- Grand Ethiopian Renaissance Dam (GERD)
- Hawassa Industrial Park Phase II
- National Digital ID System (Fayda)
- And 11 more...

## Environment Variables

See `.env.example` for available configuration options.

## License

Prototype — for demonstration purposes only.
