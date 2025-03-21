import os
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

def upload_file(file_path):
    """Upload a file to Azure Blob Storage."""
    try:
        # Ensure absolute path
        absolute_path = os.path.abspath(file_path)
        print(f" Absolute file path: {absolute_path}")

        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f" File not found: {absolute_path}")

        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(STORAGE_CONTAINER, os.path.basename(file_path))

        with open(absolute_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        print(f" Uploaded '{absolute_path}' to Blob Storage")
    except Exception as e:
        print(f" Error uploading '{file_path}':", str(e))

if __name__ == "__main__":
    # Ensure the path is correct
    file_path = "data/raw/sales_data_sample.csv"
    upload_file(file_path)

