
# Grocery Application – Requirements & Architecture Document  
## **Part 2 – Functional Requirements Document (FRD)**

---

# **Functional Requirements Document (FRD)**  
This is **Part 2** of the full consolidated documentation.  
It contains the **complete, detailed Functional Requirements** for the Grocery Shopping Management Application (Phase 1 – Local Desktop).

---

# **Table of Contents (Part 2)**

1. Introduction  
2. User Roles  
3. Use Case List  
4. Detailed Use Cases  
   - Category Management  
   - Item Management  
   - Shopping List Lifecycle  
   - Actual Purchases  
   - Bill Parsing (LLM-Vision)  
   - Dashboard  
   - ML Suggestions  
5. Functional Requirements (FR-IDs)  
6. Business Rules  
7. Validation Rules  

---

# **1. Introduction**

This FRD translates the business requirements into **detailed functional behaviors** that developers must implement.  
All functionality in Phase 1 is local-only and will run without login.

---

# **2. User Roles**

| Role | Description | Permissions |
|------|-------------|-------------|
| **Primary User (Amit)** | Single end-user of the application | Full access to all modules |

There are **no other roles** in Phase 1.  
Phase 2 will introduce guest users, authenticated users, and admins.

---

# **3. Use Case List**

| UC ID | Use Case Name |
|--------|----------------|
| UC-01 | Manage Categories |
| UC-02 | Manage Items |
| UC-03 | Create Shopping List |
| UC-04 | Add Items to Shopping List |
| UC-05 | Update Required Quantities |
| UC-06 | Export Shopping List |
| UC-07 | Enter Actual Purchases |
| UC-08 | Upload Bill Image |
| UC-09 | Parse Bill Using LLM |
| UC-10 | Map Extracted Items to DB Items |
| UC-11 | Save Bill Metadata |
| UC-12 | View Dashboard |
| UC-13 | ML-Based Suggestions |

---

# **4. Detailed Use Cases**

---

## **UC-01: Manage Categories**

### **Description**
Allows user to create, view, update, and delete grocery categories.

### **Triggers**
User clicks **Categories** in navigation.

### **Preconditions**
None.

### **Steps**
1. User navigates to Categories Page.  
2. System displays a table of categories.  
3. User clicks “Add Category”.  
4. User fills fields:  
   - Category Name  
   - Default measurement unit  
   - Icon (optional)  
5. User clicks Save.  
6. Category appears in the table.  
7. User may edit or delete any category.

### **Postconditions**
- Category added to DB.  
- All items linked to this category can reference it.  

---

## **UC-02: Manage Items**

### **Description**
User can create, edit, delete, and search items.

### **Steps**
1. User opens Items Page.  
2. System shows a filterable list.  
3. User clicks Add Item.  
4. User fills fields:  
   - Item name  
   - Category  
   - Measurement type  
   - Brand (optional)  
   - Notes (optional)  
5. User saves item.  

**On-the-Fly Item Creation:**
- While making shopping list, user can click **“Add New Item”** from modal.

---

## **UC-03: Create Shopping List**

### **Description**
Allows user to create a named grocery list.

### **Steps**
1. User clicks **New Shopping List**.  
2. User enters list name.  
3. User clicks Save.  
4. Blank list is created.  

---

## **UC-04: Add Items to Shopping List**

### **Steps**
1. System loads item master.  
2. User searches or filters items.  
3. User enters required quantities for each item.  
4. User can add items on the fly.  
5. System persists all entries.  

---

## **UC-05: Update Required Quantities**

### **Description**
Modify any item’s planned quantity.

### **Rules**
- Quantity must be numeric.  
- Zero or negative values are not allowed.  

---

## **UC-06: Export Shopping List**

User can export PDF, Excel, or print directly.

---

## **UC-07: Enter Actual Purchases**

### **Steps**
1. User opens Actual Purchases for a list.  
2. System shows planned vs actual side-by-side.  
3. User enters:  
   - Actual quantity  
   - Unit price  
   - Total price (auto-calculated)  
4. User saves data.  

### **Rules**
- Total = Unit price × Actual quantity  
- Actual quantity cannot be negative  

---

## **UC-08: Upload Bill Image**

User selects an image file from local disk.

---

## **UC-09: Parse Bill Using LLM**

### **Steps**
1. Backend receives image.  
2. FastAPI sends image to ChatGPT Vision.  
3. ChatGPT parses text → returns JSON.  
4. Backend returns extracted data to UI.

---

## **UC-10: Map Extracted Items to Item Master**

Backend performs fuzzy matching:
- Exact match → auto-link  
- Close match → user confirmation  
- No match → user adds new item  

---

## **UC-11: Save Bill Metadata**

System stores:
- Full JSON returned by LLM  
- Image in GridFS  
- Extracted items  
- Mapping results  

---

## **UC-12: View Dashboard**

### Includes:
- Last 12 months spend  
- Category-wise spend  
- Item-wise trends  
- Total number of trips  

---

## **UC-13: ML-Based Suggestions**

### Process
1. Backend loads historical quantities.  
2. Applies EMA + frequency model + regression.  
3. Predicts suggested quantity for each item.  
4. Returns confidence score.

---

# **5. Functional Requirements (FR-IDs)**

| FR ID | Requirement |
|--------|-------------|
| FR-01 | System shall allow user to create categories. |
| FR-02 | System shall allow user to edit and delete categories. |
| FR-03 | System shall allow user to create items with measurement type. |
| FR-04 | System shall allow filtering items by category. |
| FR-05 | System shall allow adding items on the fly from Shopping List. |
| FR-06 | System shall allow creation of named shopping lists. |
| FR-07 | System shall store required quantities per item. |
| FR-08 | System shall allow exporting list to PDF, Excel, and Print. |
| FR-09 | System shall allow entering actual quantities and prices. |
| FR-10 | System shall parse bill images using ChatGPT Vision. |
| FR-11 | System shall perform fuzzy matching between extracted items and database items. |
| FR-12 | System shall store bill images in MongoDB GridFS. |
| FR-13 | System shall store extracted JSON metadata in DB. |
| FR-14 | System shall display last 12-month trends in Dashboard. |
| FR-15 | System shall provide ML-based suggested quantities. |

---

# **6. Business Rules**

| Rule ID | Rule |
|---------|------|
| BR-01 | Category names must be unique. |
| BR-02 | Item names must be unique within a category. |
| BR-03 | Required quantities must be > 0. |
| BR-04 | Actual quantities must be ≥ 0. |
| BR-05 | Bill image must be jpg/png/pdf. |
| BR-06 | Fuzzy match threshold ≥ 0.85 for auto-link. |

---

# **7. Validation Rules**

- Required fields: category name, item name, measurement type  
- Quantity fields: float or integer  
- Prices: numeric, ≥ 0  
- File size limit for bill images: 10 MB  
- Only allowed formats: JPG, PNG, JPEG  

---

# **End of Part 2**

