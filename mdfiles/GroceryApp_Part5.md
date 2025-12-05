
# Grocery Application – Requirements & Architecture Document  
## **Part 5 – Database Schema & Data Dictionary (MongoDB + GridFS)**

---

# **Database Schema & Data Dictionary**  
This is **Part 5** of the consolidated documentation.  
It defines the complete **MongoDB data model** for the Grocery Shopping Management Application.

---

# **Table of Contents (Part 5)**

1. Overview of Collections  
2. Collection: `categories`  
3. Collection: `items`  
4. Collection: `shopping_lists`  
5. Collection: `shopping_list_items`  
6. Collection: `actual_purchases`  
7. Collection: `bills_metadata`  
8. GridFS Collections: `bill_images.files` & `bill_images.chunks`  
9. Optional Collections: `analytics_cache`, `ml_training_data`  
10. Indexing Strategy  
11. Relationships Overview  
12. Sample Documents  
13. Data Retention Considerations  

---

# **1. Overview of Collections**

The application uses the following MongoDB collections:

| Collection Name       | Purpose |
|-----------------------|---------|
| `categories`          | Stores grocery categories (Pulses, Masala, etc.) |
| `items`               | Stores individual grocery items |
| `shopping_lists`      | Stores metadata for each shopping list |
| `shopping_list_items` | Stores required quantities for a given list and item |
| `actual_purchases`    | Stores actual quantities and prices recorded post-shopping |
| `bills_metadata`      | Stores extracted AI data & metadata for each bill |
| `bill_images.files`   | GridFS files collection for bill images |
| `bill_images.chunks`  | GridFS chunks collection for bill images |
| `analytics_cache`*    | Optional cache for heavy analytics queries |
| `ml_training_data`*   | Optional storage for ML model artifacts |

\* Optional in Phase 1.

---

# **2. Collection: `categories`**

## **2.1 Purpose**
Store category master (e.g., Pulses, Masala, Cleaning, Dairy).

## **2.2 Document Structure**

```json
{
  "_id": "ObjectId",
  "category_name": "string",
  "icon": "string|null",
  "default_measurement_unit": "string|null",
  "created_at": "ISODate",
  "updated_at": "ISODate"
}
```

## **2.3 Field Definitions**

| Field                     | Type      | Description |
|---------------------------|-----------|-------------|
| `_id`                     | ObjectId  | Unique identifier for the category |
| `category_name`           | string    | Name of the category (e.g., "Pulses") |
| `icon`                    | string    | Optional icon identifier (UI representation) |
| `default_measurement_unit`| string    | Default unit for items (e.g., "kg", "g", "L", "ml", "unit") |
| `created_at`              | datetime  | Timestamp when category was created |
| `updated_at`              | datetime  | Timestamp when category was last updated |

## **2.4 Indexes**

- Unique index on `category_name`:
```js
db.categories.createIndex({ category_name: 1 }, { unique: true });
```

---

# **3. Collection: `items`**

## **3.1 Purpose**
Store all item master data, including category and measurement.

## **3.2 Document Structure**

```json
{
  "_id": "ObjectId",
  "item_name": "string",
  "category_id": "ObjectId",
  "measurement_type": "string",
  "brand": "string|null",
  "notes": "string|null",
  "created_at": "ISODate",
  "updated_at": "ISODate"
}
```

## **3.3 Field Definitions**

| Field              | Type      | Description |
|--------------------|-----------|-------------|
| `_id`              | ObjectId  | Unique item ID |
| `item_name`        | string    | Name (e.g., "Toor Dal") |
| `category_id`      | ObjectId  | Reference to `categories._id` |
| `measurement_type` | string    | Unit for quantity entry (kg, g, L, ml, unit) |
| `brand`            | string    | Optional brand (e.g., "Tata") |
| `notes`            | string    | Optional notes/reminders |
| `created_at`       | datetime  | Creation timestamp |
| `updated_at`       | datetime  | Last modification timestamp |

