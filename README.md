# 🚀 AI-Powered Spam Detection Platform

## 📌 Overview

A scalable backend system for detecting spam phone numbers using Machine Learning and AI.

## ⚙️ Features

- Phone number lookup
- Spam detection using ML
- GenAI-based explanation
- REST APIs (Django DRF)
- Dockerized deployment
- CI/CD pipeline (GitHub Actions)

## 🧠 Tech Stack

- Python, Django, DRF
- Machine Learning (TF-IDF, Naive Bayes)
- Docker
- GitHub Actions
- AWS EC2

## 🏗️ Architecture

- Backend API
- ML Engine
- Docker containerization
- CI/CD automation

## 🚀 How to Run

```bash
git clone <repo>
cd docker
docker-compose up --build


📡 API Endpoints
Lookup

GET /api/spam/lookup/?number=1234567890

Report Spam

POST /api/spam/report/

📈 Future Enhancements
Redis caching
Celery async processing
React frontend
