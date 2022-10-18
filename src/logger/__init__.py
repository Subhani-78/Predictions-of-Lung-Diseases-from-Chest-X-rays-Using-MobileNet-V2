import logging
from src.constant import LOG_DIR_NAME
from datetime import datetime
import os


# Current time stamp for logging
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Logging directory name
LOG_DIR_NAME = LOG_DIR_NAME

# Logging file name
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

# Creating a logging directory
os.makedirs(LOG_DIR_NAME,exist_ok=True)

# Logging Files Path
LOG_FILE_PATH = os.path.join(LOG_DIR_NAME,LOG_FILE_NAME)

# Writing logging details on logging files
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