## **3.4 Indexes**

- Index on `category_id` for fast filtering:
```js
db.items.createIndex({ category_id: 1 });
```

- Optional text index for fuzzy searching by name:
```js
db.items.createIndex({ item_name: "text" });
```

---

# **4. Collection: `shopping_lists`**

## **4.1 Purpose**
Represent each shopping list (e.g., "Jan 2025 Shopping").

## **4.2 Document Structure**

```json
{
  "_id": "ObjectId",
  "list_name": "string",
  "created_at": "ISODate",
  "updated_at": "ISODate"
}
```

## **4.3 Field Definitions**

| Field        | Type      | Description |
|--------------|-----------|-------------|
| `_id`        | ObjectId  | Unique list ID |
| `list_name`  | string    | Display name of the list |
| `created_at` | datetime  | When list was created |
| `updated_at` | datetime  | Last time list was modified |

## **4.4 Indexes**

- Index on `created_at` (for 12-month analytics):
```js
db.shopping_lists.createIndex({ created_at: -1 });
```

---

# **5. Collection: `shopping_list_items`**

## **5.1 Purpose**
Store required quantities for each item in a specific list.

## **5.2 Document Structure**

```json
{
  "_id": "ObjectId",
  "list_id": "ObjectId",
  "item_id": "ObjectId",
  "required_quantity": "number",
  "measurement_type": "string",
  "added_at": "ISODate"
}
```

## **5.3 Field Definitions**

| Field             | Type      | Description |
|-------------------|-----------|-------------|
| `_id`             | ObjectId  | Unique row ID |
| `list_id`         | ObjectId  | Reference to `shopping_lists._id` |
| `item_id`         | ObjectId  | Reference to `items._id` |
| `required_quantity`| number   | Planned quantity (as entered by user) |
| `measurement_type`| string    | Unit (kg, g, L, ml, unit) |
| `added_at`        | datetime  | When this item was added to the list |

## **5.4 Indexes**

- Compound index for (list_id, item_id):
```js
db.shopping_list_items.createIndex({ list_id: 1, item_id: 1 });
```

---

# **6. Collection: `actual_purchases`**

## **6.1 Purpose**
Store actual quantities purchased and their prices, after shopping.

## **6.2 Document Structure**

```json
{
  "_id": "ObjectId",
  "list_id": "ObjectId",
  "item_id": "ObjectId",
  "actual_quantity": "number",
  "unit_price": "number|null",
  "total_price": "number|null",
  "bill_id": "ObjectId|null",
  "updated_at": "ISODate"
}
```

## **6.3 Field Definitions**

| Field           | Type      | Description |
|-----------------|-----------|-------------|
| `_id`           | ObjectId  | Unique id of actual purchase record |
| `list_id`       | ObjectId  | Reference to `shopping_lists._id` |
| `item_id`       | ObjectId  | Reference to `items._id` |
| `actual_quantity`| number   | Quantity actually bought |
| `unit_price`    | number    | Price per unit (e.g., ₹ per kg) |
| `total_price`   | number    | Total price for this line item |
| `bill_id`       | ObjectId  | Optional link to `bills_metadata._id` |
| `updated_at`    | datetime  | Last updated timestamp |

## **6.4 Indexes**

- Compound index on `(list_id, item_id)`:
```js
db.actual_purchases.createIndex({ list_id: 1, item_id: 1 });
```

- Index on `bill_id` if linking to bills:
```js
db.actual_purchases.createIndex({ bill_id: 1 });
```

---

# **7. Collection: `bills_metadata`**

## **7.1 Purpose**
Store metadata and extracted AI data for each bill image.

## **7.2 Document Structure**

