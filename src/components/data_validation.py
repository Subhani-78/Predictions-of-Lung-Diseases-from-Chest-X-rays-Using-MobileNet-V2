import json
import sys, os
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import *
from src.entity.artifact_entity import *
from src.utils.utils import *

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json


class DataValidation:
    
    def __init__(self, data_validation_config: DataValidationConfig, data_ingestion_artifact: DataIngestionArtifact) :
        try:
            logging.info(f" {'>>' * 30} Data Validation has been Started. {'>>' * 30}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.schema_file_info = read_yaml_file(file_path = data_validation_config.schema_file_path)
            
        except Exception as e:
            raise CustomException(e,sys) from e
    
    def get_train_test_and_val_df(self):
        
        """
        It returns dataframes for test, train and validation data
        
            Parameters: None

            Returns: 
                train_df (dataframe), test_df (dataframe), val_df (dataframe)
        """
        
        try:
            
            train_df = pd.read_csv(self.data_ingestion_artifact.ingested_data_csv_train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.ingested_data_csv_test_file_path)
            val_df = pd.read_csv(self.data_ingestion_artifact.ingested_data_csv_val_file_path)
            
            return train_df, test_df, val_df
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def is_train_test_and_val_file_exit(self) -> None:
        
        """
        It checks if dataframes for test, train and validation data exits
        
            Parameters: None

            Returns: None
        """
        
        try:
            logging.info("Checking if training, testing and validation dataframes exits")
            
            is_train_file_exit = False
            is_test_file_exit = False
            is_val_file_exit = False
            
            train_file_path = self.data_ingestion_artifact.ingested_data_csv_train_file_path
            test_file_path = self.data_ingestion_artifact.ingested_data_csv_test_file_path
            val_file_path = self.data_ingestion_artifact.ingested_data_csv_val_file_path
            
            is_train_file_exit = os.path.exists(train_file_path)
            is_test_file_exit = os.path.exists(test_file_path)
            is_val_file_exit = os.path.exists(val_file_path)
            
            if is_train_file_exit == is_test_file_exit == is_val_file_exit == True:
                logging.info(f"Dataframes for training, testing and validation exits.")
            else:
                message = f"Training file : {train_file_path}, testing file : {test_file_path} and validation file : {val_file_path} is not present."
                
                raise Exception(message)
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def validate_dataset_schema(self) -> bool:
        
        """
        It validates the train, test and val dataframes with our schema file.
        
            Parameters: None

            Returns: 
                is_train_valid (bool), is_test_valid (bool), is_val_valid (bool)
        """        
        
        try:
            
            # result = (on_false, on_true)[condition]
            
            is_train_valid = False
            is_test_valid = False
            is_val_valid = False
            
            logging.info(f"Validating the schema of training, testing and validating dataframe.")
            train_df, test_df, val_df = self.get_train_test_and_val_df()
            

            logging.info(f"Starting to validate train dataframe.")
            is_train_valid = (False,True)[train_df.columns[0] == self.schema_file_info[SCHEMA_DATA_COLUMNS][0] and 
                              train_df.columns[1] == self.schema_file_info[SCHEMA_DATA_COLUMNS][1] and 
                              train_df.dtypes[train_df.columns[0]] == self.schema_file_info[SCHEMA_DATA_COLUMN_DATATYPES][SCHEMA_DATA_LABEL_IMAGE_PATH] and 
                              train_df.dtypes[train_df.columns[1]] == self.schema_file_info[SCHEMA_DATA_COLUMN_DATATYPES][SCHEMA_DATA_IMAGE_LABEL] and 
                              train_df[train_df.columns[1]].unique()[0] == self.schema_file_info[SCHEMA_DATA_DOMIAN_VALUES][SCHEMA_DATA_IMAGE_LABEL][0] and
                              train_df[train_df.columns[1]].unique()[1] == self.schema_file_info[SCHEMA_DATA_DOMIAN_VALUES][SCHEMA_DATA_IMAGE_LABEL][1]]
            logging.info(f"Train Dataframe has a validation result {is_train_valid} .")
            
            logging.info(f"Starting to validate test dataframe.")
            is_test_valid = (False,True)[test_df.columns[0] == self.schema_file_info[SCHEMA_DATA_COLUMNS][0] and 
                              test_df.columns[1] == self.schema_file_info[SCHEMA_DATA_COLUMNS][1] and 
                              test_df.dtypes[test_df.columns[0]] == self.schema_file_info[SCHEMA_DATA_COLUMN_DATATYPES][SCHEMA_DATA_LABEL_IMAGE_PATH] and 
                              test_df.dtypes[test_df.columns[1]] == self.schema_file_info[SCHEMA_DATA_COLUMN_DATATYPES][SCHEMA_DATA_IMAGE_LABEL] and 
                              test_df[test_df.columns[1]].unique()[0] == self.schema_file_info[SCHEMA_DATA_DOMIAN_VALUES][SCHEMA_DATA_IMAGE_LABEL][0] and
                              test_df[test_df.columns[1]].unique()[1] == self.schema_file_info[SCHEMA_DATA_DOMIAN_VALUES][SCHEMA_DATA_IMAGE_LABEL][1]]
            logging.info(f"Test Dataframe has a validation result {is_test_valid} .")
            
            logging.info(f"Starting to validate validation dataframe.")
            is_val_valid = (False,True)[val_df.columns[0] == self.schema_file_info[SCHEMA_DATA_COLUMNS][0] and 
                              val_df.columns[1] == self.schema_file_info[SCHEMA_DATA_COLUMNS][1] and 
                              val_df.dtypes[val_df.columns[0]] == self.schema_file_info[SCHEMA_DATA_COLUMN_DATATYPES][SCHEMA_DATA_LABEL_IMAGE_PATH] and 
                              val_df.dtypes[val_df.columns[1]] == self.schema_file_info[SCHEMA_DATA_COLUMN_DATATYPES][SCHEMA_DATA_IMAGE_LABEL] and 
                              val_df[val_df.columns[1]].unique()[0] == self.schema_file_info[SCHEMA_DATA_DOMIAN_VALUES][SCHEMA_DATA_IMAGE_LABEL][0] and
                              val_df[val_df.columns[1]].unique()[1] == self.schema_file_info[SCHEMA_DATA_DOMIAN_VALUES][SCHEMA_DATA_IMAGE_LABEL][1]]
            logging.info(f"Validation Dataframe has a validation result {is_val_valid} .")
            
            return is_train_valid, is_test_valid, is_val_valid
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def get_validation_reports(self):
        try:
            is_train_valid, is_test_valid, is_val_valid = self.validate_dataset_schema()
            train_df, test_df, val_df = self.get_train_test_and_val_df()
            
            # Validation report directory path for train, test and val data
            data_validation_reports_file_path = self.data_validation_config.data_validation_reports_file_path
            
            os.makedirs(data_validation_reports_file_path, exist_ok=True)
            
            train_data_validation_text_report_file_path = os.path.join(data_validation_reports_file_path,TRAIN_REPORT +
                                                                TEXT_EXTENTION)
            
            test_data_validation_text_report_file_path = os.path.join(data_validation_reports_file_path,TEST_REPORT +
                                                                TEXT_EXTENTION)

            val_data_validation_text_report_file_path = os.path.join(data_validation_reports_file_path,VAL_REPORT +
                                                                TEXT_EXTENTION)            
            
            if is_train_valid == True and is_test_valid == True and is_val_valid == True:
                
                logging.info(f"Writing validation reports for train dataframe.")
                
                text_report = open(train_data_validation_text_report_file_path, 'a')
                text_report.write('No. of features in dataframe : ' + str(len(train_df.columns)) + '\n')
                text_report.write('No. of rows in dataframe : ' + str(train_df.shape[0])+ '\n')
                text_report.write('Features in dataframe : ' + str(train_df.columns)+ '\n')
                text_report.write('Categories in ' + str(train_df.columns[1]) + ' : ' + str(train_df.Image_Label.unique())+ '\n')
                text_report.write('No. of rows for ' + str(train_df.Image_Label.unique()[0]) + ' : ' + str(len(train_df[train_df.Image_Label == train_df.Image_Label.unique()[0]]))+ '\n')
                text_report.write('No. of rows for ' + str(train_df.Image_Label.unique()[1]) + ' : ' + str(len(train_df[train_df.Image_Label == train_df.Image_Label.unique()[1]]))+ '\n')
                text_report.close()
                
                logging.info(f"Writing validation reports for test dataframe.")
                
                text_report = open(test_data_validation_text_report_file_path, 'a')
                text_report.write('No. of features in dataframe : ' + str(len(test_df.columns)) + '\n')
                text_report.write('No. of rows in dataframe : ' + str(test_df.shape[0])+ '\n')
                text_report.write('Features in dataframe : ' + str(test_df.columns)+ '\n')
                text_report.write('Categories in ' + str(test_df.columns[1]) + ' : ' + str(test_df.Image_Label.unique())+ '\n')
                text_report.write('No. of rows for ' + str(test_df.Image_Label.unique()[0]) + ' : ' + str(len(test_df[test_df.Image_Label == test_df.Image_Label.unique()[0]]))+ '\n')
                text_report.write('No. of rows for ' + str(test_df.Image_Label.unique()[1]) + ' : ' + str(len(test_df[test_df.Image_Label == test_df.Image_Label.unique()[1]]))+ '\n')
                text_report.close()
                
                
                logging.info(f"Writing validation reports for validation dataframe.")
                
                text_report = open(val_data_validation_text_report_file_path, 'a')
                text_report.write('No. of features in dataframe : ' + str(len(val_df.columns)) + '\n')
                text_report.write('No. of rows in dataframe : ' + str(val_df.shape[0])+ '\n')
                text_report.write('Features in dataframe : ' + str(val_df.columns)+ '\n')
                text_report.write('Categories in ' + str(val_df.columns[1]) + ' : ' + str(val_df.Image_Label.unique())+ '\n')
                text_report.write('No. of rows for ' + str(val_df.Image_Label.unique()[0]) + ' : ' + str(len(val_df[val_df.Image_Label == val_df.Image_Label.unique()[0]]))+ '\n')
                text_report.write('No. of rows for ' + str(val_df.Image_Label.unique()[1]) + ' : ' + str(len(val_df[val_df.Image_Label == val_df.Image_Label.unique()[1]]))+ '\n')
                text_report.close()
                
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])
            train_df, test_df, val_df = self.get_train_test_and_val_df()
            profile.calculate(train_df,test_df)
            report = json.loads(profile.json())
                
                # Validation report directory path for train, test and val data
            data_validation_reports_file_path = self.data_validation_config.data_validation_reports_file_path
                
            os.makedirs(data_validation_reports_file_path, exist_ok=True)
                
            data_validation_json_report_file_path = os.path.join(
                data_validation_reports_file_path,
                DATA_VALIDATION_JSON_REPORT_FILE_NAME +
                JSON_EXTENTION
            )
                
            with open(data_validation_json_report_file_path, 'w') as report_file:
                json.dump(report, report_file, indent=6)
                
            return report
            
        except Exception as e:
                raise CustomException(e,sys) from e
            
            
    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df, val_df = self.get_train_test_and_val_df()
            dashboard.calculate(train_df,test_df)
            
            # Validation report directory path for train, test and val data
            data_validation_reports_file_path = self.data_validation_config.data_validation_reports_file_path
            
            os.makedirs(data_validation_reports_file_path, exist_ok=True)
            
            data_validation_webpage_report_file_path = os.path.join(
                data_validation_reports_file_path,
                DATA_VALIDATION_JSON_REPORT_FILE_NAME +
                HTML_EXTENSION
            )
            
            dashboard.save(data_validation_webpage_report_file_path)
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def is_data_drift_found(self) :
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            
            return True
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_and_val_file_exit()
            self.validate_dataset_schema()
            self.get_validation_reports()
            self.is_data_drift_found()
            
            data_validation_artifact = DataValidationArtifact(
                schema_file_path= self.data_validation_config.schema_file_path,
                data_validation_reports_file_path= self.data_validation_config.data_validation_reports_file_path,
                is_validated= True,
                message= "Data Validation Performed Sucessfully"
            )
            
            logging.info(f"Data Validation Artifact : {data_validation_artifact}")
            
            return data_validation_artifact
            
        except Exception as e:
            raise CustomException(e,sys) from e