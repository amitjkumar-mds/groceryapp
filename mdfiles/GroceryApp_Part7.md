
# Grocery Application – Requirements & Architecture Document  
## **Part 7 – UI Wireframes (React Screens in Markdown)**

---

# **UI Wireframes – Part 7**  
This section contains complete text-based UI wireframes for all pages of the Grocery Shopping Application.  
These wireframes are meant for **React + TypeScript** implementation and represent the functional layout of the application.

---

# **Table of Contents (Part 7)**

1. UI Principles  
2. Navigation Layout  
3. Categories Page  
4. Items Page  
5. Shopping List Page  
6. Actual Purchases Page  
7. Bill Upload Page  
8. Dashboard Page  
9. Global Components  
10. Modals & Dialogs  

---

# **1. UI Principles**

- Clean, light-mode UI  
- Mobile-responsive, though local-only in Phase 1  
- Simple, form-driven interactions  
- Common Material UI components:
  - Tables  
  - Dialogs  
  - Textfields  
  - Dropdowns  
  - Buttons  
- Consistent spacing & alignment  
- All pages accessible via left sidebar  

---

# **2. Navigation Layout (Wireframe)**

```
+--------------------------------------------------------+
| Grocery Manager                                        |
+--------------------------------------------------------+
| Sidebar                       | Main Content           |
|------------------------------ |------------------------|
| > Dashboard                   | (Page renders here)    |
| > Categories                  |                        |
| > Items                       |                        |
| > Shopping Lists              |                        |
| > Actual Purchases            |                        |
| > Bills                       |                        |
| > ML Suggestions              |                        |
|------------------------------ |                        |
```

---

# **3. Categories Page Wireframe**

### **URL:** `/categories`

```
+------------------------------------------------------------+
| Categories                                                 |
+------------------------------------------------------------+
| [Add Category] button                                      |
+------------------------------------------------------------+
| Table:                                                     |
|------------------------------------------------------------|
|  Category Name | Default Unit | Icon | Actions             |
|------------------------------------------------------------|
|  Pulses        | kg            | ●    | Edit | Delete      |
|  Masala        | g             | ●    | Edit | Delete      |
|  Cleaning      | unit          | ●    | Edit | Delete      |
|------------------------------------------------------------|
```

### **Add Category Modal**

```
+-----------------------------+
| Add Category                |
+-----------------------------+
| Category Name: [text]       |
| Default Unit:  [dropdown]   |
| Icon:          [dropdown]   |
+-----------------------------+
| [Cancel] [Save]             |
+-----------------------------+
```

---

# **4. Items Page Wireframe**

### **URL:** `/items`

```
+----------------------------------------------------------------+
| Items                                                          |
+----------------------------------------------------------------+
| Filters: [Category Dropdown] [Search Box]                      |
| [Add Item]                                                     |
+----------------------------------------------------------------+
| Table:                                                         |
|----------------------------------------------------------------|
| Item Name | Category | Measurement | Brand | Actions           |
|----------------------------------------------------------------|
| Toor Dal  | Pulses   | kg          | Tata  | Edit | Delete     |
| Aata      | Grains   | kg          | Aashirvad | Edit | Delete |
| Surf Excel| Laundry  | unit        | Surf  | Edit | Delete     |
|----------------------------------------------------------------|
```

### Add Item Modal

```
+--------------------------+
| Add Item                 |
+--------------------------+
| Item Name: [text]        |
| Category:  [dropdown]    |
| Measurement Type: [dropdown] |
| Brand: [text]            |
| Notes: [text area]       |
+--------------------------+
| [Cancel] [Save]          |
+--------------------------+
```

---

# **5. Shopping List Page Wireframe**

### **URL:** `/shopping-lists`

```
+------------------------------------------------------------+
| Shopping Lists                                              |
+------------------------------------------------------------+
| [New Shopping List]                                         |
+------------------------------------------------------------+
| Table:                                                      |
|------------------------------------------------------------|
| List Name             | Created On        | Actions         |
|------------------------------------------------------------|
| Jan 2025 Shopping     | 30-Dec-2024 7PM   | Open | Delete   |
| Feb 2025 Shopping     | 01-Feb-2025 10AM  | Open | Delete   |
|------------------------------------------------------------|
```

---

## **5.1 Shopping List Details Wireframe**

### **URL:** `/shopping-lists/{id}`