```json
{
  "_id": "ObjectId",
  "bill_gridfs_id": "ObjectId",
  "list_id": "ObjectId|null",
  "extracted_items": [
    {
      "raw_name": "string",
      "parsed_name": "string|null",
      "quantity": "number|string|null",
      "unit": "string|null",
      "unit_price": "number|null",
      "total_price": "number|null",
      "matched_item_id": "ObjectId|null"
    }
  ],
  "raw_llm_response": "object",
  "uploaded_at": "ISODate"
}
```

## **7.3 Field Definitions**

| Field           | Type      | Description |
|-----------------|-----------|-------------|
| `_id`           | ObjectId  | Unique bill metadata ID |
| `bill_gridfs_id`| ObjectId  | ID of file in GridFS (`bill_images.files`) |
| `list_id`       | ObjectId  | Optional reference to `shopping_lists._id` |
| `extracted_items`| array    | List of items extracted by LLM |
| `raw_llm_response`| object  | Unmodified full JSON response from LLM |
| `uploaded_at`   | datetime  | When bill was uploaded and processed |

### **Nested `extracted_items` fields**:

| Field           | Type   | Description |
|-----------------|--------|-------------|
| `raw_name`      | string | Original line text from bill (e.g., "Tur Dal 1kg") |
| `parsed_name`   | string | Cleaned name (e.g., "Toor Dal") |
| `quantity`      | number/string|null | Quantity extracted |
| `unit`          | string | Unit (kg, g, L, ml, unit, pcs) |
| `unit_price`    | number | Price per unit |
| `total_price`   | number | Line total |
| `matched_item_id`| ObjectId|null | Link to `items._id` if matched |

## **7.4 Indexes**

```js
db.bills_metadata.createIndex({ uploaded_at: -1 });
db.bills_metadata.createIndex({ list_id: 1 });
```

---

# **8. GridFS Collections: `bill_images.files` & `bill_images.chunks`**

MongoDB GridFS is used to store bill images efficiently.

## **8.1 `bill_images.files` Document Structure**

```json
{
  "_id": "ObjectId",
  "length": "number",
  "chunkSize": "number",
  "uploadDate": "ISODate",
  "filename": "string",
  "metadata": {
    "user": "string",
    "list_id": "ObjectId|null"
  }
}
```

## **8.2 `bill_images.chunks` Document Structure**

Stores binary chunks for each file; internal to GridFS.

---

# **9. Optional Collections**

## **9.1 `analytics_cache`**

Used to store precomputed analytics results (e.g., monthly spend, category charts) to speed up dashboard load.

```json
{
  "_id": "ObjectId",
  "key": "string",        // e.g., "summary_last_12_months"
  "payload": "object",    // arbitrary JSON (charts, numbers)
  "generated_at": "ISODate"
}
```

## **9.2 `ml_training_data`**

Optional storage for ML model snapshots or training data (Phase 2+).

```json
{
  "_id": "ObjectId",
  "model_name": "string",
  "version": "string",
  "created_at": "ISODate",
  "parameters": "object",
  "metrics": "object"
}
```

---

# **10. Indexing Strategy**

| Collection           | Index Definition                            | Purpose |
|----------------------|---------------------------------------------|---------|
| `categories`         | `{ category_name: 1 }` unique               | Fast lookup & uniqueness |
| `items`              | `{ category_id: 1 }`                        | Filter by category |
| `items`              | `{ item_name: "text" }` (optional)          | Text search on item name |
| `shopping_lists`     | `{ created_at: -1 }`                        | Recent lists for dashboard |
| `shopping_list_items`| `{ list_id: 1, item_id: 1 }`                | Fast lookups per list/item |
| `actual_purchases`   | `{ list_id: 1, item_id: 1 }`                | Analytics & ML joins |
| `bills_metadata`     | `{ uploaded_at: -1 }`                       | Recent bills |
| `bills_metadata`     | `{ list_id: 1 }`                            | Link bills to lists |

---

# **11. Relationships Overview**

