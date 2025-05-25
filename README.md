
---

# 🚀 fastapi-helm-k8s-starter

A production-grade **FastAPI** microservice template, built for scalable deployment on **Kubernetes** using **Docker** and **Helm**, complete with health checks, ingress routing, and automated **CI/CD via GitHub Actions**. Perfect for kickstarting modern, container-native API services.

---

## 🎯 Project Overview

This project is a robust foundation to develop and deploy FastAPI-based microservices with:

* **FastAPI** for building high-performance REST APIs
* **Docker** for packaging the application into lightweight containers
* **Kubernetes** for managing containerized services in a scalable, resilient way
* **Helm** for templated, configurable Kubernetes deployments
* **Health Probes** for automatic container restarts and traffic management
* **Nginx Ingress Controller** for clean routing with custom domain support
* **GitHub Actions CI/CD** for automatic Docker builds and DockerHub deployment

---

## ⚙️ Key Features

* 🔁 **Scalable Kubernetes Deployments** with configurable replica counts
* 🩺 **Liveness & Readiness Probes** for Kubernetes-managed health checks
* 🌐 **Ingress Support** for routing traffic to the service using a domain name
* 🐳 **Optimized Docker Image** based on a slim Python base
* 🔄 **Image Pull Policy Configuration** for flexible deployment environments
* 🤖 **CI/CD Integration** to automate Docker image builds and publishing
* 🧩 **Helm Charts** for modular, repeatable Kubernetes deployments
* 🧼 **Clean Architecture** separating code, config, and CI/CD logic

---

## 🚀 Getting Started Workflow

1. **Build and containerize the FastAPI application**
2. **Deploy the application to a Kubernetes cluster using Helm**
3. **Access the app via domain-based Ingress routing**
4. **Verify application health via HTTP endpoints**
5. **Monitor and manage pods through Kubernetes commands**
6. **Push changes to GitHub and let CI/CD handle image builds and DockerHub publishing**

---

## ⚙️ Configuration Highlights

All key deployment parameters like replicas, ports, domain name, and Docker image settings are easily customizable using a values configuration file—no need to modify the codebase itself.

---

## 🤖 CI/CD with GitHub Actions

This project comes with a pre-configured GitHub Actions pipeline that:

* Triggers on every push to the main branch
* Builds a new Docker image
* Pushes it to DockerHub under the configured repository
* Keeps your production deployments up-to-date automatically

---

## 🌟 Benefits

* ⏱️ **Rapid Bootstrap**: Start building production APIs in minutes
* 🔄 **Automated Deployments**: CI/CD ensures delivery is fast and consistent
* 🧱 **Modular and Maintainable**: Helm and Docker separate logic from infrastructure
* ☁️ **Cloud Ready**: Works in any CNCF-compliant Kubernetes cluster
* 📦 **Reusable Template**: Use it for any FastAPI-based project needing Kubernetes deployment

---
