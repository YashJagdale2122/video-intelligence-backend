## Video Intelligence Backend

![CI](https://github.com/YashJagdale2122/video-intelligence-backend/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Postgres](https://img.shields.io/badge/database-postgresql-blue)


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


## Running Locally

```bash
docker-compose up --build

API will be available at:
http://localhost:8000
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

Get Video Status:

GET `/api/v1/videos/{video_id}`
 ```
 
 
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
