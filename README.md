# 🚀 fastapi-helm-k8s-starter

A production-ready **FastAPI** microservice starter template, fully containerized with **Docker**, deployed on **Kubernetes** using **Helm** charts, including **Ingress**, health checks, and scalable deployment setup. Perfect for building and deploying modern FastAPI apps quickly and reliably.

---

## 🎯 Project Overview

This starter project provides a robust, scalable foundation for your FastAPI microservices in a Kubernetes environment with:

- 🐍 **FastAPI** framework for high-performance, easy-to-build APIs  
- 🐳 **Docker** containerization for consistent environments  
- ☸️ **Kubernetes Deployment** for scalable and resilient microservice orchestration  
- 📦 **Helm Chart** for simple, repeatable deployments and version control  
- 🩺 **Health Checks** (Liveness & Readiness probes) for automatic pod management  
- 🌐 **Nginx Ingress Controller** integration with path rewriting and routing  
- 🔄 Configurable replicas for load balancing and high availability  
- 🔒 Configurable image pull policies for flexible deployment workflows  

---

## ⚙️ Key Features

- **Scalable Deployment:** Easily adjust replica counts to match your workload needs.  
- **Self-healing:** Kubernetes restarts failed containers automatically based on health checks.  
- **Ingress Routing:** Manage external traffic routing via hostname with SSL termination options.  
- **Configurable via Helm:** Customize your deployment through values.yaml without changing code.  
- **Production-grade:** Implements best practices for containerized API deployment.  
- **Lightweight:** Uses `python:3.10-slim` base image for minimal resource consumption.

---

## 🚀 Getting Started

1. **Build Docker Image**  
   Containerize your FastAPI application with a Dockerfile optimized for production.

2. **Deploy with Helm**  
   Use Helm to install and manage the deployment on your Kubernetes cluster.

3. **Access the API**  
   Access your FastAPI service externally via the configured Ingress hostname.

4. **Monitor and Scale**  
   Leverage Kubernetes tooling to monitor pods and scale replicas as required.

---

## 🛠️ Configuration

All deployment parameters are fully configurable via the Helm `values.yaml` file, including:

- Replica count  
- Docker image repository, tag, and pull policy  
- Service type and port  
- Ingress hostname and enabled flag  

---

## 🌟 Benefits

- Rapid setup for FastAPI microservices on Kubernetes  
- Modular Helm charts for easy integration into CI/CD pipelines  
- Health checks to ensure application uptime and reliability  
- Flexible ingress configuration for different environments  
- Supports both local and cloud Kubernetes clusters  

---

