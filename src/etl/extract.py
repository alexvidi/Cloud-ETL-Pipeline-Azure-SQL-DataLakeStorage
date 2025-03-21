import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Load configuration from config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config/config.json")

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

# Retrieve Azure Storage credentials
STORAGE_ACCOUNT = config["storage_account"]
STORAGE_CONTAINER = config["storage_container"]
STORAGE_KEY = os.getenv("AZURE_STORAGE_KEY")

# Build connection string
CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={STORAGE_ACCOUNT};AccountKey={STORAGE_KEY};EndpointSuffix=core.windows.net"

# Define the file name in Blob Storage and local path
BLOB_FILE_NAME = "sales_data_sample.csv"
LOCAL_FILE_PATH = os.path.join(os.getcwd(), "data/raw", BLOB_FILE_NAME)

def download_blob():
    """Download the sales data CSV from Azure Blob Storage."""
    try:
        print(f" Downloading '{BLOB_FILE_NAME}' from Azure Blob Storage...")
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(STORAGE_CONTAINER, BLOB_FILE_NAME)

        with open(LOCAL_FILE_PATH, "wb") as file:
            file.write(blob_client.download_blob().readall())

        print(f"File downloaded successfully: {LOCAL_FILE_PATH}")
    except Exception as e:
        print(f" Error downloading '{BLOB_FILE_NAME}':", str(e))

def load_data():
    """Load the sales data CSV into a Pandas DataFrame."""
    try:
        print(f" Loading data from '{LOCAL_FILE_PATH}'...")
        df = pd.read_csv(LOCAL_FILE_PATH, encoding="ISO-8859-1")
        print(f" Data loaded successfully! Shape: {df.shape}")
        return df
    except Exception as e:
        print(f" Error loading data: {str(e)}")
        return None

if __name__ == "__main__":
    download_blob()
    df = load_data()
