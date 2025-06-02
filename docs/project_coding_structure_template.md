# Project Coding & Structure Template

## Version: 2.0.0 (Last updated: 2025-05-25)

## Examples

### Example 1: Simple Project Structure

- **Language:** Python
- **Paradigm:** Modular, OOP
- **Key Practice:** Use snake_case for variables, modularize utilities

```text
project-root/
├── api/            # FastAPI endpoints
├── models/         # Pydantic models
├── services/       # Business logic
├── tests/          # Unit and integration tests
├── config/         # Settings and secrets
└── README.md
```

**Tech Stack:**

- Frontend: N/A
- Backend: FastAPI
- Database: SQLite
- CI/CD: GitHub Actions

---

### Example 2: Detailed Fullstack Project

- **Language:** TypeScript, Python
- **Paradigm:** Functional (frontend), OOP (backend)
- **Key Practice:** Use PascalCase for React components, modularize Redux slices

```text
project-root/
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── store/        # Redux slices
│   │   └── utils/        # Helpers
│   └── public/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI endpoints
│   │   ├── db/           # Database models
│   │   └── services/     # Business logic
│   └── tests/
├── shared/
│   └── types/            # Shared TypeScript types
├── scripts/
└── README.md
```

**Tech Stack:**

- Frontend: React, Redux, TypeScript
- Backend: FastAPI, SQLAlchemy
- Database: PostgreSQL
- CI/CD: GitHub Actions, Docker
- Cloud: AWS (S3, EC2)

---

## Template

- **Language(s):**
- **Paradigm(s):**
- **Key Practices:**

```text
[project-root]/
├── [dir-1]/
│   ├── [subdir-1]/    # [description]
│   ├── [subdir-2]/    # [description]
│   └── [subdir-3]/    # [description]
├── [dir-2]/
│   ├── [subdir-1]/    # [description]
│   └── [subdir-2]/    # [description]
├── [shared-or-common]/
│   ├── [subdir-1]/    # [description]
│   └── [subdir-2]/    # [description]
└── [config-or-root-files]/
    └── [description]
```

**Tech Stack:**

- Frontend:
- Backend:
- Database:
- CI/CD:
- Cloud/Other:
