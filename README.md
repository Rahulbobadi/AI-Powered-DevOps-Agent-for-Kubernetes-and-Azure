# AI-Powered-DevOps-Agent-for-Kubernetes-and-Azure

# AI DevOps Agent 🚀

An AI-powered DevOps chatbot that manages Kubernetes and Azure resources using natural language commands.

## Overview

AI DevOps Agent provides a conversational interface for performing common DevOps operations across Kubernetes and Azure Cloud.

Instead of manually executing kubectl and Azure CLI commands, users can interact with the platform through a simple chatbot UI.

Example commands:

* Check cluster health
* Create deployment nginx-demo
* Delete deployment nginx-demo
* Create storage account mlopsdemo123
* List storage
* Create registry mlopsacr001
* Delete registry mlopsacr001

---

## Architecture

```text
User
  |
  v
Streamlit UI
  |
  v
Agent Router (agent.py)
  |
  +-----------------------+
  |                       |
  v                       v
k8s_tools.py         azure_tools.py
  |                       |
  v                       v
Kubernetes API      Azure CLI
  |                       |
  v                       v
Minikube Cluster    Azure Resources
```

---

## Technologies Used

### DevOps & Cloud

* Kubernetes
* Minikube
* Docker
* Azure CLI
* Azure Storage Accounts
* Azure Container Registry (ACR)

### Development

* Python 3.11
* Streamlit
* Kubernetes Python Client

### Security

* Service Accounts
* ClusterRole
* ClusterRoleBinding
* RBAC

### Future Enhancements

* Ollama
* LLM Tool Calling
* Azure Managed Identity
* Multi-Agent Architecture
* MLOps Automation

---

## Features

### Kubernetes Operations

* Check cluster health
* Create deployments
* Delete deployments
* List running workloads

### Azure Operations

* Create Storage Account
* List Storage Accounts
* Delete Storage Account
* Create Azure Container Registry
* List Registries
* Delete Registry

---

## Project Structure

```text
ai-devops-agent/
│
├── app.py
├── agent.py
│
├── agents/
│   ├── k8s_tools.py
│   └── azure_tools.py
│
├── deployment.yaml
├── service.yaml
├── rbac.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Deployment

### Build Docker Image

```bash
docker build -t ai-devops-agent:v1 .
```

### Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f rbac.yaml
```

### Verify Deployment

```bash
kubectl get pods
kubectl get svc
```

---

## Example Commands

### Kubernetes

```text
Check cluster health
```

```text
Create deployment nginx-demo
```

```text
Delete deployment nginx-demo
```

### Azure

```text
List storage
```

```text
Create storage account mlopsdemo123
```

```text
Delete storage account mlopsdemo123
```

```text
List registries
```

```text
Create registry mlopsacr001
```

```text
Delete registry mlopsacr001
```

---

## RBAC Configuration

The application accesses the Kubernetes API using a dedicated ServiceAccount.

Components:

* ServiceAccount
* ClusterRole
* ClusterRoleBinding

This enables the chatbot to securely interact with cluster resources.

---

## Troubleshooting

### Kubernetes Permission Error

Error:

```text
403 Forbidden
```

Resolution:

Configure ServiceAccount, ClusterRole, and ClusterRoleBinding.

---

### Azure Login Required

Error:

```text
Please run 'az login'
```

Resolution:

```bash
az login
```

Future enhancement:

* Managed Identity
* Service Principal Authentication

---

### Disk Space Issues

Error:

```text
No space left on device
```

Resolution:

```bash
docker system prune -a -f
```

Check disk usage:

```bash
df -h
```

---

## CI/CD Roadmap

Planned GitHub Actions workflow:

1. Code Push
2. Build Docker Image
3. Push to Azure Container Registry
4. Deploy to Kubernetes
5. Verify Deployment

---

## Future Roadmap

### Phase 1

* Kubernetes Agent
* Azure Agent

### Phase 2

* GitHub Actions CI/CD
* ACR Integration

### Phase 3

* Ollama Integration
* Tool Calling
* AI-based Intent Detection

### Phase 4

* MLOps Automation
* MLflow Deployment
* Model Registry
* Monitoring Agent

---

## Learning Outcomes

This project demonstrates:

* Kubernetes API Automation
* Azure Resource Provisioning
* RBAC and Security
* Containerization
* Cloud Authentication
* AI Agent Architecture
* DevOps Automation

---

## Author

Rahul Bobadi

AI | DevOps | Kubernetes | Azure | Cloud Automation
