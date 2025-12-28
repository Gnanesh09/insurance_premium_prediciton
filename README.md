# Insurance Premium Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green)
![Docker](https://img.shields.io/badge/Docker-Available-blue)
![AWS](https://img.shields.io/badge/AWS-Deployed-orange)

## 📖 Overview

This project is a Machine Learning application built to predict insurance premiums in real-time. It utilizes a trained **Scikit-learn** model served via a **FastAPI** backend. The application is containerized using **Docker** and is designed to be deployed on cloud platforms like **AWS**.

## 🚀 Features

- **Real-time Prediction**: Instant premium estimation based on user inputs.
- **FastAPI Framework**: High-performance, easy-to-use API framework.
- **Dockerized**: Fully containerized for consistent deployment environments.
- **Machine Learning**: Utilizes advanced regression techniques for accurate predictions.
- **Modular Design**: Codebase organized into config, model, and schema modules.

## 🛠️ Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **ML Library**: Scikit-learn, Pandas, NumPy
- **Containerization**: Docker
- **Deployment**: AWS (Elastic Container Registry / Elastic Beanstalk / EC2)

## 📂 Project Structure

```bash
insurance_premium_prediction/
├── config/              # Configuration files
├── model/               # Trained ML models and loading logic
├── schema/              # Pydantic schemas for data validation
├── app.py               # Main FastAPI application entry point
├── Dockerfile           # Docker build instructions
├── requirements.txt     # Python dependencies
└── .gitignore           # Git ignore file