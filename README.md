# Workflow Requirements Management Platform

A backend-focused requirements management platform designed to structure and organize the project discovery phase. The system helps teams define, prioritize, and manage requirements before creating user stories in tools like Jira.

## Overview

This project is a work in progress that I build and iterate on in my free time. It focuses on backend system design, relational data modeling, and maintainable schema evolution.

The platform models core entities such as **projects, users, roles, requirements, and tasks**, with explicit relationships that reflect real-world software delivery workflows. It is designed to support requirement alignment, traceability, and ownership prior to development execution.

## Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy (ORM)**
- **Alembic (migrations)**
- **Docker**
- **Git / GitHub**

## Key Concepts

- **Projects** act as the top-level container for planning and discovery.
- **Users** are assigned roles (e.g., project manager, business analyst, developer).
- **Requirements** capture functional and non-functional needs with type, priority, and status.
- **Tasks** can be associated with projects, requirements, or both, allowing flexible planning and execution.
- **Schema migrations** are managed explicitly using Alembic to ensure consistent, versioned database evolution.

## Goals

- Practice and demonstrate backend engineering fundamentals
- Model real-world business workflows using relational data structures
- Build maintainable, evolvable systems using industry-standard tooling
- Serve as a foundation for future API endpoints and workflow automation

## Status

**Active development** — the database schema and domain models are implemented, with API endpoints and authorization logic planned next.
