# Azure Data Engineering Project

**Overview**

This project implements a robust ETL pipeline using Azure cloud services to process and analyze sales data. The solution leverages Azure Data Lake Storage, Azure SQL Database, and Python-based processing to create a scalable, enterprise-grade data solution.

**Azure Services Used**

* Azure Data Lake Storage (ADLS Gen2) - Hierarchical storage for raw and processed data files
* Azure SQL Database - Managed relational database for structured data storage and querying
* Azure Query Editor - Interactive tool for executing SQL queries and analysis
* Python Ecosystem - Pandas, PyODBC, and other libraries for ETL operations

**ETL Process**

1.  **Extract**
    * Download raw data from Azure Data Lake Storage
    * Connect to source systems using secure authentication
    * Validate data integrity during extraction
2.  **Transform**
    * Clean and preprocess data using Python and Pandas
    * Handle missing values, outliers, and data type conversions
    * Standardize formats and apply business rules
3.  **Load**
    * Insert processed data into Azure SQL Database
    * Maintain data lineage and versioning
    * Optimize for query performance
4.  **Analyze**
    * Execute SQL queries for business insights
    * Generate reports and visualizations
    * Support data-driven decision making

---

**Project Structure**

```
azure-data-engineering/
├── config/               # Configuration files
│   ├── config.json       # Project configuration file
│
├── data/                 # Raw & processed datasets
│   ├── raw/              # Raw data files
│   ├── processed/        # Processed data files
│
├── queries/              # SQL queries for analysis
│   ├── average_sales_price_order.sql  # SQL query for avg sales per order
│   ├── best-selling_product_quantity.sql  # Query for top-selling product
│   ├── total_quantity_sold_month.sql  # Query for total monthly sales
│
├── results/              # Exported query results
│   ├── average_sales_order.csv
│   ├── best_selling_product.csv
│   ├── total_quantity_month.csv
│
├── src/                  # Source code
│   ├── etl/              # Python ETL scripts
│   │   ├── extract.py    # Extract data from Azure Data Lake Storage
│   │   ├── transform.py  # Clean and preprocess data
│   │   ├── load_sql.py   # Load data into Azure SQL Database
│   │   ├── upload_to_blob.py  # Upload data to Data Lake Storage
│
├── images_azure/         # Screenshots of SQL analysis
│   ├── Average_sales_price_order.png
│   ├── Best-selling_product_quantity.png
│   ├── Total_quantity_sold_per_month.png
│
├── tests/                # Unit tests for Blob Storage and SQL
│   ├── test_blob.py       # Tests for Blob Storage functionality
│   ├── test_sql.py        # Tests for Azure SQL connection
│
├── venv/                 # Virtual environment (excluded from Git)
├── .gitignore            # Git ignore file
├── .env                  # Environment variables (excluded from Git)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
---
##  How to Use

1️ **Clone the repository:**

```bash
git clone [https://github.com/your-repo/azure-data-engineering.git](https://github.com/your-repo/azure-data-engineering.git)
cd azure-data-engineering

## 📌 How to Use

1️ **Clone the repository:**

```bash
git clone [https://github.com/your-repo/azure-data-engineering.git](https://github.com/your-repo/azure-data-engineering.git)
cd azure-data-engineering

2️ **Install dependencies:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

3️ **Run the ETL pipeline:**

```bash
python src/etl/upload_to_blob.py  # Upload data to Azure Data Lake Storage
python src/etl/extract.py         # Extract data from Data Lake Storage
python src/etl/transform.py       # Transform data
python src/etl/load_sql.py        # Load into Azure SQL Database

## Author

 Alexandre Vidal De Palol