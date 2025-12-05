
# Grocery Application – Requirements & Architecture Document  
## **Part 4 – Data Flow Diagrams & Sequence Diagrams**

---

# **Data Flow & Sequence Diagrams**  
This is **Part 4** of the consolidated documentation.  
It contains all **data flow diagrams (DFDs)** and **sequence diagrams** required to understand the runtime behavior of the system.

---

# **Table of Contents (Part 4)**

1. End-to-End Data Flow (Level 0 DFD)  
2. Bill Parsing Flow (Level 1 DFD)  
3. Shopping List Creation Flow (Level 1 DFD)  
4. Sequence Diagram – Shopping List Creation  
5. Sequence Diagram – Bill Parsing with LLM  
6. Sequence Diagram – Dashboard Analytics  
7. Sequence Diagram – ML Suggestion Engine  
8. Sequence Diagram – On-the-Fly Item Add  
9. Error Handling Flow  
10. Data Lifecycle of a Grocery Item  

---

# **1. End-to-End Data Flow (Level 0 DFD)**

This diagram shows the **top-level movement of data** between the User, UI, Backend, Database, and LLM API.

```text
                           ┌───────────────────────────┐
                           │        User (Amit)        │
                           └──────────────┬────────────┘
                                          │
                                          ▼
                           ┌───────────────────────────┐
                           │    React UI (Frontend)     │
                           │   Forms / Tables / Views   │
                           └──────────────┬────────────┘
                                          │ REST API Calls
                                          ▼
                           ┌───────────────────────────┐
                           │      FastAPI Backend       │
                           │  Validation + Processing   │
                           └──────────────┬────────────┘
                                          │ DB Queries
                                          ▼
                           ┌───────────────────────────┐
                           │     MongoDB (Local)        │
                           │  Collections + GridFS      │
                           └──────────────┬────────────┘
                                          │ LLM Requests
                                          ▼
                           ┌───────────────────────────┐
                           │   OpenAI ChatGPT Vision    │
                           │   (Cloud Image-to-JSON)    │
                           └────────────────────────────┘
```

---

# **2. Bill Parsing Flow (Level 1 DFD)**

Details how data moves when a bill image is uploaded and parsed.

```text
User
  │
  ▼
[Upload Bill Image]
  │
  ▼
React UI
  │ Sends multipart/form-data
  ▼
FastAPI (Bill Upload Endpoint)
  │
  ├─► Temporarily store image if needed
  │
  ├─► Call LLM Service (ChatGPT Vision) with image + prompt
  │        │
  │        ▼
  │    ChatGPT Vision (LLM)
  │        │
  │        ▼
  │  JSON: items [{name, qty, unit_price, total_price}]
  │
  ├─► Fuzzy Matching (parsed_name → items collection)
  │
  ├─► Store image in GridFS (bill_images.files / chunks)
  │
  ├─► Store extracted metadata in bills_metadata
  │
  ▼
React UI receives structured data and displays a review table.
```

---

# **3. Shopping List Creation Flow (Level 1 DFD)**

```text
User → React: Click "New Shopping List"
           │
           ▼
React → FastAPI: POST /shopping-lists
           │
           ▼
FastAPI → MongoDB: Insert new list document
           │
           ▼
FastAPI → React: List created (id returned)
           │
           ▼
React → FastAPI: GET /items (load master items)
           │
           ▼
FastAPI → MongoDB: Fetch items
           │
           ▼
React displays item table with quantity fields
           │
           ▼
User enters quantities → React → FastAPI: POST /shopping-lists/{id}/items
           │
           ▼
FastAPI → MongoDB: Insert/Update shopping_list_items
```

---

# **4. Sequence Diagram – Shopping List Creation**

```text
User        UI (React)        FastAPI Backend        MongoDB
 │              │                   │                   │
 │  Open Page   │                   │                   │
 ├────────────► │                   │                   │
 │              │ GET /items        │                   │
 │              ├──────────────────►│                   │
 │              │                   │ Query items       │
 │              │                   ├──────────────────►│
 │              │                   │ Return list       │
 │              │ ◄─────────────────┤                   │
 │              │ Render table      │                   │
 │ Enters qty   │                   │                   │
 ├────────────► │                   │                   │
 │              │ POST /shopping-lists                   │
 │              ├──────────────────►│                   │
 │              │                   │ Insert list       │
 │              │                   ├──────────────────►│
 │              │                   │ Return id         │
 │              │ ◄─────────────────┤                   │
 │              │ POST /shopping-lists/{id}/items       │
 │              ├──────────────────►│                   │
 │              │                   │ Insert list items │
 │              │                   ├──────────────────►│
 │              │                   │ OK                │
 │              │ ◄─────────────────┤                   │
 │ Confirm Msg  │                   │                   │
```

