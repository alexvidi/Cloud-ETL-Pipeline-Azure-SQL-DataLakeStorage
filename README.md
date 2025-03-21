#  Azure Data Engineering Project

 **Overview**

This project demonstrates an ETL pipeline using Azure services to process and analyze sales data. It integrates Azure Data Lake Storage (ADLS Gen2), Azure SQL Database, and SQL queries to create a scalable data solution.

 **Azure Services Used**

* Azure Data Lake Storage (ADLS Gen2) → Stores raw and processed data efficiently.
* Azure SQL Database → Centralized storage for structured data.
* Azure Query Editor → Executes SQL queries for analysis.
* Python (Pandas, PyODBC) → Handles ETL processes.

 **ETL Process**

1.  **Extract** → Download raw data from Azure Data Lake Storage.
2.  **Transform** → Clean and preprocess data using Python.
3.  **Load** → Insert processed data into Azure SQL Database.
4.  **Analyze** → Run SQL queries to generate insights.

 **Project Structure**

---
azure-data-engineering/
├── data/               # Raw & processed datasets
│   ├── raw/            # Raw data files
│   ├── processed/      # Processed data files
│
├── queries/            # SQL queries for analysis
├── results/            # Exported query results
├── src/
│   ├── etl/            # Python ETL scripts
│   │   ├── extract.py  # Extract data from Azure Data Lake Storage
│   │   ├── transform.py  # Clean and preprocess data
│   │   ├── load_sql.py  # Load data into Azure SQL Database
│   │   ├── upload_to_blob.py  # Upload data to Data Lake Storage
│
├── images_azure/       # Screenshots of SQL analysis
├── config/             # Configuration files
├── tests/              # Unit tests for Blob Storage and SQL
├── venv/               # Virtual environment (excluded from Git)
├── .gitignore          # Git ignore file
├── .env                # Environment variables (excluded from Git)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