```text
Category (1) ────────────────┐
                             │
                             ▼
                          Items (many)
                             │
         ┌────────────────────┴────────────────────┐
         ▼                                         ▼
Shopping Lists (1)                         Bills (1..many)
         │                                         │
         ▼                                         │
Shopping List Items (many)        →  bills_metadata, bill_images
         │
         ▼
Actual Purchases (many)
```

- **categories → items**: 1-to-many  
- **shopping_lists → shopping_list_items**: 1-to-many  
- **shopping_lists → actual_purchases**: 1-to-many  
- **bills_metadata → bill_images.files**: 1-to-1 (via `bill_gridfs_id`)  

---

# **12. Sample Documents**

## **12.1 Sample Category**

```json
{
  "_id": { "$oid": "676ac2f12345abcd12345678" },
  "category_name": "Pulses",
  "icon": "grain",
  "default_measurement_unit": "kg",
  "created_at": "2025-11-23T10:20:01Z",
  "updated_at": "2025-11-23T10:20:01Z"
}
```

## **12.2 Sample Item**

```json
{
  "_id": { "$oid": "676ac3159999abcd98765432" },
  "item_name": "Toor Dal",
  "category_id": { "$oid": "676ac2f12345abcd12345678" },
  "measurement_type": "kg",
  "brand": "Tata",
  "notes": "Prefer unpolished",
  "created_at": "2025-11-23T10:25:00Z",
  "updated_at": "2025-11-23T10:25:00Z"
}
```

## **12.3 Sample Shopping List**

```json
{
  "_id": { "$oid": "676ac36b2828123499887766" },
  "list_name": "Jan 2025 Shopping",
  "created_at": "2025-12-30T18:00:00Z",
  "updated_at": "2025-12-30T18:00:00Z"
}
```

## **12.4 Sample Shopping List Item**

```json
{
  "_id": { "$oid": "676ac4aa9988bbccdd001122" },
  "list_id": { "$oid": "676ac36b2828123499887766" },
  "item_id": { "$oid": "676ac3159999abcd98765432" },
  "required_quantity": 2.0,
  "measurement_type": "kg",
  "added_at": "2025-12-30T18:10:00Z"
}
```

## **12.5 Sample Actual Purchase**

```json
{
  "_id": { "$oid": "676ac5bb1199ccddee770011" },
  "list_id": { "$oid": "676ac36b2828123499887766" },
  "item_id": { "$oid": "676ac3159999abcd98765432" },
  "actual_quantity": 2.0,
  "unit_price": 110,
  "total_price": 220,
  "bill_id": { "$oid": "676ac44a2214aa9988776611" },
  "updated_at": "2025-12-30T19:15:00Z"
}
```

## **12.6 Sample Bill Metadata**

```json
{
  "_id": { "$oid": "676ac44a2214aa9988776611" },
  "bill_gridfs_id": { "$oid": "676ac44a0000bbccddeeff00" },
  "list_id": { "$oid": "676ac36b2828123499887766" },
  "extracted_items": [
    {
      "raw_name": "Tur Dal 1kg",
      "parsed_name": "Toor Dal",
      "quantity": 1,
      "unit": "kg",
      "unit_price": 110,
      "total_price": 110,
      "matched_item_id": { "$oid": "676ac3159999abcd98765432" }
    }
  ],
  "raw_llm_response": { "model": "gpt-4o-mini-vision", "raw_json": { } },
  "uploaded_at": "2025-12-30T19:00:00Z"
}
```

---

# **13. Data Retention Considerations**

For **Phase 1 (Local Application)**:
- No automatic purging; all data retained until user manually clears it.
- Bill images and metadata can accumulate; user can optionally prune old bills.

For **Phase 2 (Cloud – Future)**:
- Data retention policies may limit bill images to 12–24 months.
- Analytics & ML features can continue using aggregated historical data.

---

# **End of Part 5**

This file fully defines the MongoDB data model and can be handed directly to a backend developer or DBA.
