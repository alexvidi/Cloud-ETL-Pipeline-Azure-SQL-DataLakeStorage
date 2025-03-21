import os
import pandas as pd
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Load configuration from config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config/config.json")

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

# Define file paths
RAW_FILE_PATH = os.path.join(os.getcwd(), "data/raw/sales_data_sample.csv")
PROCESSED_FILE_PATH = os.path.join(os.getcwd(), "data/processed/sales_data_cleaned.csv")

def transform_data():
    """Transform the raw sales data into a cleaned and structured format."""
    try:
        print(f" Loading raw data from: {RAW_FILE_PATH}")
        df = pd.read_csv(RAW_FILE_PATH, encoding="ISO-8859-1")

        # Drop duplicate rows if any
        df.drop_duplicates(inplace=True)

        # Drop rows with missing values in important columns
        df.dropna(subset=["ORDERNUMBER", "PRODUCTCODE", "ORDERDATE"], inplace=True)

        # Convert 'Order Date' to datetime format
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

        # Ensure numerical columns are correct
        df["PRICEEACH"] = pd.to_numeric(df["PRICEEACH"], errors="coerce")
        df["QUANTITYORDERED"] = pd.to_numeric(df["QUANTITYORDERED"], errors="coerce")

        # Standardize column names
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # Save the cleaned data
        os.makedirs(os.path.dirname(PROCESSED_FILE_PATH), exist_ok=True)
        df.to_csv(PROCESSED_FILE_PATH, index=False)

        print(f" Data transformation complete. Processed file saved at: {PROCESSED_FILE_PATH}")
        return df

    except Exception as e:
        print(f" Error during data transformation: {str(e)}")
        return None

if __name__ == "__main__":
    transform_data()
