# 🚀 QR Code Generator – CI/CD Enabled DevOps Project

A **full-stack QR Code Generator web application** built using **HTML, CSS, JavaScript (Frontend)** and **FastAPI (Backend)**, fully **containerized with Docker** and **automatically deployed on AWS EC2 using Jenkins CI/CD pipeline**.

This project demonstrates **real-world DevOps practices** including containerization, cloud deployment, and continuous integration & delivery.

---

## 📌 Features
✅ Generate QR codes instantly  
✅ Download generated QR codes  
✅ Responsive and user-friendly UI  
✅ FastAPI-powered backend  
✅ Dockerized application  
✅ Automated CI/CD using Jenkins  
✅ Deployed on AWS EC2  
✅ Auto redeploy on every GitHub push  

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
- qrcode (Pillow)  
- CORS Middleware  

### **DevOps & Cloud**
- Docker  
- Jenkins (CI/CD Pipeline)  
- GitHub  
- AWS EC2 (Ubuntu)  

---

## 🧩 Project Architecture (High Level)

![Home Page](https://github.com/SaiDivakar-Navara/QR-Code-Generator/blob/main/Frontend/image.png)


## 📂 Project Structure
```
📁 qr-code-generator
│── 📂 frontend
│   ├── index.html        # Frontend UI
│   ├── style.css         # Frontend styling
│   ├── script.js         # JavaScript (Handles API requests)
│── 📂 backend
│   ├── main.py             # FastAPI Backend
│   ├── requirements.txt    # Python dependencies  
│── Dockerfile               # Docker Configuration     
│── README.md               # Project Documentation     
```


---

### ☁️ Deployment on AWS EC2
- Deployment Steps
- Created Ubuntu EC2 instance
- Installed Docker and Jenkins
- Opened port 8000 in Security Group
- Deployed application using Docker container
- Jenkins handles automated redeployment
  
    Live URL:

        http://<EC2-PUBLIC-IP>:8000/


### 🔄 CI/CD Pipeline Using Jenkins
- CI/CD Workflow
- Developer pushes code to GitHub
- Jenkins pulls the latest code
- Docker image is built
- Old container is stopped
- New container is deployed automatically
- Jenkins Pipeline Stages
- Clone Repository
- Build Docker Image
- Deploy Docker Container


###  📜 License

    This project is licensed under the MIT License.

### 👨‍💻 Author

    Sai Divakar Navara  
    📧 Email: saidivakar.navara@gmail.com

🔗 GitHub: https://github.com/SaiDivakar-Navara


### Thank You!!!
