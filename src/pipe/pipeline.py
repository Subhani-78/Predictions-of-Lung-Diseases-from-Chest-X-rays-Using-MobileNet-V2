from src.config.configuration import Configuration
from src.logger import logging
from src.exception import CustomException
from src.entity.artifact_entity import *
from src.entity.config_entity import *
from src.components.data_ingestion import DataIngestion
import os, sys


class Pipeline:
    
    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
            return 
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys) from e