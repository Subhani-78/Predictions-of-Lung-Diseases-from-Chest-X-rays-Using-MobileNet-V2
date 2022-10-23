from ensure import ensure_annotations
from src.entity.config_entity import *
from src.constant import *
import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.utils.utils import read_yaml_file

class Configuration:
    
    
    def __init__(self, config_file_path = CONFIG_FILE_PATH, 
                 current_time_stamp = CURRENT_TIME_STAMP) -> None :
        
        self.config_file_info = read_yaml_file(file_path = config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        """
        Returns a named tuple containg file paths of all directories required for data ingestion.
        
            Parameters: None

            Returns: 
                data_ingestion_config (named tuple) -> It contains file path for the following directiories
                
                    1. Ziped_Data (Contains downloaded ziped data)
                    2. Raw_Data (Contains raw train, test and val data)
                    3. Ingested_CSV_Data (Contains csv train,test and val data)
                    4. Train_CSV_Data (Contains train csv data)
                    5. Test_CSV_Data (Contains test csv data)
                    6. Val_CSV_Data (Contains val csv data)
        """
        
        try:
            
            # Path to artifact directory
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            
            # Path to data_ingestion in artifcat directory
            data_ingestion_artifcat_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            
            data_ingestion_config_file_info = self.config_file_info[DATA_INGESTION_CONFIG_KEY]
            
            
            # Contains source to data
            data_source_url = data_ingestion_config_file_info[DATA_INGESTION_DOWNLOAD_URL]
            
            # Path to ziped_data in data_ingestion//artifact
            local_zip_data_dir = os.path.join(
                data_ingestion_artifcat_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_ZIP_DATA_DIR]
            )
            
            
            # Path to raw_data in data_ingestion//artifact
            local_raw_data_dir = os.path.join(
                data_ingestion_artifcat_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_RAW_DATA_DIR]
            )
            
            
            # Path to ingested_csv_data in data_ingestion//artifact
            local_ingested_csv_data_dir = os.path.join(
                data_ingestion_artifcat_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_INGESTED_CSV_DATA_DIR]
            )
            
            # Path to train_csv_data in ingested_csv_data//data_ingestion//artifact
            local_train_csv_data_dir = os.path.join(
                local_ingested_csv_data_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_TRAIN_CSV_DATA_DIR]
            )
            
            # Path to test_csv_data in ingested_csv_data//data_ingestion//artifact
            local_test_csv_data_dir = os.path.join(
                local_ingested_csv_data_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_TEST_CSV_DATA_DIR]
            )
            
            # Path to val_csv_data in ingested_csv_data//data_ingestion//artifact
            local_val_csv_data_dir = os.path.join(
                local_ingested_csv_data_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_VAL_CSV_DATA_DIR]
            )
            
            
            data_ingestion_config = DataIngestionConfig(
                data_source_url=data_source_url,
                local_zip_data_dir= local_zip_data_dir,
                local_raw_data_dir = local_raw_data_dir,
                local_ingested_csv_data_dir = local_ingested_csv_data_dir,
                local_train_csv_data_dir = local_train_csv_data_dir,
                local_test_csv_data_dir = local_test_csv_data_dir,
                local_val_csv_data_dir = local_val_csv_data_dir
            )
            
            logging.info(f" Data Ingestion Config : [{data_ingestion_config}]")
            
            return data_ingestion_config
            
            
        except Exception as e:
            raise CustomException(sys,e) from e
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        
        """
        Returns a named tuple containg path to artifact directory.
        
            Parameters: None

            Returns:
                training_pipeline_config (named tuple): Contains complete path of artifact directory.
        """
        
        
        try:
            training_pipeline_config = self.config_file_info[TRAINING_PIPELINE_CONFIG_KEY] 
            artifact_dir = os.path.join(ROOT_DIR, training_pipeline_config[TRAINING_PIPELINE_NAME],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR]) 
            
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            
            logging.info(f" Training Pipeline Config : [{training_pipeline_config}]")
            
            
            return training_pipeline_config
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
        

