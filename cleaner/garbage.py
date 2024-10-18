
import glob
import os
import logging
from pathlib import Path

async def clean_media_after_timeout():
    media_path = Path("media")

    if not media_path.exists():
        logging.warning(f"Media path '{media_path}' does not exist. Skipping cleanup.")
        return

    files = glob.glob(str(media_path / "*"))
    
    if not files:
        logging.info("No media files to clean.")
        return

    logging.info(f"Cleaning {len(files)} media files...")
    
    for file in files:
        try:
            os.remove(file)
            logging.info(f"Removed file: {file}")
        except Exception as e:
            logging.error(f"Error removing file {file}: {e}")

