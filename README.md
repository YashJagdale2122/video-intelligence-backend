## Video Intelligence Backend

This project is a backend system that ingests video inputs (file or URL) and asynchronously processes them to produce structured intelligence outputs. It demonstrates clean backend architecture, lifecycle-driven APIs, and async processing using FastAPI, PostgreSQL, and Docker.


## Problem Statement

Processing video content involves long-running, resource-intensive tasks such as transcription and visual analysis. Many systems either block requests synchronously or tightly couple business logic with infrastructure.

This project focuses on designing a backend that cleanly separates concerns, supports asynchronous processing, and exposes a clear lifecycle for video ingestion and analysis.


## Architecture Overview

The system is implemented as a modular monolith with strict separation of responsibilities:

- API Layer: Handles HTTP requests and validation
- Service Layer: Encapsulates business logic and lifecycle transitions
- Repository Layer: Manages database persistence
- Database: PostgreSQL for structured storage
- Background Processing: FastAPI background tasks for async workflows


POST /videos
  → VideoService
    → VideoRepository
      → PostgreSQL
  → Background Task
    → PROCESSING
    → COMPLETED


## API Design

### POST /api/v1/videos
Ingests a video via file upload or URL and returns a video identifier.

### GET /api/v1/videos/{id}
Returns the current processing status and metadata for a video.


## Processing Lifecycle

Each video follows a defined lifecycle:

- UPLOADED: Video accepted by the system
- PROCESSING: Background processing in progress
- COMPLETED: Processing finished successfully

The current implementation uses a background processing stub to simulate AI workloads. This design allows easy replacement with a task queue such as Celery in future iterations.


## Database Design

- videos: Stores video metadata and processing state
- ai_results: Reserved for storing AI-generated outputs

AI-related fields are stored as JSON to allow schema flexibility as models evolve.


## Running the Project

The system is fully containerized using Docker Compose.

```bash
docker-compose up --build

This starts:
    FastAPI backend
    PostgreSQL database

The API is available at:
http://localhost:8000/docs
```


## Design Decisions & Trade-offs

- Modular Monolith: Chosen over microservices to reduce distributed complexity while maintaining clean internal boundaries.
- Background Tasks: Used instead of a full task queue to validate async workflows with minimal infrastructure.
- JSON Storage for AI Results: Prevents frequent schema migrations as AI outputs evolve.
- Docker After Validation: The backend was validated locally before containerization to ensure understanding of failure modes.


## Future Improvements

- Replace background task stub with a distributed task queue
- Persist AI analysis outputs
- Add retry and failure handling
- Introduce migrations using Alembic
