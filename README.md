# AI E-Commerce Platform

An AI-powered e-commerce platform inspired by modern online marketplaces. The project combines a scalable microservices architecture with artificial intelligence to deliver personalized product recommendations using semantic search, vector databases, and event-driven processing.

> **Current Status:** Sprint 3 Completed

---

# Features

## E-Commerce

* User Authentication (JWT)
* User Management
* Product Catalog
* Product Search
* Shopping Cart
* Order Management
* Payment Integration (Stripe - In Progress)

---

## AI Recommendation System

* Event-Driven Recommendation Pipeline
* User Behavior Tracking
* Product Snapshot Service
* User Profile Generation
* Content-Based Recommendation
* Semantic Search
* Vector Search with Qdrant
* Sentence Transformers Embeddings

---

## Infrastructure

* FastAPI Backend
* Next.js Frontend
* PostgreSQL
* RabbitMQ
* Redis
* MinIO
* Qdrant
* Docker
* Docker Compose

---

# Technology Stack

## Backend

* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* RabbitMQ
* Redis
* Pydantic

## Frontend

* Next.js
* React
* Tailwind CSS

## Artificial Intelligence

* Sentence Transformers
* Qdrant Vector Database
* Semantic Search
* Embedding Generation

## DevOps

* Docker
* Docker Compose
* Nginx (Planned)
* GitHub Actions (Planned)
* Kubernetes (Future)

---

# Project Architecture

```
                       +----------------------+
                       |      Frontend        |
                       |      Next.js         |
                       +----------+-----------+
                                  |
                                  |
                         REST API / JWT
                                  |
                                  |
                       +----------v-----------+
                       |      FastAPI         |
                       |       Backend        |
                       +----+----+-----+------+
                            |    |     |
                            |    |     |
          +-----------------+    |     +----------------+
          |                      |                      |
          |                      |                      |
+---------v-------+      +-------v-------+      +-------v--------+
|   PostgreSQL    |      |   RabbitMQ    |      |     Redis      |
+-----------------+      +-------+-------+      +----------------+
                                 |
                                 |
                                 v
                +--------------------------------+
                | Recommendation Service         |
                | FastAPI Microservice           |
                +---------------+----------------+
                                |
             +------------------+------------------+
             |                                     |
             |                                     |
     +-------v-------+                     +-------v-------+
     |    Qdrant     |                     | Sentence      |
     | Vector DB     |                     | Transformers  |
     +---------------+                     +---------------+
```

---

# Recommendation Pipeline

```
User Action
      │
      ▼
RabbitMQ Event
      │
      ▼
Recommendation Worker
      │
      ▼
Store User Event
      │
      ▼
Update User Profile
      │
      ▼
Generate Recommendations
      │
      ▼
Store Recommendations
```

---

# Repository Structure

```
backend/
frontend/
services/
    recommendation-service/

docs/
infrastructure/

docker-compose.yml
README.md
```

---

# Completed Sprints

## Sprint 1

* Authentication
* Products
* Orders
* Database
* Docker Setup

## Sprint 2

* Event-Driven Architecture
* Recommendation Pipeline
* Product Snapshots
* User Profiles

## Sprint 3

* Semantic Search
* Vector Database (Qdrant)
* Embedding Generation
* AI Recommendation Engine

---

# Roadmap

## Sprint 4

* Hybrid Recommendation Engine
* User Embeddings
* Product Embeddings
* Vector Ranking
* Popularity Ranking

## Sprint 5

* LLM Shopping Assistant
* Conversational AI
* Personalized Search

## Sprint 6

* RAG (Retrieval-Augmented Generation)

## Sprint 7

* MLOps Pipeline

## Sprint 8

* Kubernetes Deployment

## Sprint 9

* Monitoring & Observability

## Sprint 10

* Production Deployment

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/your-username/ai-ecommerce-platform.git
```

## Start Services

```bash
docker compose up -d
```

## Backend

```
http://localhost:8000
```

## Frontend

```
http://localhost:3000
```

---

# Future Goals

* AI Shopping Assistant
* Multi-Modal Search
* Recommendation Ranking Models
* Real-Time Recommendations
* Production Ready Deployment
* Cloud Native Architecture

---

# License

This project is developed for learning, research, and portfolio purposes.
