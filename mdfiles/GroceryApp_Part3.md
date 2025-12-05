
# Grocery Application – Requirements & Architecture  
## **Part 3 – System Architecture (High-Level + Low-Level)**

---

# **System Architecture Document (Part 3)**  
This is **Part 3** of the full consolidated document.  
It includes all architectural elements required for development, scaling, and future phases.

---

# **Table of Contents**
1. Architecture Overview  
2. High-Level Architecture  
3. Logical Architecture  
4. Component Architecture  
5. Deployment Architecture  
6. LLM Integration Architecture  
7. ML Architecture  
8. Scalability Plan  

---

# **1. Architecture Overview**

The system is built as a modular 3-tier architecture:

- **Frontend:** React + TypeScript (Browser-based)
- **Backend:** FastAPI (Python)
- **Database:** MongoDB Local (NoSQL + GridFS)
- **AI:** ChatGPT Vision API
- **ML:** Local lightweight predictive engine

The architecture supports **Phase 1 local execution**, with a clean upgrade path to **cloud (Phase 2)** and **mobile (Phase 3)**.

---

# **2. High-Level Architecture**

```
             ┌──────────────────────────┐
             │     React Frontend       │
             │ Browser-based UI         │
             └──────────────┬───────────┘
                            │ REST API Calls
                            ▼
             ┌──────────────────────────┐
             │     FastAPI Backend      │
             │ Business Logic + LLM/ML  │
             └──────────────┬───────────┘
                            │ DB Operations
                            ▼
             ┌──────────────────────────┐
             │      MongoDB Local       │
             │NoSQL + GridFS (Images)   │
             └──────────────┬───────────┘
                            │ LLM Requests
                            ▼
             ┌──────────────────────────┐
             │  ChatGPT Vision (Cloud)  │
             │ Bill Parsing + Extraction│
             └──────────────────────────┘
```

---

# **3. Logical Architecture**

```
┌───────────────────────────┐
│       Presentation Layer   │  → React UI (Components, Pages)
└───────────────┬───────────┘
                ▼
┌───────────────────────────┐
│     API Routing Layer      │ → FastAPI Routers
└───────────────┬───────────┘
                ▼
┌───────────────────────────┐
│   Business Logic Layer     │ → Services (LLM, ML, Mapping)
└───────────────┬───────────┘
                ▼
┌───────────────────────────┐
│   Data Access Layer (DAL)  │ → MongoDB CRUD + GridFS
└───────────────────────────┘
```

---

# **4. Component Architecture**

## **4.1 Frontend Components (React + TypeScript)**

```
src/
 ├── components/
 │     ├── CategoryForm.tsx
 │     ├── CategoryTable.tsx
 │     ├── ItemForm.tsx
 │     ├── ItemTable.tsx
 │     ├── ShoppingListBuilder.tsx
 │     ├── ActualPurchaseTable.tsx
 │     ├── BillUpload.tsx
 │     ├── DashboardCharts.tsx
 │     └── Navbar.tsx
 │
 ├── pages/
 │     ├── CategoriesPage.tsx
 │     ├── ItemsPage.tsx
 │     ├── ShoppingListPage.tsx
 │     ├── ActualsPage.tsx
 │     ├── BillsPage.tsx
 │     └── DashboardPage.tsx
 │
 ├── services/
 │     ├── api.ts
 │     ├── listService.ts
 │     └── billService.ts
 │
 └── utils/
        ├── validators.ts
        └── formatters.ts
```

---

## **4.2 Backend Components (FastAPI)**

```
app/
 ├── main.py
 ├── routers/
 │     ├── categories.py
 │     ├── items.py
 │     ├── shopping_lists.py
 │     ├── actuals.py
 │     ├── bills.py
 │
 ├── services/
 │     ├── llm_service.py
 │     ├── ml_service.py
 │     ├── mapping_service.py
 │
 ├── database/
 │     ├── mongo.py
 │
 ├── models/
 │     ├── category.py
 │     ├── item.py
 │     ├── shopping_list.py
 │     ├── actual_purchase.py
 │     └── bill.py
 │
 └── utils/
        ├── file_utils.py
        └── response_builder.py
```

---

# **5. Deployment Architecture**

### **Phase 1 (Local Laptop)**

```
Frontend  → http://localhost:3000
Backend   → http://localhost:8000
Database  → mongodb://localhost:27017
AI API    → OpenAI (Cloud)
```

Local execution with minimal infrastructure. Ideal for single-user offline-first usage.

---

# **6. LLM Integration Architecture**

### **Purpose:**  
To extract structured item data from grocery bill images.

### **Flow**

```
User Upload
   ▼
FastAPI → /bills/upload
   ▼
LLM Service (Image + Prompt)
   ▼
ChatGPT Vision API
   ▼
Structured JSON Extracted
   ▼
Fuzzy Matching with Item Master
   ▼
MongoDB Save (Metadata + GridFS Image)
   ▼
UI displays parsed items
```

### **Prompt Strategy**
- Extract item name  
- Extract quantity  
- Extract unit price  
- Extract total price  
- Return pure JSON  

---

# **7. ML Architecture**

### **Models Used**
- **Exponential Moving Average (EMA)**  
- **Purchase Frequency Model**  
- **Linear Regression (sklearn)**  

### **Prediction Output**
- Suggested quantity  
- Suggested brand  
- Confidence score  

### **ML Processing Pipeline**
```
Load History
   ▼
Feature Engineering
   ▼
Model Execution (EMA + Regression)
   ▼
Prediction Assembly
   ▼
Return suggestions to UI
```

---

# **8. Scalability for Phase 2 & Phase 3**

### **Phase 2 – Cloud**
- Deploy FastAPI to AWS/GCP/Azure  
- Use MongoDB Atlas  
- Add JWT authentication  
- Add multi-user support  
- Add logs + monitoring  

### **Phase 3 – Mobile App**
- Build mobile app with React Native  
- Offline sync with local SQLite  
- Real-time cloud sync  
- Use same backend APIs  

---

# **End of Part 3**
