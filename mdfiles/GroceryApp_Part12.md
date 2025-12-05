
# Grocery Application – Requirements & Architecture Document  
## **Part 12 – Comprehensive Test Plan (Unit, Integration, E2E, LLM Validation)**

---

# **PART 12 – TEST PLAN**

This document provides the **complete testing strategy** for the Grocery Shopping Application (Phase 1 Local Desktop App).  
It includes:

- Unit Test Plan  
- Integration Tests  
- End-to-End (E2E) Tests  
- LLM Validation Tests  
- ML Model Validation Tests  
- Performance & Load Tests  
- Security Tests  
- UAT Scenarios  

---

# **Table of Contents (Part 12)**

1. Testing Objectives  
2. Testing Scope  
3. Test Types & Levels  
4. Unit Test Plan  
5. Integration Test Plan  
6. End-to-End (E2E) Tests  
7. LLM Parsing Validation Tests  
8. ML Suggestion Engine Tests  
9. Performance & Load Tests  
10. Security Tests  
11. Regression Test Suite  
12. UAT Scenarios  
13. Exit Criteria  
14. Test Data Strategy  
15. Tools for Testing  

---

# **1. TESTING OBJECTIVES**

The test plan aims to ensure:

- All functionalities behave as expected  
- Data integrity is maintained  
- ML/LLM output is validated systematically  
- UI flows are seamless and bug-free  
- Backend service and database work correctly  
- Application is ready for Phase 2 migration  

---

# **2. TESTING SCOPE**

### **IN SCOPE**
- UI testing (React)  
- API testing (FastAPI)  
- MongoDB CRUD validation  
- LLM image parsing validation  
- ML model output testing  
- Export (PDF/Excel) validation  
- Dashboard correctness  
- Error handling  

### **OUT OF SCOPE (Phase 1)**
- Multi-user authentication  
- Cloud load testing  
- Mobile app testing  

---

# **3. TEST TYPES & LEVELS**

| Test Type | Description |
|-----------|-------------|
| Unit Tests | Component-level testing |
| Integration Tests | Backend + DB, UI + API |
| E2E Tests | Full workflow testing |
| LLM Extraction Tests | Validate JSON correctness |
| ML Output Tests | Validate predictions |
| Performance Tests | Response time, processing time |
| Security Tests | Validation, sanitization, API key protection |

---

# **4. UNIT TEST PLAN**

### **4.1 Backend (FastAPI) Unit Tests**

**Modules to test:**
- Category service  
- Item service  
- Shopping list service  
- Bill upload service  
- Fuzzy matching engine  
- ML utilities  

**Examples:**

1. `test_create_category()`  
2. `test_invalid_category_name()`  
3. `test_create_item_with_missing_fields()`  
4. `test_ml_ema_calculation()`  
5. `test_fuzzy_match_high_score()`  

**Expected Tools:**  
- `pytest`  
- `pytest-asyncio`  

---

### **4.2 Frontend (React) Unit Tests**

**Modules to test:**
- Category form  
- Item form  
- Shopping list item table  
- Bill upload component  
- Dashboard components  

**Test cases:**
- Component renders correctly  
- Form validation  
- API errors handled gracefully  
- State updates correctly  

**Expected Tools:**  
- Jest  
- React Testing Library  

---

# **5. INTEGRATION TEST PLAN**

Integration tests validate **interactions between components**.

### **5.1 Backend + Database Tests**
- Create category → stored correctly  
- Create item → category reference valid  
- Add item to shopping list → linked in DB  
- Upload bill → GridFS storage validated  
- LLM parsed data → inserted in `bills_metadata`  

### **5.2 Frontend → API Integration Tests**
- UI sends correct payloads  
- API errors surface correctly  
- Table renders updated data after operations  

### **5.3 LLM Flow Integration**
Input → Bill upload → LLM → Parsed data → DB  

Validate:
- JSON is clean  
- Quantity parsed correctly  
- No hallucinated fields  

---

# **6. END-TO-END (E2E) TESTS**

Tools:
- Cypress  
- Playwright  

### **Major E2E Scenarios**

