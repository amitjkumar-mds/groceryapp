
# Grocery Application – Requirements & Architecture Document  
## **Part 8 – ML / AI Design (LLM + Local Machine Learning Models)**

---

# **ML & AI Design Document – Part 8**

This section defines the complete AI behavior for the Grocery Shopping Application.  
Includes LLM-based bill parsing and local ML-based quantity/brand suggestions.

---

# **Table of Contents**

1. AI Objectives  
2. LLM (ChatGPT Vision) Architecture  
3. Prompt Engineering  
4. LLM JSON Schema  
5. Fuzzy Matching Logic  
6. ML Models Overview  
7. Feature Engineering  
8. Training Pipeline  
9. Prediction Pipeline  
10. API Integration  
11. Evaluation Metrics  
12. Model Versioning Strategy  
13. Future Enhancements  

---

# **1. AI Objectives**

### Primary AI Goals:
- Parse grocery bills automatically  
- Convert bill text into structured JSON  
- Suggest next-month quantities  
- Suggest commonly purchased brands  
- Highlight unusual price spikes  

---

# **2. LLM (ChatGPT Vision) Architecture**

```
User → Upload Bill Image  
React → FastAPI (/bills/upload)  
FastAPI → LLM Service  
LLM → Extract structured JSON  
FastAPI → Fuzzy Matching → Store  
React → Display parsed items  
```

LLM is called only during bill uploads.

---

# **3. Prompt Engineering**

A carefully constructed prompt ensures consistent output:

```
You are an expert invoice parser.
Extract all items from this bill and return pure JSON:

{
 "items": [
   {
    "raw_name": "",
    "parsed_name": "",
    "quantity": "",
    "unit": "",
    "unit_price": "",
    "total_price": ""
   }
 ]
}

Rules:
- No explanations
- Pure JSON
- Ensure numeric values are correctly typed
```

---

# **4. LLM JSON Schema**

Sample output:

```json
{
  "items": [
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
```

Notes:
- `raw_name` preserves OCR text
- `parsed_name` is cleaned name
- Units normalized to standard (kg, g, ml, L, unit)

---

# **5. Fuzzy Matching Logic**

FastAPI maps LLM-extracted items to DB items.

### Steps:
1. Normalize both strings:
   - lowercase  
   - remove units (“1kg”)  
   - remove symbols (“–”, “#”)  
2. Compare using *rapidfuzz*:
```python
score = fuzz.partial_ratio(extracted, master_item)
```
3. If score ≥ **85%** → auto-match  
4. Else → user manually maps via UI  

---

# **6. ML Models Overview**

The system uses **hybrid lightweight ML**, not heavy deep learning.

### Models included:
- **EMA (Exponential Moving Average)**  
- **Linear Regression (sklearn)**  
- **Purchase Frequency Estimator**  
- **Brand Preference Selector**  

### ML purpose:
- Suggest next-month quantity  
- Suggest preferred brand  
- Detect deviations in price  

---

# **7. Feature Engineering**

### Features extracted from history:

| Feature | Description |
|---------|-------------|
| `last_6_quantities` | Rolling quantities for each month |
| `avg_purchase_gap` | Time between purchases |
| `seasonal_variation` | Higher sugar in Diwali, etc. |
| `brand_frequency` | How often a brand was purchased |
| `price_trend` | Rising or falling cost |

Example feature vector:

```
[ 2.0, 2.0, 3.0, 1.5, 2.5, 3.0, 6 (gap), 1 (brand: Tata) ]
```

---

# **8. Training Pipeline**

ML is retrained on every suggestion call.

### Steps:
```
Load actual_purchases from MongoDB
→ Group by item
→ Build historical feature vector
→ Run EMA
→ Run Regression
→ Combine scores with hybrid weighting
→ Output suggestions
```

No offline training needed for Phase 1.

---

# **9. Prediction Pipeline**

```
User clicks “Get Suggestions”
→ React → FastAPI GET /ml/suggestions/next-list
→ Backend loads all history
→ Generate features
→ Run models
→ Return predictions
→ UI displays cards (suggested quantity + brand)
```

### Output Example:
```json
{
  "item": "Toor Dal",
  "suggested_quantity": 2.5,
  "confidence": 0.78,
  "brand_suggestion": "Tata"
}
```

---

# **10. API Integration**

### API used:
```
GET /api/v1/ml/suggestions/next-list
```

### Response:
- Suggested quantity  
- Brand suggestion  
- Confidence score  

Backend merges EMA + regression predictions into a single result.

---

# **11. Evaluation Metrics**

| Metric | Purpose |
|--------|----------|
| RMSE | Regression error |
| MAPE | Month-to-month accuracy |
| Confidence Score | Tells user reliability |
| Variance Score | Measures stability |

---

# **12. Model Versioning Strategy**

### Phase 1:
- No versioning (models are ephemeral)

### Phase 2:
Store in MongoDB:
```json
{
  "model_name": "quantity_predictor",
  "version": "v1.0",
  "created_at": "2026-01-01",
  "parameters": {},
  "metrics": {}
}
```

### Phase 3:
- Deploy models via cloud ML hosting (AWS Sagemaker / GCP Vertex AI)

---

# **13. Future AI Enhancements**

### Phase 2:
- Deep-learning invoice parser  
- Price anomaly detection  
- Collaborative filtering (recommendation engine)  

### Phase 3:
- Barcode scanning for direct item detection  
- Voice input for shopping list creation  
- AI-chat interface (“Plan my monthly groceries”)  
- Real-time pricing updates from digital catalogs  

---

# **End of Part 8**
