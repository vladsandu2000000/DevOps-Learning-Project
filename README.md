## SPA Salon Management System

This is a Django web application containerized with **Docker** and deployed to an **Azure Linux VM** using **GitHub Actions CI/CD**.

---

## Architecture

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +--> Build Docker image
    +--> Push image to Docker Hub
    +--> SSH into Azure VM
    v
Azure Ubuntu VM
    |
    v
Docker Compose
    |
    +--> Django container
    +--> PostgreSQL container
```

---

## Tech Stack

* **Backend:** Python / Django 6.0
* **Database:** PostgreSQL 15
* **Containers:** Docker & Docker Compose
* **Cloud:** Azure Virtual Machine (Ubuntu 24.04)
* **CI/CD:** GitHub Actions & Docker Hub

---

## How the CI/CD Pipeline Works

When code is pushed to the `main` branch, GitHub Actions automatically:

1. Builds the Docker image for the Django app.
2. Pushes the image to Docker Hub.
3. Connects to the Azure VM via SSH.
4. Pulls the latest code and updates the containers using `docker compose`.
5. Runs database migrations (`python manage.py migrate`).

---

## How to Run Locally

If you want to run this project on your machine using Docker:

### 1. Clone the repository

git clone https://github.com/vladsandu2000000/DevOps-Learning-Project.git 
cd DevOps-Learning-Project

### 2. Start the application

docker compose up -d --build

### 3. Run migrations and create an admin user

docker compose exec web python spa_salon/manage.py migrate
docker compose exec web python spa_salon/manage.py createsuperuser

Open your browser and go to ⁠http://localhost:8000⁠ or ⁠http://localhost:8000/admin⁠.
