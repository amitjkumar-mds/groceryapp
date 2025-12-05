
# Grocery Application – Requirements & Architecture Document  
## **Part 1 – Title Page, Executive Summary & Table of Contents**

---

# **Grocery Shopping Management Application**  
### **Phase 1 – Local Desktop Version**  
**Prepared for:** Amit  
**Prepared by:** ChatGPT (Business Analyst + Architect)  
**Document Type:** Consolidated Requirements & Architecture (Part 1)  
**Version:** 1.0  
**Date:** 2025  

---

# **Executive Summary**

The Grocery Shopping Management Application is designed as a personal-use, AI-assisted grocery planning and tracking system running fully on Amit’s local laptop. The goal of Phase 1 is to eliminate manual effort in maintaining grocery lists, tracking purchases, and extracting data from bills.

This application combines:

- **React + TypeScript** (frontend)
- **FastAPI (Python)** (backend)
- **MongoDB local** (NoSQL database)
- **ChatGPT Vision API** for bill extraction
- **Lightweight ML models** for consumption prediction
- **Local-only execution** (except LLM calls)

The system allows creation of categories, items, shopping lists, quantity planning, entry of actual purchases, automatic bill parsing, and dashboards showing up to 12 months of spending and consumption.

This document is **Part 1** of the full consolidated requirements and architecture documentation.

---

# **Table of Contents (for Part 1)**

1. Title Page  
2. Executive Summary  
3. Business Purpose  
4. Business Objectives  
5. Scope (In-Scope & Out-of-Scope)  
6. Key Assumptions  
7. Stakeholders  
8. Business Risks  
9. High-Level Business Requirements Summary  

---

# **1. Business Purpose**

The Grocery Shopping Management Application aims to offer a streamlined, intelligent approach to household grocery management for a single user (Amit). It removes repetitive manual tasks such as:

- Writing grocery lists every month  
- Tracking quantities required and actual purchases  
- Calculating total costs  
- Comparing historical trends  
- Reading bill images manually  

With AI-powered bill extraction and a structured categorical database, this application significantly reduces errors and improves convenience.

Phase 1 is entirely **local** with **no login**, ensuring privacy and control.

---

# **2. Business Objectives**

## **Primary Objectives**
1. Provide ability to create and manage categories and grocery items.  
2. Build shopping lists with required quantities.  
3. Allow item creation on the fly.  
4. Capture actual purchases (quantity, unit price, total cost).  
5. Use ChatGPT Vision to extract bill details automatically.  
6. Maintain all information in a local MongoDB database.  
7. Provide export options: PDF, Excel, Printable formats.  
8. Display spending trends for the last 12 months.  
9. Suggest quantities and brands using lightweight ML models.

## **Secondary Objectives**
1. Prepare backend & frontend for Phase 2 cloud migration.  
2. Create modular architecture usable for mobile app in Phase 3.

---

# **3. Scope of Work**

## **In Scope (Phase 1)**
- Category management (CRUD)  
- Item management (CRUD)  
- Shopping list creation  
- Required quantity entry  
- Actual purchase entry  
- Bill upload and AI extraction  
- Dashboard (12-month trends)  
- ML suggestions (basic models)  
- PDF/Excel exports  
- Local MongoDB storage  
- React-based browser UI  
- FastAPI backend  

## **Out of Scope**
- Cloud hosting  
- User authentication  
- Multi-user support  
- Mobile application  
- Advanced ML (deep learning)  
- Notifications  

---

# **4. Key Business Assumptions**

1. All data is stored locally on Amit’s laptop.  
2. Internet is required only for AI bill parsing.  
3. Laptop is sufficiently powerful to run React + FastAPI + MongoDB.  
4. User has valid OpenAI API key stored in `.env`.  
5. User will maintain local backups as needed.  
6. System will be extended in future phases without redesign.

---

# **5. Stakeholders**

| Stakeholder | Role | Responsibilities |
|------------|------|------------------|
| Amit | Product Owner | Defines requirements, tests features |
| ChatGPT | BA + Architect | Designs specifications & architecture |
| Developer (future) | Implementer | Builds Phase 1 application |
| MongoDB Local | Data store | Stores all collections and images |

---

# **6. Business Risks**

### **High**
- LLM failures may impact bill parsing.  
- No cloud backup in Phase 1.  

### **Medium**
- Inaccurate bill OCR due to poor image quality.  
- Large bill image storage increasing local DB size.  

### **Low**
- UI performance degradation with very large data.  

---

# **7. High-Level Business Requirements Summary**

| ID | Requirement | Description |
|----|-------------|-------------|
| BR-01 | Category Management | Create/edit/delete categories |
| BR-02 | Item Management | Create/edit/delete items |
| BR-03 | Shopping Lists | Create and manage shopping lists |
| BR-04 | Exporting | Export lists to PDF/Excel |
| BR-05 | Actual Purchases | Enter actual values post-shopping |
| BR-06 | Bill Parsing | AI extraction from bill images |
| BR-07 | Local DB | All data stored in MongoDB local |
| BR-08 | Dashboard | 12-month trends |
| BR-09 | ML Suggestions | Predict quantities for next list |

---

# **End of Part 1**

This file contains the full content of Part 1 without truncation or placeholders.

More parts (Part 2–15) can be generated the same way.

