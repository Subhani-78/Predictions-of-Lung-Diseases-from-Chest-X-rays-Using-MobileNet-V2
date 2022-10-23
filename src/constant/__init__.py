import imp
import os
from datetime import datetime
from tkinter import CURRENT


# Config file path in config directory
ROOT_DIR = os.getcwd()
CONFIG_DIR_NAME = "config"
CONFIG_FILE_NAME = "config.yml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR_NAME,CONFIG_FILE_NAME)


# Time Stamp Constants
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


# Logger Constants
LOG_DIR_NAME = "logs"

# Training Pipeline Config Constants

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_NAME = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR = "artifact_dir"

# Data Ingestion Config Contants

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL = "data_source_url"
DATA_INGESTION_LOCAL_ZIP_DATA_DIR = "local_zip_data_dir"
DATA_INGESTION_LOCAL_RAW_DATA_DIR = "local_raw_data_dir"
DATA_INGESTION_LOCAL_INGESTED_CSV_DATA_DIR = "local_ingested_csv_data_dir"
DATA_INGESTION_LOCAL_TRAIN_CSV_DATA_DIR = "local_train_csv_data_dir"
DATA_INGESTION_LOCAL_TEST_CSV_DATA_DIR = "local_test_csv_data_dir"
DATA_INGESTION_LOCAL_VAL_CSV_DATA_DIR = "local_val_csv_data_dir"

# Data Ingestion Component Constants
UNZIPED_DATA_FILE_NAME = "chest_xray"
LABEL_IMAGE_PATH = 'Label_Image_Path'
IMAGE_LABEL = 'Image_Label'
TRAIN_DATA = "train"
TEST_DATA = "test"
VAL_DATA = "val"
CSV_EXTENSION = '.csv'





