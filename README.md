# Advertising Sales MLOps Pipeline

## Project Overview

This project implements an end-to-end Machine Learning pipeline using GitHub Actions, Docker, Flask API, and Kubernetes.

The system predicts product sales based on TV, Radio, and Newspaper advertising budgets using a Linear Regression machine learning model.

The project demonstrates:

- Data preprocessing
- Model training and testing
- Flask API deployment
- Docker containerisation
- Continuous Integration (CI)
- Continuous Delivery (CD)
- Continuous Deployment
- Kubernetes deployment using Kind
- Automated deployment using GitHub Actions

---

# Machine Learning Pipeline

The pipeline used in this project is shown below:

Raw Dataset  
↓  
Data Preprocessing  
↓  
Cleaned Dataset  
↓  
Model Training & Testing  
↓  
Saved Machine Learning Model  
↓  
Flask API Deployment  
↓  
Docker Containerisation  
↓  
GitHub Actions CI/CD  
↓  
Docker Hub  
↓  
Google VM / Kind Kubernetes Deployment  

---

# Project Structure

```text
advertising-sales-mlops/
│
├── app/
│   └── flaskapp.py
│
├── data/
│   └── Advertising_And_Sales.csv
│
├── src/
│   ├── preprocess.py
│   └── train.py
│
├── models/
│   └── sales_model.pkl
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── docker-publish.yml
│       ├── deploy.yml
│       └── k8s-deploy.yml
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Docker
- GitHub Actions
- Docker Hub
- Kubernetes (Kind)
- Google Cloud VM

---

# Branching Strategy

This project uses a simple branching strategy:

- `dev` → development branch
- `testing` → validation/testing branch
- `main` → stable production branch

Changes move from:

```text
dev → testing → main
```

Only validated and tested changes should be merged into the `main` branch.

---

# Model Training

The machine learning model was developed using:

- Linear Regression
- Train/Test split
- MAE evaluation metric
- R² score evaluation

Input Features:

- TV advertising budget
- Radio advertising budget
- Newspaper advertising budget

Target:

- Sales

---

# Flask API

The trained model is deployed through a Flask API.

Example endpoint:

```text
/predict?tv=100&radio=20&newspaper=10
```

Example response:

```json
{
  "tv": 100.0,
  "radio": 20.0,
  "newspaper": 10.0,
  "predicted_sales": 11.29
}
```

---

# Docker Deployment

The Flask API and trained machine learning model were containerised using Docker.

The Docker image was automatically built and pushed to Docker Hub using GitHub Actions.

Docker Hub Image:

<img width="1232" height="710" alt="Screenshot 2026-05-24 at 01 50 47" src="https://github.com/user-attachments/assets/f979dd85-8f98-4a84-a235-db647051106e" />


---

# Kubernetes Deployment

The Flask application was deployed to a Kind Kubernetes cluster running on a Google Cloud VM.

Kubernetes manages:

- Pod creation
- Container orchestration
- Networking
- Service exposure

The application was deployed using:

- `deployment.yaml`
- `service.yaml`

---

# GitHub Actions Workflows

## CI Pipeline

Automatically runs:

- dependency installation
- preprocessing
- model training

after code pushes.

---

## Publish Docker Image

Automatically:

- builds Docker image
- pushes image to Docker Hub

---

## Deploy Flask App

Automatically:

- pulls latest Docker image
- redeploys container on Google VM

---

## Deploy to Kind Kubernetes

Automatically deploys the Flask application to the Kubernetes cluster using:

```text
kubectl apply
```

---

# Screenshots

## GitHub Actions Workflows

<img width="1542" height="809" alt="Screenshot 2026-05-24 at 01 36 45" src="https://github.com/user-attachments/assets/80e802b5-63dd-4bf3-8826-c6b3e74fbc66" />

---

## Self-Hosted Runner

<img width="890" height="298" alt="Screenshot 2026-05-24 at 01 38 19" src="https://github.com/user-attachments/assets/c31218c1-7076-4c17-bd42-f0997dd70020" />

---

## Docker Containers Running

<img width="1682" height="603" alt="Screenshot 2026-05-24 at 01 33 15" src="https://github.com/user-attachments/assets/586a1c0e-8d17-472e-b1f4-202a89cdc392" />

---

## Kubernetes Deployment

<img width="833" height="621" alt="Screenshot 2026-05-24 at 01 28 04" src="https://github.com/user-attachments/assets/a340e95a-f47d-4d8c-a042-48a5e4b849e9" />

---

## Flask API Prediction Through Kubernetes

<img width="1188" height="743" alt="Screenshot 2026-05-24 at 01 29 26" src="https://github.com/user-attachments/assets/27b89a85-0d2e-416b-a70e-4f0eae379283" />


---

## Flask API Home Page

<img width="1194" height="745" alt="Screenshot 2026-05-24 at 01 34 36" src="https://github.com/user-attachments/assets/772c7fab-f122-489d-9e75-3cb1c0389439" />


---

# Continuous Integration and Deployment Flow

```text
Developer pushes code to GitHub
        ↓
GitHub Actions CI Pipeline runs
        ↓
Model preprocessing and training
        ↓
Docker image built automatically
        ↓
Docker image pushed to Docker Hub
        ↓
Deployment workflow runs on self-hosted VM
        ↓
Kubernetes deploys Flask API containers
        ↓
Users access prediction API
```

---

# Deployment Architecture

```text
GitHub Actions
        ↓
Self-Hosted Runner (Google VM)
        ↓
Docker / Kubernetes Deployment
        ↓
Flask API Pods
        ↓
Machine Learning Predictions
```

---

# Author
Mohamed Abdelnasser

