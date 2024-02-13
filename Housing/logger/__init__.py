import logging
from datetime import datetime 
import os

# All the log files will be stored LOG_DIR Directory.
LOG_DIR = "housing_logs"

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

# Creates directory, (exist_ok=TRUE is "If folder is not created than only the folder will be created").
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO
                    )



