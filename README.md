# Azure Progressive Delivery Pipeline

![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Bicep](https://img.shields.io/badge/Bicep-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)

## Live Demo
**[View Live Application](https://ghaith-fastapi-app.yellowplant-440f3719.swedencentral.azurecontainerapps.io)**

## Overview
Production-ready CI/CD pipeline with progressive delivery on Azure Container Apps. Features blue/green deployments, infrastructure as code, secrets management, and full observability.

## Architecture
| Component | Technology | Purpose |
| :--- | :--- | :--- |
| Container Registry | Azure Container Registry (ACR) | Private Docker image storage |
| Compute | Azure Container Apps | Serverless container hosting |
| CI/CD | GitHub Actions | Automated deployment pipeline |
| Secrets | Azure Key Vault | Secure secrets management |
| Monitoring | Azure Application Insights | Real-time observability |
| Infrastructure as Code | Bicep | Version-controlled infrastructure |

## Features
- Zero-downtime blue/green deployments via revision-based traffic switching
- Automated CI/CD pipeline with GitHub Actions supporting manual color selection
- Infrastructure as Code using Bicep modules for repeatable deployments
- Secrets management with Azure Key Vault and RBAC access policies
- Real-time observability through Application Insights with distributed tracing
- Health check endpoints for reliability monitoring and automated rollback capability

## Project Structure
.
├── .github/workflows/
│ └── deploy.yml # GitHub Actions CI/CD pipeline
├── main.bicep # Infrastructure as Code definition
├── main.py # FastAPI application
├── Dockerfile # Container image definition
└── requirements.txt # Python dependencies

## Pipeline Flow
Git Push → GitHub Actions → ACR Build & Push → Container Apps Update
↓
Revision Created
↓
Zero-Downtime Traffic Switch

## Authentication Note
The GitHub Actions workflow uses device code authentication (`az login --use-device-code`) due to university Azure AD tenant restrictions on service principal creation. In a production enterprise environment, this would be implemented using:
- OIDC Federated Credentials for passwordless authentication
- Managed Identities for Azure-to-Azure communication
- Service Principal with certificate-based authentication

This constraint demonstrates practical experience working within organizational security boundaries while maintaining deployment automation capabilities.

## Azure Resources Created
| Resource | Name | Purpose |
| :--- | :--- | :--- |
| Resource Group | `ghaith-azure-project-rg` | Logical container for all resources |
| Container Registry | `ghaithacr2026` | Private Docker image registry |
| Container Apps Environment | `ghaith-env` | Serverless container runtime |
| Container App | `ghaith-fastapi-app` | Application endpoint |
| Key Vault | `ghaith-kv` | Secrets storage |
| Application Insights | `ghaith-appinsights` | Monitoring and telemetry |

## Skills Demonstrated
- Azure Container Apps & Azure Container Registry
- GitHub Actions CI/CD pipeline design and implementation
- Infrastructure as Code using Bicep
- Blue/Green progressive delivery strategy
- Azure Key Vault secrets management with RBAC
- Application Insights observability and distributed tracing
- Docker containerization and multi-stage builds
- FastAPI REST API development
- YAML pipeline configuration
- Cloud resource troubleshooting and debugging

## Screenshots
<img width="1867" height="975" alt="Live App - BLUE Version" src="https://github.com/user-attachments/assets/e54907e6-3e0c-4457-b8d5-6741bfbd2d28" />
<img width="1865" height="974" alt="Live App - GREEN Version" src="https://github.com/user-attachments/assets/890e589d-e247-4269-8b80-3cf5bc29ddc2" />
<img width="1868" height="935" alt="Application Insights Dashboard" src="https://github.com/user-attachments/assets/72a86020-617d-4807-8f93-6538ae21be17" />
<img width="1867" height="980" alt="GitHub Actions Workflow Run" src="https://github.com/user-attachments/assets/4a2757a6-3630-44c0-a7b0-0bc77d2194e1" />
<img width="1869" height="931" alt="Azure Portal - Container App Overview" src="https://github.com/user-attachments/assets/7370a0eb-ee96-49d3-8a27-1739a7ded9dc" />
<img width="894" height="278" alt="Terminal - Bicep Output" src="https://github.com/user-attachments/assets/ba3c95ef-dba0-4bc4-8e1f-ac318c731f4f" />

## Author
**Ghaith Dhaouadi** - Cloud DevOps Engineer
