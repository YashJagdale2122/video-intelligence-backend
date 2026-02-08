# Video Intelligence Backend

![CI](https://github.com/YashJagdale2122/video-intelligence-backend/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://video-intelligence-backend.onrender.com/docs)
![Status](https://img.shields.io/badge/Status-Actively%20Maintained-brightgreen)

**[Live Demo](https://video-intelligence-backend.onrender.com/docs)** |
**[API Docs](https://video-intelligence-backend.onrender.com/docs)** |
**[Health Check](https://video-intelligence-backend.onrender.com/health)**


## Overview

**Video Intelligence Backend** is a **production-oriented backend system** designed to
ingest and process video content asynchronously.

The project focuses on **backend architecture, job orchestration, and reliability**,
treating AI pipelines as **internal processing components**, not the core system design.

It demonstrates how long-running, AI-heavy workloads can be handled **without blocking
API requests**, using clean separation of concerns and async execution.


## Problem Statement

Modern platforms must analyze large volumes of video content for tasks such as:

- Transcription
- Content understanding
- Metadata extraction
- Risk or compliance checks

These workloads are **slow and unpredictable**, making synchronous request handling
impractical, unreliable, and difficult to scale.


## Solution Overview

This project implements a **layered FastAPI backend** that:

- Accepts video ingestion requests via REST APIs
- Persists job metadata and lifecycle state
- Executes video analysis asynchronously
- Returns immediate responses to clients
- Tracks processing status reliably

The design prioritizes:

- Clear separation of concerns
- Async-first execution
- Testability and maintainability
- Future scalability (queues, workers, AI models)


## Architecture Overview

The system follows a **clean, layered backend architecture**, where request handling,
business logic, persistence, and AI processing are clearly separated.

```text
Client
  ↓
FastAPI API Layer
  ↓
Service Layer (Job Orchestration)
  ↓
Repository Layer
  ↓
PostgreSQL Database
  ↑
Background Worker
  ↓
AI Processing Pipelines
````

### Key Architectural Principles

* **Async ingestion**: APIs never perform heavy processing
* **Service-centric design**: Business logic lives outside routes
* **Repository abstraction**: Persistence is decoupled from logic
* **AI as a component**: Models are replaceable implementation details

📄 **Detailed architecture documentation:**
➡️ [`docs/architecture.md`](docs/architecture.md)


### Design Trade-offs

- **Background tasks vs message queues**  
  Background tasks are used initially to keep the system simple and easy to reason about.
  The architecture is designed to support migration to a message queue (Celery / RabbitMQ)
  when higher throughput or distributed workers are required.

- **Polling-based status retrieval**  
  Clients poll for job status instead of using callbacks or WebSockets to avoid added
  complexity in early stages and to keep the API contract simple and reliable.

- **AI pipelines as internal components**  
  AI models are treated as replaceable implementation details to avoid coupling API
  contracts to model behavior.


## Core Components

### API Layer

* Built with FastAPI
* Handles request validation and response formatting
* Exposes REST endpoints for ingestion and status retrieval
* Remains thin and logic-free

### Service Layer

* Orchestrates workflows and job lifecycle
* Manages state transitions (`UPLOADED → PROCESSING → COMPLETED`)
* Triggers background processing

### Repository Layer

* Encapsulates database access using SQLAlchemy
* Provides persistence abstraction
* Keeps business logic database-agnostic

### Background Processing

* Executes long-running video analysis
* Runs outside the request-response cycle
* Designed to be replaced by queues/workers in future

### AI Pipelines (Internal)

* Transcription
* NLP / vision analysis (stubbed)
* Designed to be pluggable and replaceable


## Data Flow & Job Lifecycle

The system follows an **asynchronous job-based processing model** to handle
long-running video intelligence workloads without blocking API requests.

### 1. Video Ingestion

1. Client submits a video URL via `POST /api/v1/videos`
2. API layer validates the request
3. Service layer creates a new job with status `UPLOADED`
4. Job metadata is persisted in the database
5. API responds immediately with a `video_id`

No heavy processing occurs at this stage.

### 2. Background Processing Trigger

1. Service layer triggers background processing
2. Job status transitions to `PROCESSING`
3. Background worker begins execution independently

### 3. Video Analysis Pipeline

The background worker performs:

* Video access / download
* Audio extraction (if applicable)
* AI pipeline execution:

  * Speech-to-text
  * NLP / vision analysis (extensible)
* Result generation and persistence

AI components remain **internal implementation details**.

### 4. Completion or Failure Handling

* On success:

  * Status → `COMPLETED`
  * Results persisted
* On failure:

  * Status → `FAILED`
  * Error information logged

Future extensions include retries and dead-letter handling.

### 5. Status Retrieval

Clients poll job status using:

```
GET /api/v1/videos/{video_id}
```

### Job State Transitions

```
UPLOADED → PROCESSING → COMPLETED
                 ↘
                  FAILED
```


## API Contracts

All endpoints are **versioned** to ensure backward-compatible evolution.

Base path:

```
/api/v1
```

### Health Check

**GET** `/health`

```json
{ "status": "ok" }
```


### Ingest Video

**POST** `/api/v1/videos`

```json
{
  "url": "https://example.com/video.mp4"
}
```

Response:

```json
{
  "video_id": "uuid",
  "status": "UPLOADED"
}
```


### Get Video Status

**GET** `/api/v1/videos/{video_id}`

```json
{
  "video_id": "uuid",
  "status": "PROCESSING",
  "created_at": "2026-02-06T10:15:30Z",
  "updated_at": "2026-02-06T10:17:12Z"
}
```


## Key Features

* Asynchronous video ingestion
* Background AI processing (extensible stubs)
* Explicit job lifecycle tracking
* PostgreSQL with SQLAlchemy ORM
* Dockerized development environment
* Automated tests with Pytest
* CI pipeline using GitHub Actions
* Live deployed backend (Render)


## Tech Stack

* **Backend**: FastAPI (Python 3.12)
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Async Processing**: Background tasks
* **Testing**: Pytest
* **CI/CD**: GitHub Actions
* **Containerization**: Docker & Docker Compose


## Quick Start

### Prerequisites

* Docker & Docker Compose
* Python 3.12+ (local development)
* PostgreSQL (managed via Docker)

### Clone & Run

```bash
git clone https://github.com/YashJagdale2122/video-intelligence-backend.git
cd video-intelligence-backend
cp .env.example .env
docker-compose up --build
```


## Live Demo

* API: [https://video-intelligence-backend.onrender.com](https://video-intelligence-backend.onrender.com)
* Docs: [https://video-intelligence-backend.onrender.com/docs](https://video-intelligence-backend.onrender.com/docs)
* Health: [https://video-intelligence-backend.onrender.com/health](https://video-intelligence-backend.onrender.com/health)

> Free-tier deployments may take 30–60 seconds to wake up.


## Testing

```bash
pytest
```

All tests run automatically via **GitHub Actions** on every push.


## Future Improvements

* Real AI pipeline integration (Whisper, vision models)
* Message queues (Kafka / RabbitMQ)
* Retry & failure policies
* Distributed workers
* Authentication & authorization
* Observability (metrics, tracing)