1. **Create Category → Add Items → Create Shopping List**  
2. **Add Required Quantities → Save → Reopen List**  
3. **Upload Bill → LLM Extracts → Map Items → Save Actual Purchases**  
4. **Export PDF & Excel**  
5. **Dashboard shows correct 12-month analytics**  
6. **ML suggestions show correct quantities & brand**  

Each scenario validates:
- UI workflow  
- API orchestration  
- Database writing  
- Data consistency  

---

# **7. LLM PARSING VALIDATION TESTS**

LLM responses must be validated to avoid incorrect entries.

### **Test Method**
For each uploaded bill:

1. Verify **JSON schema**  
2. Validate **numeric extraction**  
3. Validate **unit normalization**  
4. Ensure no extraneous fields  
5. Ensure no hallucinated items  
6. Log malformed responses  

### **Test Cases**
| Case | Example |
|------|---------|
| Single item | “Sugar 1kg – ₹45” |
| Multi-item bill | 10+ items |
| Smudged text | low clarity image |
| Wrong unit detection | “2 packets” vs “2 units” |
| Price extraction errors | total missing or incorrect |

---

# **8. ML SUGGESTION ENGINE TESTS**

### **Test Inputs**
- Multi-month history  
- Gaps in purchase history  
- Highly seasonal items  
- Items with brand variability  
- Items with no purchase history  

### **Test Output Validations**
- EMA prediction correctness  
- Regression prediction correctness  
- Confidence score range (0–1)  
- Brand suggestion logic  

### **Edge Cases**
- Zero purchase history  
- Outlier purchase spikes  
- Incorrect DB entries  

---

# **9. PERFORMANCE & LOAD TESTING**

### **LLM Performance**
- Time to process bill image  
- Retry logic validation  

### **API Performance**
- Response time < 300ms for CRUD  
- Bill upload time < 3 seconds  

### **DB Performance**
- Index validation  
- Query speed for dashboard  

Tools:
- Locust  
- JMeter (optional)  

---

# **10. SECURITY TESTS**

### Backend:
- Payload validation  
- Schema enforcement  
- Injection tests  

### Frontend:
- XSS injection tests  
- Input field sanitization  

### API Key Validation:
- Ensure OpenAI API key is never logged  
- Prevent CORS misconfigurations  

### File Upload Security:
- Allow only images  
- Reject >10MB files  

---

# **11. REGRESSION TEST SUITE**

Triggered:
- Before major releases  
- After feature additions  
- After DB schema changes  

### Includes:
- All unit tests  
- Critical E2E flows  
- ML & LLM validation suite  

Regression ensures **nothing breaks during enhancement cycles**.

---

# **12. USER ACCEPTANCE TESTING (UAT) SCENARIOS**

### **UAT-01: Create My First Shopping List**
User can:
- Add category  
- Add items  
- Create list  
- Add required quantities  

### **UAT-02: Upload Bill & Auto-Extract Items**
- LLM extraction works reliably  
- Mapped data is correct  

### **UAT-03: Compare Required vs Actual Purchases**
- Correct price/quantity comparison  

### **UAT-04: Dashboard Displays Correct Analytics**

### **UAT-05: ML Recommendations Work Properly**
- Suggestions align with history  

Each scenario includes:
- Preconditions  
- Test steps  
- Expected output  
- Pass/Fail criteria  

---

# **13. EXIT CRITERIA**

Testing is considered complete when:

- All critical bugs are resolved  
- Code coverage ≥ 80% for backend  
- E2E flows pass successfully  
- LLM & ML validations produce stable results  
- DB integrity verified  
- No performance blocker exists  

---

# **14. TEST DATA STRATEGY**

Create controlled datasets:

### **Dataset 1 – Small**
- 5 categories  
- 20 items  
- 3 shopping lists  

### **Dataset 2 – Medium**
- 10 categories  
- 80 items  
- 12 shopping lists  
- 6 months purchase history  

### **Dataset 3 – Edge Cases**
- Missing prices  
- Uncommon units  
- Blurry bills  

---

# **15. TOOLS FOR TESTING**

| Category | Tools |
|----------|--------|
| Unit Testing | pytest, Jest |
| E2E | Cypress, Playwright |
| API Testing | Postman, Pytest |
| Load Testing | Locust |
| Security Testing | OWASP ZAP (later) |
| LLM Validation | Schema validators |

---

# **End of Part 12**
