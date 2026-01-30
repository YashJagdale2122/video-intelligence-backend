````md
# System Architecture

This document describes the architecture, design decisions, and data flow
for the **Video Intelligence Backend**.

The system is designed as a **modular monolith** with clear internal boundaries,
optimized for maintainability, testability, and future scalability.

## High-Level Architecture

```text
Client
  |
  v
FastAPI API Layer
  |
  v
Service Layer (Business Logic)
  |
  v
Repository Layer
  |
  v
PostgreSQL Database
  |
  +--> Background Task (AI Processing Stub)
````

### Key Characteristics

* Single deployable backend (modular monolith)
* Clear separation of concerns
* Asynchronous background processing
* Database-backed state tracking



## Layered Responsibilities

### API Layer

**Responsibility**

* Handle HTTP requests and responses
* Perform request validation
* Convert domain objects to API schemas

**What it does NOT do**

* No business logic
* No database operations
* No status transitions



### Service Layer

**Responsibility**

* Core business logic
* Orchestrates workflows
* Controls state transitions (e.g., `UPLOADED → PROCESSING`)

**Why this layer exists**

* Centralizes domain rules
* Makes logic testable
* Prevents fat controllers or smart repositories



### Repository Layer

**Responsibility**

* Database interaction via SQLAlchemy
* CRUD operations
* Transaction handling

**What it does NOT do**

* No business decisions
* No status changes
* No workflow logic



### Domain Layer

**Responsibility**

* Enums (e.g., processing status, source type)
* Domain concepts shared across layers

**Why enums are used**

* Prevent inconsistent string usage
* Enforce valid state transitions
* Ensure consistency across API, service, and persistence layers



### Infrastructure Layer

**Responsibility**

* Database configuration
* Background task execution
* External system integration (future)

Currently includes:

* PostgreSQL setup
* SQLAlchemy session management
* Background processing stub



## Request Flow

### Video Ingestion Flow

```text
1. Client sends POST /api/v1/videos
2. API validates input
3. Service creates Video entity with status = UPLOADED
4. Repository persists video record
5. Background task is triggered
6. API responds immediately with video_id
```

### Status Retrieval Flow

```text
1. Client sends GET /api/v1/videos/{video_id}
2. API delegates to service
3. Repository fetches video record
4. API returns current processing status
```



## Asynchronous Processing Design

### Why Asynchronous Processing?

* Video analysis (AI, transcription, vision) is time-consuming
* Synchronous processing would block API threads
* Poor user experience and low throughput

### Current Implementation

* Uses FastAPI background tasks (stub)
* Simulates long-running AI processing
* Updates status asynchronously

### Future Evolution

* Replace background task with:

  * Celery + Redis/RabbitMQ **or**
  * Kafka-based worker
* Add retry and failure recovery
* Isolate AI processing into a separate service if needed



## Database Design Overview

### Core Tables

* `videos`
* `ai_results`

### Key Design Decisions

* `videos` stores ingestion metadata and processing state
* `ai_results` stores AI outputs in JSON format
* AI fields are optional to support partial results

### Why JSON Fields?

* AI outputs are unstructured and evolving
* Avoid premature schema rigidity
* Enables faster iteration



## Design Decisions & Rationale

### Why Modular Monolith?

* Lower operational complexity than microservices
* Avoids network overhead and distributed failures
* Easier local development and debugging
* Internal modules allow future service extraction



### Why Service Controls Status?

* Status transitions are **business rules**
* Prevents duplication across routes
* Enables validation and future enforcement of state machines



### Why Repository Does Not Contain Logic?

* Keeps persistence concerns isolated
* Improves testability
* Avoids tight coupling between storage and business rules



### Why Return Domain Objects from Services?

* Allows API layer to control response shaping
* Prevents leakage of transport concerns into domain logic
* Makes service reusable by other interfaces (CLI, workers, gRPC)



## Trade-offs & Limitations

```text
Current Trade-offs:
- Background tasks are in-process
- No distributed queue yet
- No retry or dead-letter handling
- JSON fields reduce relational querying

Intentional Reasoning:
- Optimized for clarity and learning
- Avoid premature optimization
- Architecture supports gradual evolution
```



## Scalability Considerations

If load increases:

* Introduce message queue for background processing
* Add worker pool for AI tasks
* Cache status reads if needed
* Extract AI processing into separate service

The current design supports these changes without major refactoring.
