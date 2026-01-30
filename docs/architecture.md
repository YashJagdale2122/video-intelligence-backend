# Architecture

## Overview

The **Video Intelligence Backend** is designed as a modular, scalable backend system
for ingesting and processing video content asynchronously.

The architecture follows **clean layering principles** to ensure:
- Clear separation of concerns
- Testability
- Long-term maintainability
- Easy extension to real AI pipelines and distributed systems

The system is optimized for **fast ingestion**, while heavy AI workloads are handled
outside the request-response cycle.




## System Architecture Diagram

```mermaid
flowchart LR
    Client[Client / Frontend] -->|HTTP Requests| API[FastAPI API Layer]

    API --> Service[Service Layer]
    Service --> Repo[Repository Layer]
    Repo --> DB[(PostgreSQL Database)]

    Service -->|Trigger| BG[Background Task]
    BG --> AI[AI Processing Pipeline]
    AI --> Repo
````



## Core Components

### 1. API Layer (FastAPI)

**Responsibility**

* Handle HTTP requests
* Validate input/output schemas
* Return fast responses to clients

**Key Characteristics**

* Thin controllers
* No business logic
* Async-first design

**Examples**

* `POST /api/v1/videos`
* `GET /api/v1/videos/{video_id}`



### 2. Service Layer

**Responsibility**

* Business logic orchestration
* Workflow coordination
* Trigger background processing

**Why it exists**

* Prevents logic leakage into API routes
* Makes business rules testable and reusable

**Examples**

* Video ingestion workflow
* Status transitions (`UPLOADED → PROCESSING → COMPLETED`)



### 3. Repository Layer

**Responsibility**

* Database access abstraction
* ORM interaction via SQLAlchemy

**Why it exists**

* Decouples persistence from business logic
* Makes database changes low-impact

**Examples**

* Create video record
* Fetch video by ID
* Update processing status



### 4. Database Layer (PostgreSQL)

**Responsibility**

* Persistent storage
* Transactional consistency
* Source of truth for video state

**Stored Data**

* Video metadata
* Processing status
* Timestamps
* AI results (future)



### 5. Background Processing

**Responsibility**

* Execute long-running AI workflows
* Prevent blocking API requests

**Current Implementation**

* FastAPI background tasks (stubbed)

**Future Ready For**

* Celery / RQ
* Kafka / RabbitMQ
* Distributed workers



### 6. AI Processing Pipeline (Pluggable)

**Responsibility**

* Video analysis
* Transcription
* NLP / Vision / Risk detection

**Current State**

* Stubbed for extensibility

**Future Integrations**

* Whisper / ASR
* Vision models
* Custom LLM pipelines



## Request Flow (Step-by-Step)

### Video Ingestion Flow

1. Client sends `POST /api/v1/videos`
2. API validates input
3. Service creates video entry with status `UPLOADED`
4. Repository persists data in database
5. Background task is triggered
6. API responds immediately to client



### Video Status Retrieval Flow

1. Client sends `GET /api/v1/videos/{video_id}`
2. API calls service
3. Service queries repository
4. Repository fetches from database
5. API returns current status



## Design Decisions

### Why Async Processing?

* AI workloads are slow and unpredictable
* Keeps ingestion latency low
* Enables horizontal scaling



### Why Layered Architecture?

* Prevents tight coupling
* Enables isolated testing
* Allows independent evolution of layers



### Why Repository Pattern?

* Database independence
* Cleaner service logic
* Easier migration to new storage systems



## Scalability & Future Architecture

Planned upgrades without architectural changes:

* Replace background tasks with message queues
* Add multiple AI workers
* Introduce caching (Redis)
* Add authentication & authorization
* Introduce observability (metrics, tracing)