```
+---------------------------------------------------------------+
| Shopping List: Jan 2025 Shopping                             |
+---------------------------------------------------------------+
| [Add Item] (On-the-fly)                                       |
| Filters: [Category Dropdown] [Search Item]                    |
+---------------------------------------------------------------+
| Items Table                                                   |
|---------------------------------------------------------------|
| Item Name | Category | Required Qty | Unit | Actions          |
|---------------------------------------------------------------|
| Toor Dal  | Pulses   | [2.00]       | kg   | Delete           |
| Sugar     | Grocery  | [1.00]       | kg   | Delete           |
| Maggi     | Snacks   | [6]          | unit | Delete           |
|---------------------------------------------------------------|
```

### Actions:
- Edit quantities inline  
- Add new item  
- Delete item  
- Export PDF  
- Export Excel  
- Print list  

---

# **6. Actual Purchases Page Wireframe**

### **URL:** `/actuals/{list_id}`

```
+------------------------------------------------------------+
| Actual Purchases – Jan 2025 Shopping                       |
+------------------------------------------------------------+
| Table                                                      |
|------------------------------------------------------------|
| Item Name | Required | Actual | Unit Price | Total | Link  |
|------------------------------------------------------------|
| Toor Dal  | 2 kg     | [2]    | [110]      | 220   | Bill |
| Sugar     | 1 kg     | [1]    | [45]       | 45    | Bill |
| Maggi     | 6 units  | [5]    | [14]       | 70    | Bill |
|------------------------------------------------------------|
```

### Notes:
- Total auto-calculated  
- Option to link each item with a parsed bill row  

---

# **7. Bill Upload Page Wireframe**

### **URL:** `/bills`

```
+------------------------------------------------------------+
| Bills                                                      |
+------------------------------------------------------------+
| [Upload Bill Image]                                        |
+------------------------------------------------------------+
| Table                                                      |
|------------------------------------------------------------|
| Bill ID | Uploaded On | Linked List | Actions              |
|------------------------------------------------------------|
| 676ac44a | 30-Dec-2024| Jan 2025    | View | Delete        |
|------------------------------------------------------------|
```

---

## **7.1 Bill Upload Modal**

```
+---------------------------+
| Upload Bill Image         |
+---------------------------+
| Select File: [Choose...]  |
| Link to List: [dropdown]  |
+---------------------------+
| [Cancel] [Upload]         |
+---------------------------+
```

---

## **7.2 Bill Details Screen**

```
+------------------------------------------------------------------+
| Bill Details – #676ac44a                                         |
+------------------------------------------------------------------+
| Parsed Items (from ChatGPT Vision)                               |
+------------------------------------------------------------------+
| Raw Name  | Parsed Name | Qty | Unit | Unit Price | Total | Map |
|------------------------------------------------------------------|
| Tur Dal 1kg | Toor Dal  | 1   | kg   | 110        | 110   | ✔   |
| Aata 5kg    | Aata      | 5   | kg   | 240        | 240   | ✔   |
| Maggi Pack  | Maggi     | 6   | unit | 14         | 84    | ✔   |
|------------------------------------------------------------------|
```

Mapping may involve:
- Auto-matched items  
- Buttons to manually map  
- Button: "Create New Item"  

---

# **8. Dashboard Page Wireframe**

### **URL:** `/dashboard`

```
+------------------------------------------------------------+
| Dashboard                                                  |
+------------------------------------------------------------+
| Cards:                                                     |
|------------------------------------------------------------|
| Total Spend (12 months): ₹12,450                           |
| Total Lists: 10                                            |
| Avg Spend per Trip: ₹1,245                                 |
|------------------------------------------------------------|

Charts:
--------------------------------------------------------------
| Line Chart – Monthly Spend (Last 12 Months)                |
--------------------------------------------------------------
| Bar Chart – Category-wise Spend                            |
--------------------------------------------------------------
| Table – Top 10 Purchased Items                             |
--------------------------------------------------------------
```

---

# **9. Global Components**

### **9.1 Navigation Sidebar**
- Dashboard  
- Categories  
- Items  
- Shopping Lists  
- Actual Purchases  
- Bills  
- ML Suggestions  

### **9.2 Buttons**
- Primary: Blue  
- Secondary: Grey  
- Danger: Red  

---

# **10. Modals & Dialogs**

### Common Modal Layout

```
+-----------------------------------------------+
| Title                                         |
+-----------------------------------------------+
| Form Fields / Information                     |
+-----------------------------------------------+
| [Cancel]                        [Save]        |
+-----------------------------------------------+
```

Used for:
- Add Category  
- Add Item  
- Add to Shopping List  
- Upload Bill  
- Edit Item  
- Delete Confirmation  

---

# **End of Part 7**
