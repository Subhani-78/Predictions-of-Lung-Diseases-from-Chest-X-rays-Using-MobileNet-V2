from src.config.configuration import Configuration
from src.logger import logging
from src.exception import CustomException
from src.entity.artifact_entity import *
from src.entity.config_entity import *
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import  DataValidation
from src.components.data_transformation import DataTransformation
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
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation = DataValidation(self.config.get_data_validation_config(), 
                                             data_ingestion_artifact = data_ingestion_artifact)
            
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def start_data_transformation(self, data_ingestion_artifact:DataIngestionArtifact) -> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                self.config.get_data_transformation_config(),
                data_ingestion_artifcat = data_ingestion_artifact
            )
            
            return data_transformation.initiate_data_transformation()
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact)
            
        except Exception as e:
            raise CustomException(e,sys) from e