---

# **5. Sequence Diagram – Bill Parsing with LLM**

```text
User           UI (React)         FastAPI            ChatGPT           MongoDB
 │                │                 │                   │                 │
 │ Upload image   │                 │                   │                 │
 ├───────────────►│                 │                   │                 │
 │                │ POST /bills/upload                  │                 │
 │                ├────────────────►│                   │                 │
 │                │                 │ Prepare prompt    │                 │
 │                │                 │ & image payload   │                 │
 │                │                 ├───────────────────►│                 │
 │                │                 │                   │ Vision model    │
 │                │                 │                   │ extracts JSON   │
 │                │                 │                   │◄────────────────┤
 │                │                 │ Receive JSON      │                 │
 │                │                 │ Fuzzy item match  │                 │
 │                │                 │ Save image GridFS │                 │
 │                │                 ├───────────────────►│ (bill_images)   │
 │                │                 │ Save metadata     │                 │
 │                │                 ├───────────────────►│ (bills_metadata)│
 │                │                 │ Return parsed     │                 │
 │                │ ◄────────────────┤ data              │                 │
 │ Show items     │                 │                   │                 │
```

---

# **6. Sequence Diagram – Dashboard Analytics**

```text
User          UI (React)              FastAPI                MongoDB
 │               │                      │                      │
 │ Open Dashboard│                      │                      │
 ├──────────────►│                      │                      │
 │               │ GET /analytics/summary                      │
 │               ├──────────────────────►│                      │
 │               │                      │ Aggregate data for    │
 │               │                      │ last 12 months        │
 │               │                      ├──────────────────────►│
 │               │                      │ Mongo aggregation     │
 │               │                      ◄──────────────────────┤
 │               │ Render charts & cards│                      │
 │               ◄──────────────────────┤                      │
```

---

# **7. Sequence Diagram – ML Suggestion Engine**

```text
UI           FastAPI           ML Service           MongoDB
 │              │                 │                   │
 │ GET /ml/suggestions/next-list │                   │
 ├────────────►│                 │                   │
 │              │ Load history   │                   │
 │              │───────────────►│                   │
 │              │                 │ Query actual_purchases |
 │              │                 │ and shopping_list_items│
 │              │                 ├───────────────────────►│
 │              │                 │ Return historical data │
 │              │                 ◄───────────────────────┤
 │              │                 │ Compute features       │
 │              │                 │ Run EMA / regression   │
 │              │                 │ Build suggestion list  │
 │              │◄───────────────┤                        │
 │ Render cards │                 │                        │
```

---

# **8. Sequence Diagram – Add Item On-the-Fly**

```text
User      UI (React)          FastAPI           MongoDB
 │          │                    │                │
 │ Click    │                    │                │
 │ "Add New Item"                │                │
 ├────────►│                    │                │
 │          │ Show modal        │                │
 │ Fills    │                    │                │
 │ form     │                    │                │
 ├────────►│                    │                │
 │          │ POST /items       │                │
 │          ├──────────────────►│                │
 │          │                    │ Insert item    │
 │          │                    ├──────────────►│
 │          │                    │ OK             │
 │          │◄───────────────────┤                │
 │          │ Update item list   │                │
```

---

# **9. Error Handling Flow**

```text
User Input
   │
   ▼
UI Validation
   ├─ If invalid → Show inline error / toast
   └─ If valid → Send to backend
   ▼
FastAPI
   │ Validates schema with Pydantic
   ├─ If validation error → return JSON error
   │   { "success": false, "error_code": "VALIDATION_ERROR", ... }
   └─ Else → proceed
   ▼
DB / LLM Calls
   ├─ If DB error → return "DB_ERROR"
   ├─ If LLM error → return "LLM_ERROR"
   └─ Else → success
   ▼
UI receives error response and displays friendly message.
```

---

# **10. Data Lifecycle of a Grocery Item**

```text
1. Item Created
   - Inserted into `items` collection.

2. Item Added to Shopping List
   - Entry added to `shopping_list_items` with required quantity.

3. Actual Purchase Recorded
   - Entry added/updated in `actual_purchases` for that list + item.

4. Bill Parsed (Optional)
   - LLM extracts line items and maps them to `items`.
   - `bills_metadata` contains mapping and raw LLM data.

5. Analytics / ML
   - Dashboard aggregates data for charts.
   - ML engine reads historical rows for predictions.

6. Future Lists
   - ML suggests quantity and brand based on patterns.
```

---

# **End of Part 4**

This file completes all DFDs and sequence diagrams needed for your grocery application.

