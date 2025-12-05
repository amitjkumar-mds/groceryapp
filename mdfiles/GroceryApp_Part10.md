
# Grocery Application – Requirements & Architecture Document  
## **Part 10 – Deployment Guide, Folder Structure & Setup Instructions**

---

# **PART 10 – Deployment Guide & Setup Instructions (Local Desktop App)**

This document describes *exactly how to install, configure, and run* the Grocery Shopping Application (Phase 1 – Local Desktop Application).

It includes:
- Folder structure  
- Installation steps  
- Dependency setup  
- MongoDB setup  
- Running frontend + backend  
- Environment variables  
- Debugging instructions  
- Packaging for local distribution  

---

# **TABLE OF CONTENTS (PART 10)**

1. Overview  
2. Folder Structure  
3. Prerequisites  
4. Backend (FastAPI) Setup  
5. Frontend (React + TypeScript) Setup  
6. MongoDB Local Setup  
7. Running the Application (Full System)  
8. Environment Variables  
9. LLM Integration Setup  
10. Packaging App for Local Distribution  
11. Logging & Debugging  
12. Backup & Restore (DB + Bill Images)  
13. Next Steps (Future Deployment Path)  

---

# **1. OVERVIEW**

The application consists of:

- **Frontend:** React + TypeScript  
- **Backend:** FastAPI (Python)  
- **Database:** MongoDB (local)  
- **AI Layer:** ChatGPT Vision API  
- **Storage:** GridFS (inside MongoDB for storing bill images)  

The entire solution runs **locally on your laptop**.

---

# **2. FOLDER STRUCTURE**

```
grocery-app/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── categories.py
│   │   │   ├── items.py
│   │   │   ├── shopping_lists.py
│   │   │   ├── actuals.py
│   │   │   ├── bills.py
│   │   │   └── ml.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── llm_client.py
│   │   ├── models/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── tests/
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── App.tsx
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── docs/
│   └── All markdown design docs (Parts 1–10)
│
└── env/
    └── .env.example
```

---

# **3. PREREQUISITES**

Install the following on your laptop:

| Component | Version |
|----------|----------|
| Python | 3.10 or higher |
| Node.js | 18+ |
| MongoDB Community Edition | Latest |
| Git | Latest |
| VS Code | Recommended |
| OpenAI API Key | Required for LLM |

---

# **4. BACKEND SETUP (FASTAPI)**

### **Step 1: Navigate to backend folder**
```
cd grocery-app/backend
```

### **Step 2: Create and activate virtual environment**
Windows:
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install dependencies**
```
pip install -r requirements.txt
```

### **Step 4: Start FastAPI server**
```
uvicorn app.main:app --reload --port 8000
```

### Backend now runs at:
👉 http://localhost:8000  
👉 API docs: http://localhost:8000/docs  

---

# **5. FRONTEND SETUP (REACT + TYPESCRIPT)**

### **Step 1: Navigate**
```
cd grocery-app/frontend
```

### **Step 2: Install dependencies**
```
npm install
```

### **Step 3: Start frontend**
```
npm start
```

### Frontend runs at:
👉 http://localhost:3000  

---

# **6. MONGODB LOCAL SETUP**

### Option 1: Install MongoDB Community Edition  
Download from:
https://www.mongodb.com/try/download/community

### Option 2: Run via Docker (optional)
```
docker run -d -p 27017:27017 --name grocery-mongo mongo:latest
```

### **Create database & GridFS collections**
FastAPI will auto-create required collections on first run.

---

# **7. RUNNING THE FULL SYSTEM**

Start all services:

### **1. MongoDB**
Automatic if installed locally

### **2. Backend**
```
uvicorn app.main:app --reload --port 8000
```

### **3. Frontend**
```
npm start
```

### FULL APP URL:
👉 http://localhost:3000  

You now have full functionality:
- Add categories & items  
- Create shopping lists  
- Upload bills  
- ML suggestions  
- Dashboard analytics  

---

# **8. ENVIRONMENT VARIABLES**

A `.env` file must be placed inside **backend/**.

### Sample `.env`:

```
MONGO_URI=mongodb://localhost:27017/grocerydb
OPENAI_API_KEY=sk-xxxxxx
MODEL_NAME=gpt-4.1-mini
GRIDFS_BUCKET=bill_images
```

---

# **9. LLM INTEGRATION SETUP**

Only one thing needed:

### **OpenAI API Key**
Get from: https://platform.openai.com

Set it in `.env`.

If using proxies or VPN → configure in `llm_client.py`.

---

# **10. PACKAGING FOR LOCAL DISTRIBUTION**

You may want to pack the app for easy installation for yourself or family.

### **Option A: Create a Simple Batch File (Windows)**

Create `start-app.bat`:

```
cd backend
venv\Scripts\activate
uvicorn app.main:app --port 8000
```

Create `start-ui.bat`:

```
cd frontend
npm start
```

### **Option B: Build Frontend into a Static App**

```
npm run build
```

Serve via:
```
npm install -g serve
serve -s build
```

---

# **11. LOGGING & DEBUGGING**

### Backend Logs
Automatically generated in FastAPI console.

### Frontend Logs  
Browser console → Inspect → Console tab

### MongoDB Logs  
Located in MongoDB log directory.

---

# **12. BACKUP & RESTORE**

### **Backup database**
```
mongodump --db grocerydb --out backup/
```

### **Restore**
```
mongorestore backup/
```

### **Backup bill images**
GridFS automatically included in dump.

---

# **13. NEXT STEPS (PHASE 2 & 3 DEPLOYMENT PATH)**

### Phase 2 (Cloud)
- Deploy backend on AWS EC2 / Render / Azure App Service  
- Move MongoDB to Atlas  
- Move bill images to S3  
- Add authentication  

### Phase 3 (Mobile App)
- Build React Native app  
- Add offline sync layer  
- Authenticate via cloud backend  

---

# **End of Part 10**
