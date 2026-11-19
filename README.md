# 🚀 QR Code Generator – CI/CD & GitOps Enabled DevOps Project

A **full-stack QR Code Generator web application** built using **HTML, CSS, JavaScript (Frontend)** and **FastAPI (Backend)**, fully **containerized with Docker**, packaged with **Helm**, automated with **GitHub Actions (CI)**, and **continuously deployed on AWS EKS using ArgoCD (GitOps)**.

This project demonstrates **real-world cloud-native DevOps & GitOps practices** including automated testing, code quality checks, container image versioning, Helm chart updates, and declarative Kubernetes deployments.

---

## 📌 Features
✅ Generate QR codes instantly  
✅ Download generated QR codes  
✅ Responsive and user-friendly UI  
✅ FastAPI-powered backend with automated `pytest` suite  
✅ Dockerized multi-component application  
✅ Automated CI pipeline using GitHub Actions  
✅ Automated Helm chart image tag updates (`[skip ci]` loop prevention)  
✅ GitOps-driven Continuous Deployment (CD) on AWS EKS via ArgoCD  

---

## 🛠️ Technologies Used

### **Frontend**
- HTML5  
- CSS3  
- JavaScript  

### **Backend**
- Python  
- FastAPI  
- Uvicorn  
- `pytest` (Automated Testing)  
- `qrcode` (Pillow)  
- CORS Middleware  

### **DevOps, GitOps & Cloud**
- Docker  
- GitHub Actions (CI Pipeline)  
- Helm (Kubernetes Package Manager)  
- ArgoCD (GitOps CD)  
- AWS EKS (Managed Kubernetes)  
- GitHub  

---

## 🧩 Project Architecture (High Level)

```text
Developer Push (GitHub)
        │
        ▼
┌────────────────────────────────────────────────────────┐
│              GitHub Actions (CI Pipeline)              │
│  1. Build & Test (pytest)                              │
│  2. Code Quality Check                                 │
│  3. Build & Push Docker Image to Registry              │
│  4. Update Helm Chart with New Docker Tag [skip ci]    │
└────────────────────────────────────────────────────────┘
        │
        ▼  (Updated Helm values.yaml in Git)
┌────────────────────────────────────────────────────────┐
│               ArgoCD (GitOps CD on EKS)                │
│  • Detects Helm manifest change in Git                 │
│  • Automatically syncs & rolls out pods on AWS EKS     │
└────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```text
📁 QR-Code-Generator
│── 📂 .github
│   └── 📂 workflows
│       └── ci.yml              # GitHub Actions CI Pipeline
│── 📂 Frontend
│   ├── index.html              # Frontend UI
│   ├── style.css               # Frontend styling
│   └── script.js               # JavaScript (Handles API requests)
│── 📂 Backend
│   ├── __init__.py
│   ├── main.py                 # FastAPI Backend
│   ├── requirements.txt        # Python dependencies
│   └── 📂 tests
│       └── test_main.py        # Pytest unit & API tests
│── 📂 helm                     # Helm Chart for Kubernetes deployment
│   ├── Chart.yaml
│   ├── values.yaml             # Updated automatically with new Docker tags
│   └── 📂 templates
│── Dockerfile                  # Docker Configuration
│── README.md                   # Project Documentation
```

---

### 🔄 CI Pipeline Using GitHub Actions
- **CI Workflow**
  - Developer pushes code to `main` branch on GitHub
  - GitHub Actions triggers the **CI Pipeline** automatically
  - Runs unit & API tests using `python -m pytest Backend/ -v`
  - Executes code quality & linting checks
  - Builds Docker image tagged with the run/commit ID and pushes it to the container registry
  - Updates the Docker image tag inside the Helm chart (`values.yaml`) and commits back with `[skip ci]` to prevent infinite pipeline loops
- **CI Pipeline Stages**
  - Build and Test
  - Code Quality Check
  - Build and Push Docker Image
  - Update Helm Chart with New Docker Tag

---

### ☁️ GitOps CD Deployment on AWS EKS Using ArgoCD
- **Deployment Steps**
  - Provisioned an **AWS EKS** cluster and configured `kubectl`
  - Installed and configured **ArgoCD** inside the EKS cluster
  - Created an ArgoCD `Application` pointing to this repository's Helm chart path
  - Enabled automated sync (`selfHeal` & `prune`) so ArgoCD continuously monitors Git for Helm tag updates
  - Exposed the application via Kubernetes Service / Ingress LoadBalancer
- **GitOps CD Workflow**
  - CI pipeline commits the updated Docker image tag to the Helm chart
  - ArgoCD detects the Git drift automatically
  - ArgoCD performs a rolling update on **AWS EKS** with zero manual `kubectl` intervention

---

### 📜 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

**Sai Divakar Navara**  
📧 Email: saidivakar.navara@gmail.com  
🔗 GitHub: [https://github.com/SaiDivakar-Navara](https://github.com/SaiDivakar-Navara)  

---

### Thank You!!!