
# Grocery Application – Requirements & Architecture Document  
## **Part 6 – API Specification (FastAPI)**

---

# **API Specification Document (Part 6)**
This section defines the complete **REST API contract** for the Grocery Shopping Application (Phase 1).  
All endpoints are implemented using **FastAPI**, returning JSON responses.

---

# **Table of Contents (Part 6)**

1. API Design Principles  
2. Standard Response Format  
3. Error Response Format  
4. Categories API  
5. Items API  
6. Shopping Lists API  
7. Shopping List Items API  
8. Actual Purchases API  
9. Bill Upload & LLM Parsing API  
10. Dashboard / Analytics API  
11. ML Suggestions API  
12. Health Check API  

---

# **1. API Design Principles**

- REST-based architecture  
- JSON as default format  
- Pydantic models for schema validation  
- Clear separation of routes under `/api/v1`  
- All IDs use MongoDB ObjectId strings  
- Status codes follow standards:
  - `200 OK`
  - `201 Created`
  - `400 Bad Request`
  - `404 Not Found`
  - `500 Internal Server Error`

---

# **2. Standard Response Format**

```json
{
  "success": true,
  "message": "optional message",
  "data": {}
}
```

---

# **3. Error Response Format**

```json
{
  "success": false,
  "error_code": "VALIDATION_ERROR",
  "error_message": "Name is required",
  "details": {}
}
```

---

# **4. Categories API**

## **4.1 GET /api/v1/categories**
Retrieve all categories.

### Response:
```json
{
  "success": true,
  "data": [
    {
      "_id": "676ac2f12345abcd12345678",
      "category_name": "Pulses",
      "default_measurement_unit": "kg"
    }
  ]
}
```

---

## **4.2 POST /api/v1/categories**
Create a new category.

### Request:
```json
{
  "category_name": "Masala",
  "default_measurement_unit": "g"
}
```

### Response:
```json
{ "success": true, "message": "Category created" }
```

---

## **4.3 PUT /api/v1/categories/{id}**
Update category.

---

## **4.4 DELETE /api/v1/categories/{id}**
Delete category.

---

# **5. Items API**

## **5.1 GET /api/v1/items**
Retrieve all items, with optional filters.

### Query params:
- `category_id`
- `search`

---

## **5.2 POST /api/v1/items**
Create new item.

### Request:
```json
{
  "item_name": "Toor Dal",
  "category_id": "676ac2f12345abcd12345678",
  "measurement_type": "kg",
  "brand": "Tata"
}
```

---

## **5.3 PUT /api/v1/items/{id}**
Update item.

---

## **5.4 DELETE /api/v1/items/{id}**
Delete item.

---

# **6. Shopping Lists API**

## **6.1 GET /api/v1/shopping-lists**
List all shopping lists.

---

## **6.2 POST /api/v1/shopping-lists**
Create a new shopping list.

### Request:
```json
{
  "list_name": "Jan 2025 Shopping"
}
```

---

## **6.3 GET /api/v1/shopping-lists/{id}**
Get full details of a list.

---

## **6.4 DELETE /api/v1/shopping-lists/{id}**
Delete a shopping list.

---

# **7. Shopping List Items API**

## **7.1 POST /api/v1/shopping-lists/{id}/items**
Add or update an item in a list.

### Request:
```json
{
  "item_id": "676ac3159999abcd98765432",
  "required_quantity": 2,
  "measurement_type": "kg"
}
```

---

## **7.2 GET /api/v1/shopping-lists/{id}/items**
Retrieve all items of a shopping list.

---

## **7.3 DELETE /api/v1/shopping-lists/{id}/items/{item_id}**
Remove item from list.

---

# **8. Actual Purchases API**

## **8.1 POST /api/v1/actuals**
Record actual purchase info.

### Request:
```json
{
  "list_id": "676ac36b2828123499887766",
  "item_id": "676ac3159999abcd98765432",
  "actual_quantity": 2,
  "unit_price": 110,
  "total_price": 220
}
```

---

## **8.2 GET /api/v1/actuals/{list_id}**
Retrieve actual purchases for a list.

---

# **9. Bill Upload & LLM Parsing API**

## **9.1 POST /api/v1/bills/upload**
Upload a bill image and parse using ChatGPT Vision.

### Request (multipart/form-data):
```
file: image.jpg
list_id: optional
```

### Response:
```json
{
  "success": true,
  "data": {
    "bill_id": "676ac44a2214aa9988776611",
    "extracted_items": [
      {
        "raw_name": "Tur Dal 1kg",
        "parsed_name": "Toor Dal",
        "quantity": 1,
        "unit": "kg",
        "unit_price": 110,
        "total_price": 110
      }
    ]
  }
}
```

---

## **9.2 GET /api/v1/bills/{bill_id}**
Fetch bill metadata.

---

## **9.3 GET /api/v1/bills/{bill_id}/image**
Stream bill image from GridFS.

---

# **10. Dashboard / Analytics API**

## **10.1 GET /api/v1/analytics/summary**

### Output:
```json
{
  "success": true,
  "data": {
    "total_spend_last_12_months": 12450,
    "category_summary": [
      {"category": "Pulses", "total": 3200},
      {"category": "Dairy", "total": 1800}
    ],
    "monthly_chart": [
      {"month": "Jan", "amount": 2340},
      {"month": "Feb", "amount": 1800}
    ]
  }
}
```

---

# **11. ML Suggestions API**

## **11.1 GET /api/v1/ml/suggestions/next-list**
Get predicted quantities for next shopping list.

### Response:
```json
{
  "success": true,
  "data": [
    {
      "item_id": "676ac3159999abcd98765432",
      "suggested_quantity": 2.5,
      "confidence": 0.78,
      "brand_suggestion": "Tata"
    }
  ]
}
```

---

# **12. Health Check API**

## **12.1 GET /api/v1/health**
Health and readiness probe.

### Response:
```json
{ "status": "ok", "timestamp": "2025-12-03T18:00:00Z" }
```

---

# **End of Part 6**
