import gdown
import os
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATA_DIR_LINK = "https://drive.google.com/drive/folders/1wR5MG_6e9N2zGjDVUyxawp_wJ1NSilE-"

project_root = Path(__file__).resolve().parents[2]
output_dir = project_root / 'data' / 'raw'


def download_data(google_drive_link, output_path):
    try:
        # Ensure the output directory exists
        os.makedirs(output_path, exist_ok=True)

        # Download the folder from Google Drive
        gdown.download_folder(google_drive_link, output=str(output_path), quiet=False)
        logger.info(f"Data downloaded successfully and saved to {output_path}")

    except Exception as e:
        logger.error(f"An error occurred while downloading the data: {e}")


if __name__ == '__main__':
    download_data(DATA_DIR_LINK, output_dir)
