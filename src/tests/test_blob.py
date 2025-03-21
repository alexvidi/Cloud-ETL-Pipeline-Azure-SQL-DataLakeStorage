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

if not STORAGE_ACCOUNT or not STORAGE_KEY:
    raise ValueError(" Missing Azure Storage credentials in environment variables.")

# Build connection string
CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={STORAGE_ACCOUNT};AccountKey={STORAGE_KEY};EndpointSuffix=core.windows.net"

def test_blob_connection():
    """Test connection to Azure Blob Storage and list containers."""
    try:
        print(" Connecting to Azure Blob Storage...")
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        containers = blob_service_client.list_containers()

        print(" Connection to Azure Blob Storage successful!")
        print("Available Containers:")
        for container in containers:
            print(f"- {container['name']}")
    except Exception as e:
        print(" Failed to connect to Azure Blob Storage:", str(e))

if __name__ == "__main__":
    test_blob_connection()
