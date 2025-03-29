# QR Code Generator 🚀

A simple **QR Code Generator** built with **HTML, CSS, JavaScript (Frontend)** and **FastAPI (Backend in Python)**. This application allows users to generate QR codes from the frontend and display the generated image dynamically.

## 📌 Features
✅ Generate QR codes instantly  
✅ Download the generated QR code  
✅ Modern & Responsive UI  
✅ Fast and lightweight backend using FastAPI  
✅ CORS-enabled API for smooth frontend-backend communication  

---

## 🛠️ Technologies Used
### **Frontend:**
- HTML5  
- CSS3 (Responsive Design)  
- JavaScript (Fetch API for backend communication)  

### **Backend:**
- Python  
- FastAPI (for API handling)  
- qrcode library (for generating QR codes)  
- Uvicorn (to run FastAPI server)  
- CORS Middleware (for frontend-backend integration)  

---

## ⚙️ Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/SaiDivakar-Navara/QR-Code-Generator.git
cd qrcode-generator
```

### **2️⃣ Set Up Python Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r backend/requirements.txt
```

### **4️⃣ Run the FastAPI Server**
```sh
uvicorn main:app --reload
```
This starts the backend at:  
➡ **http://127.0.0.1:8000**

---

## 🖥️ Running the Frontend
### **1️⃣ Open `index.html`**
Simply open the `index.html` file in your browser.

### **OR** Start a Local HTTP Server
```sh
# Python 3.x
python -m http.server 5500
```
Then open **http://127.0.0.1:5500** in your browser.

---

## 🚀 Usage
1️⃣ Enter text in the input box.  
2️⃣ Click **"Generate QR Code"** to get the QR image.  
3️⃣ Click **"Download QR Code"** to save the image.  

---

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
│── README.md               # Project Documentation     
```

---

## 🔗 API Endpoints
### **1️⃣ Generate QR Code**
```
GET /generate_qr/?data=YourTextHere
```
**Response:** Returns the QR code image.

---

## 📜 License
This project is **open-source** under the **MIT License**.

---

## 🎯 Author
👨‍💻 Developed by **[Sai Divakar Navara]**  
📧 Contact: saidivakar.navara@gmail.com 
🔗 GitHub: [Your GitHub Profile](https://github.com/SaiDivakar-Navara)

---

🎉 **Now, you’re all set to generate and download QR codes with ease!** 🚀
