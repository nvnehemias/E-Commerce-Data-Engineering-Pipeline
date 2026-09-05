# E-Commerce Data Analytics & Analytics Engineering Pipeline

An end-to-end data pipeline built to ingest, clean, and transform large-scale Brazilian e-commerce transaction data (Olist dataset) into production-grade analytics models. 

This project demonstrates analytics engineering best practices, transitioning raw transactional data into structured Medallion Architecture data layers (**Staging**, **Intermediate**, and **Marts**) using **Python**, **PostgreSQL**, and **dbt**.

---

## 🛠️ Architecture & Data Flow

1. **Ingestion Layer:** Python scripts read raw multi-table CSV datasets, perform initial schema alignment, and load raw tables into PostgreSQL.
2. **Transformation Layer (dbt):**
   * **Staging (`stg_`):** Standardizes column naming, type casts timestamps, and cleans categorical fields.
   * **Intermediate (`int_`):** Handles complex logic, record deduplication, and order status aggregations.
   * **Marts (`fct_`, `dim_`):** Star-schema dimensional modeling tailored for business reporting (Orders, Customers, Products, Payments).

---

## 🚀 Key Features

* **Modular Data Modeling:** Clear separation between staging, intermediate logic, and final consumption models.
* **Data Quality & Testing:** Continuous schema testing (`not_null`, `unique`, foreign key relationships) built directly into dbt runs.
* **Scalable Ingestion Pipeline:** Automated Python scripts with configurable pathing and database connection parameters via `.env` management.
* **Business-Ready Analytics:** Structured datasets ready for executive key performance indicators (KPIs) like customer lifetime value (LTV), order fulfillment cycle times, and seller metrics.

---

## 📂 Repository Structure

```text
.
├── data/
│   └── raw/                    # Raw Olist CSV files (ignored in git)
├── dbt_project/                # dbt Project root directory
│   ├── models/
│   │   ├── staging/            # Staging views (stg_orders, stg_customers, etc.)
│   │   ├── intermediate/       # Business logic & aggregations
│   │   └── marts/              # Fact & Dimension tables
│   ├── dbt_project.yml         # dbt Configuration file
│   └── profiles.yml            # Database connection profiles
├── src/
│   └── ecommerce_pipeline/     # Python ingestion package / modules
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md
```
