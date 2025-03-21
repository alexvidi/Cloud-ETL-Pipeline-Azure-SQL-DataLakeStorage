import os
import pandas as pd
import pyodbc
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Load configuration from config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config/config.json")

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

# Retrieve Azure SQL credentials
SQL_SERVER = config["sql_server"]
SQL_DATABASE = config["sql_database"]
SQL_USER = os.getenv("AZURE_SQL_USER")
SQL_PASSWORD = os.getenv("AZURE_SQL_PASSWORD")

# Build connection string
CONNECTION_STRING = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USER};PWD={SQL_PASSWORD};Encrypt=yes;TrustServerCertificate=yes"

# Define processed data path
PROCESSED_FILE_PATH = os.path.join(os.getcwd(), "data/processed/sales_data_cleaned.csv")

def create_table():
    """Create sales table in Azure SQL Database if it doesn't exist."""
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        cursor = conn.cursor()
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'sales_data')
            CREATE TABLE sales_data (
                ORDERNUMBER INT PRIMARY KEY,
                PRODUCTCODE VARCHAR(50),
                ORDERDATE DATE,
                QUANTITYORDERED INT,
                PRICEEACH FLOAT,
                SALES FLOAT
            );
        """)
        conn.commit()
        conn.close()
        print(" Table 'sales_data' checked/created successfully.")
    except Exception as e:
        print(f" Error creating table: {str(e)}")

def load_data():
    """Load transformed sales data into Azure SQL Database, avoiding duplicates."""
    try:
        print(f" Loading transformed data from: {PROCESSED_FILE_PATH}")
        df = pd.read_csv(PROCESSED_FILE_PATH, encoding="ISO-8859-1")

        # Ensure column names match SQL table
        df.columns = df.columns.str.upper().str.replace(" ", "_")

        # Convert ORDERDATE to proper datetime format
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

        # Remove duplicate ORDERNUMBER values
        df.drop_duplicates(subset=["ORDERNUMBER"], keep="first", inplace=True)

        # Connect to Azure SQL
        conn = pyodbc.connect(CONNECTION_STRING)
        cursor = conn.cursor()

        # Check existing ORDERNUMBERs in SQL to avoid duplicates
        cursor.execute("SELECT ORDERNUMBER FROM sales_data")
        existing_orders = {row[0] for row in cursor.fetchall()}

        new_records = df[~df["ORDERNUMBER"].isin(existing_orders)]

        if new_records.empty:
            print(" No new records to insert. Database is up-to-date.")
        else:
            for _, row in new_records.iterrows():
                cursor.execute("""
                    INSERT INTO sales_data (ORDERNUMBER, PRODUCTCODE, ORDERDATE, QUANTITYORDERED, PRICEEACH, SALES)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, row["ORDERNUMBER"], row["PRODUCTCODE"], row["ORDERDATE"], row["QUANTITYORDERED"], row["PRICEEACH"], row["SALES"])
            
            conn.commit()
            print(f" Successfully inserted {len(new_records)} new records into Azure SQL Database.")

        conn.close()

    except Exception as e:
        print(f" Error loading data: {str(e)}")

if __name__ == "__main__":
    create_table()
    load_data()


