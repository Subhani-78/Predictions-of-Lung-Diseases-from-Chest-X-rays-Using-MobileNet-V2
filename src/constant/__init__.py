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

# Data Validation Config Constants
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_SCHEMA_DIR_NAME = "schema_file_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME = "schema_file_name"
DATA_VALIDATION_REPORTS = 'local_validation_reports_dir'

# Data Validation Component Constants
DATA_VALIDATION_JSON_REPORT_FILE_NAME = "data_drift_report"

TRAIN_REPORT = "train_report"
TEST_REPORT = "test_report"
VAL_REPORT = "val_report"

TEXT_EXTENTION = '.txt'
JSON_EXTENTION = '.json'
HTML_EXTENSION = '.html'

SCHEMA_DATA_COLUMNS = 'columns'
SCHEMA_DATA_COLUMN_DATATYPES = 'column_datatypes'
SCHEMA_DATA_LABEL_IMAGE_PATH = 'Label_Image_Path'
SCHEMA_DATA_IMAGE_LABEL = 'Image_Label'
SCHEMA_DATA_DOMIAN_VALUES = 'domain_value'

# Data Transformation Config Constant

DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORMATION_DIR_NAME = "transformed_data_dir"
DATA_TRANSFORMATION_TRAIN_DIR_NAME = "transformed_train_data_dir"
DATA_TRANSFORMATION_TEST_DIR_NAME = "transformed_test_data_dir"
DATA_TRANSFORMATION_VAL_DIR_NAME = "transformed_val_data_dir"

# Data Transformation Component Constants

IMAGE_SIZE = 224
BATCH_SIZE = 64
IMAGE_RESCALE = 1./255
INTERPOLATION = 'bilinear'
CLASS_MODE = "binary"

LABELS = ['NORMAL','PNEUMONIA']







