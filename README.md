# 💳 Cloud Banking Platform: End-to-End ETL Pipeline (Python & Azure Simulation)

## Project Overview

This mini-project demonstrates an end-to-end **Extract, Transform, Load (ETL)** pipeline using Python and the Pandas library, simulating a data integration process within a Cloud Banking platform environment. The primary goal is to take raw customer data, perform essential data quality and enrichment tasks, and load the processed data into an optimized destination, ready for Business Intelligence (BI) reporting.

## 📌 Scenario & Business Goal

A banking platform needs to ingest customer transaction data (currently simulated via a static source) and clean it for regulatory compliance and advanced analytics. The pipeline mimics the function of a tool like **Azure Data Factory** by using Python to execute the transformation logic before loading the final dataset to a Data Warehouse (DWH) environment (simulated with SQLite/Azure SQL).

## Key Technologies & Skills Demonstrated

| Area | Technology / Tool | Skillset Highlight |
| :--- | :--- | :--- |
| **Data Orchestration** | Python 3, Pandas, `etl.py` | Building **modular, repeatable, and scalable** ETL logic. |
| **Data Sourcing (Extract)** | Local Excel Files (`.xlsx`) | Handling structured data formats and file I/O operations. |
| **Data Quality (Transform)** | Pandas `fillna()`, `to_numeric()` | **Data Cleansing** focusing on missing value imputation (Mean Imputation). |
| **Data Enrichment (Transform)**| Pandas `pd.cut()` (Feature Engineering) | Creating calculated dimensions (`IncomeCategory`) for deeper **analytical insights**. |
| **Data Loading (Load)** | SQLite (`dwh_demo.db`), CSV | Loading data into an optimized DWH structure for **SQL querying**. |
| **Reporting & BI** | Power BI Desktop | Connecting to cleaned data sources for **dynamic reporting and dashboarding**. |

---

## ETL Pipeline Steps

The core transformation logic is encapsulated in the **`etl.py`** script.

1.  **Extract:**
    * Reads raw customer data from the simulated source file, `musteriler.xlsx`.
2.  **Transform:**
    * **Data Imputation:** Fills missing `Gelir` (Income) values using the **mean average** of the existing income records.
    * **Standardization:** Enforces data consistency by converting city names (`Sehir`) to **Title Case**.
    * **Feature Engineering:** Creates a categorical dimension, `GelirKategori` (IncomeCategory), by segmenting income levels into 'Low', 'Medium', and 'High' bins using `pd.cut()`.
3.  **Load:**
    * The transformed dataset is simultaneously persisted to two destinations:
        * **`musteriler.csv`**: A lightweight source for BI tools like Power BI.
        * **`dwh_demo.db` (SQLite)**: A local simulation of an **Azure SQL Database** or Cloud DWH table, optimized for querying.

---

## Getting Started: Local Execution

### 1. Environment Setup

Clone the repository and install the required dependencies:

```bash
# Activate the virtual environment
venv\Scripts\activate

# Install required packages (pandas, openpyxl, sqlalchemy)
pip install -r requirements.txt