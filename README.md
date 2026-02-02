## Video Intelligence Backend

![CI](https://github.com/YashJagdale2122/video-intelligence-backend/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Postgres](https://img.shields.io/badge/database-postgresql-blue)
[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://video-intelligence-backend.onrender.com/docs)


**🚀 [Live Demo](https://video-intelligence-backend.onrender.com/docs)** | **📖 [API Docs](https://video-intelligence-backend.onrender.com/docs)** | **❤️ [Health Check](https://video-intelligence-backend.onrender.com/health)**

## Problem Statement

Modern video platforms require automated analysis of large volumes of video content.
This includes transcription, visual understanding, and risk assessment — all of which
are time-consuming and unsuitable for synchronous processing.


## Solution Overview

This project implements a modular FastAPI backend that ingests videos and processes
them asynchronously using an AI pipeline. The system is designed for scalability,
clear separation of concerns, and production readiness.


## Architecture

The design follows a layered architecture to ensure testability, maintainability, and clear separation of concerns.

- **API Layer**: FastAPI routes handling HTTP requests
- **Service Layer**: Business logic and orchestration
- **Repository Layer**: Database access using SQLAlchemy
- **Domain Layer**: Enums and domain models
- **Infrastructure Layer**: Database and background processing

```bash
Client → API → Service → Repository → Database
                   ↓
             Background Worker (AI processing)

```


## Key Features

- Asynchronous video ingestion
- Background AI processing (stubbed for extensibility)
- Status tracking using enums
- PostgreSQL with SQLAlchemy ORM
- Dockerized development environment
- Automated tests with Pytest
- CI pipeline using GitHub Actions


## Tech Stack

- **Backend**: FastAPI (Python 3.12)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Async Processing**: Background tasks
- **Testing**: Pytest
- **CI/CD**: GitHub Actions
- **Containerization**: Docker & Docker Compose

## Quick Start

### Prerequisites

- Docker & Docker Compose installed
- Python 3.12+ (for local development without Docker)
- PostgreSQL (handled by Docker Compose)

### 1. Clone the Repository
```bash
git clone https://github.com/YashJagdale2122/video-intelligence-backend.git
cd video-intelligence-backend
```

### 2. Environment Setup

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` with your configuration (defaults work for local development).

### 3. Start the Services
```bash
docker-compose up --build
```

The API will be available at:
- **API Base**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### 4. Test the API

Using curl:
```bash
# Health check
curl http://localhost:8000/health

# Ingest a video
curl -X POST "http://localhost:8000/api/v1/videos" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/video.mp4"}'

# Check video status (replace {video_id} with actual ID)
curl http://localhost:8000/api/v1/videos/{video_id}
```

Using the Swagger UI:
1. Navigate to http://localhost:8000/docs
2. Try the `/health` endpoint first
3. Use the interactive interface to test video ingestion

### 5. Stop the Services
```bash
docker-compose down
```

To stop and remove volumes (database data):
```bash
docker-compose down -v
```


## Live Demo

The application is deployed and running at:
- **Live API**: https://video-intelligence-backend.onrender.com
- **Interactive Docs**: https://video-intelligence-backend.onrender.com/docs
- **Health Check**: https://video-intelligence-backend.onrender.com/health

> **Note**: The free tier may take 30-60 seconds to wake up on first request.

### Try it out:
```bash
# Check if service is healthy
curl https://video-intelligence-backend.onrender.com/health

# Ingest a video (interactive testing via Swagger UI recommended)
open https://video-intelligence-backend.onrender.com/docs
```


## API Example

### Ingest Video
POST `/api/v1/videos`

Response:
```json
{
  "video_id": "uuid",
  "status": "UPLOADED"
}
```
### Get Video Status
GET `/api/v1/videos/{video_id}`

 
 
 ## Testing
 
 ```bash
 pytest
 ```
 All tests are automatically executed via GitHub Actions on every push.

 
 ## Future Improvements
 
 - Real AI pipeline integration
 - Message queue (Kafka / RabbitMQ)
 - Retry & failure handling
 - Improved test coverage
 - API authentication
