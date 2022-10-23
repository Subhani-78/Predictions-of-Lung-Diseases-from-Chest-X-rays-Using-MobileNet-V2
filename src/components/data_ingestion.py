import sys, os
import zipfile
from six.moves import urllib
from src.constant import CSV_EXTENSION, TEST_DATA, TRAIN_DATA, UNZIPED_DATA_FILE_NAME, VAL_DATA
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.utils.utils import convert_into_csv_format, description_base_dir, description_label_dirs


class DataIngestion:
    
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info("Data Ingestion Log Started.")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys) from e
        
                 
    def download_zip_data(self) -> str:
        
        """
        Downloads the ziped data from source url into local_zip_data_dir_path.
        
            Parameters: None

            Returns:
                local_zip_data_dir_path (str): File path of directory containing ziped data.
        """
        
        try:
            # Contains direct download url for data
            download_url = self.data_ingestion_config.data_source_url
            
            # Location to download ziped data file
            local_zip_data_dir = self.data_ingestion_config.local_zip_data_dir
            
            
            # Creating a directory ziped_data
            if os.path.exists(local_zip_data_dir):
                os.remove(local_zip_data_dir)
                
            os.makedirs(local_zip_data_dir, exist_ok=True)
            
            
            # Basename for data ziped file
            basename = os.path.basename(download_url)[:-5]
            
            # Path of basename (ziped data file)
            local_zip_data_dir_path = os.path.join(local_zip_data_dir,basename)
            
            logging.info(f"Downloading of ziped data file has started.")
            # To download ziped data file in the directory
            urllib.request.urlretrieve(download_url,local_zip_data_dir_path)
            logging.info(f"Downloading of ziped data file completed.")
            
            return local_zip_data_dir_path
            
        except Exception as e:
            raise CustomException(e,sys) from e
    
    def extract_zip_data(self,local_zip_data_dir_path:str) -> str:
        
        """
        Extracts ziped_data in raw_data directory.
        
            Parameters: local_zip_data_dir_path (str)

            Returns: 
                local_raw_data_dir_path (str): File path of directory containing raw data.

        """
        
        try:
            # Location of raw_data directory containg train, test and val data
            local_raw_data_dir_path = self.data_ingestion_config.local_raw_data_dir
            
            # Creating a directory raw_data
            if os.path.exists(local_raw_data_dir_path):
                os.remove(local_raw_data_dir_path)
                
            os.makedirs(local_raw_data_dir_path, exist_ok=True)
            
            
            logging.info("Extaracted of ziped file started.")
            # Extracting the ziped file in raw_data directory
            with zipfile.ZipFile(local_zip_data_dir_path, 'r') as zip_ref:
                zip_ref.extractall(local_raw_data_dir_path)
            logging.info("Extaracted of ziped file completed.")
            
            return local_raw_data_dir_path
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def get_raw_data_train_test_val_path(self, local_raw_data_dir_path: str) -> tuple[str,str,str]:
        
        """
        Returns paths for raw data of train, test and validation.
        
            Parameters: local_raw_data_dir_path (str)

            Returns: 
                local_train_raw_data_dir (str), local_test_raw_data_dir (str), local_val_raw_data_dir (str): Paths of train, test and validation directories containing csv data.

        """
        
        try:
            
            # Creating a file path to chest_xray in raw_data directory
            file_local_raw_data_dir_path = os.path.join(local_raw_data_dir_path,UNZIPED_DATA_FILE_NAME)
            
            # Creating a file path to train directory in chest_xray
            local_train_raw_data_dir_path = os.path.join(file_local_raw_data_dir_path,TRAIN_DATA)
            logging.info(f"Raw train data directory : [{local_train_raw_data_dir_path}]")
            
            # Creating a file path to test directory in chest_xray
            local_test_raw_data_dir_path = os.path.join(file_local_raw_data_dir_path, TEST_DATA)
            logging.info(f"Raw test data directory : [{local_train_raw_data_dir_path}]")
            
            # Creating a file path to val directory in chest_xray
            local_val_raw_data_dir_path = os.path.join(file_local_raw_data_dir_path, VAL_DATA)
            logging.info(f"Raw validation data directory : [{local_train_raw_data_dir_path}]")
            
            return local_train_raw_data_dir_path, local_test_raw_data_dir_path, local_val_raw_data_dir_path
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def get_ingested_csv_train_test_val_path(self) -> tuple[str,str,str]:
        
        """
        Returns paths for ingested csv data for train, test and validation.
        
            Parameters: None

            Returns: 
                local_train_csv_data_dir (str), local_test_csv_data_dir (str), local_val_csv_data_dir (str): Paths of train, test and validation directories containing csv data.

        """
        
        try:
            # Location of ingested_data directory containg train, test and val data csv
            local_ingested_csv_data_dir = self.data_ingestion_config.local_ingested_csv_data_dir
            
            # Creating a ingested_data directory
            if os.path.exists(local_ingested_csv_data_dir):
                os.remove(local_ingested_csv_data_dir)
                
            os.makedirs(local_ingested_csv_data_dir,exist_ok=True)
            
            
            # Location for train_data that contain train data csv
            local_train_csv_data_dir = self.data_ingestion_config.local_train_csv_data_dir
            
            # Creating a train_data directory in ingested_data
            if os.path.exists(local_train_csv_data_dir):
                os.remove(local_train_csv_data_dir)
                
            os.makedirs(local_train_csv_data_dir,exist_ok=True)
            
            
            # Location for test_data that contain test data csv
            local_test_csv_data_dir = self.data_ingestion_config.local_test_csv_data_dir
            
            # Creating a test_data directory in ingested_data
            if os.path.exists(local_test_csv_data_dir):
                os.remove(local_test_csv_data_dir)
                
            os.makedirs(local_test_csv_data_dir,exist_ok=True)
            
            
            # Location for val_data that contain test data csv
            local_val_csv_data_dir = self.data_ingestion_config.local_val_csv_data_dir
            
            # Creating a val_data directory in ingested_data
            if os.path.exists(local_val_csv_data_dir):
                os.remove(local_val_csv_data_dir)
                
            os.makedirs(local_val_csv_data_dir,exist_ok=True)
            
            
            return local_train_csv_data_dir, local_test_csv_data_dir, local_val_csv_data_dir
            
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def convert_raw_data_as_ingested_train_test_val_csv(self, local_train_csv_data_dir, local_test_csv_data_dir, local_val_csv_data_dir, local_train_raw_data_dir, local_test_raw_data_dir, local_val_raw_data_dir) -> DataIngestionArtifact:
        
        """
        Converts raw train, test and validation data into trai, test and validation csv files.
        
            Parameters: None

            Returns: 
                data_ingestion_artifact (named tuple) -> It contains file path for the following directiories
            
                1. raw_data_train_file_path (path to raw train data)
                2. raw_data_test_file_path (path to raw test data)
                3. raw_data_val_file_path (path to val data)
                4. ingested_data_csv_train_file_path (path to train csv)
                5. ingested_data_csv_test_file_path (path to test csv)
                6. ingested_data_csv_val_file_path (path to val csv)
            )

        """
        
        try:
            
            # Getting train_csv_data for train_raw_data in train_data//ingested_data
            logging.info(f" Store directory for train data csv : [{local_train_csv_data_dir}]")
            _,_, train_label_data_dir_path = description_base_dir(dir_path=local_train_raw_data_dir)
            train_label_images_paths, train_images_labels = description_label_dirs(label_data_dir_paths=train_label_data_dir_path)
            convert_into_csv_format(label_images_paths = train_label_images_paths,label_images_labels = train_images_labels, store_dir = local_train_csv_data_dir)
            
            
            # Getting test_csv_data for train_raw_data in test_data//ingested_data
            logging.info(f" Store directory for test data csv : [{local_test_csv_data_dir}]")
            _,_, test_label_data_dir_path = description_base_dir(dir_path=local_test_raw_data_dir)
            test_label_images_paths, test_images_labels = description_label_dirs(label_data_dir_paths=test_label_data_dir_path)
            convert_into_csv_format(label_images_paths = test_label_images_paths,label_images_labels = test_images_labels, store_dir = local_test_csv_data_dir)
            
            
            # Getting test_csv_data for train_raw_data in val_data//ingested_data
            logging.info(f" Store directory for validation data csv : [{local_val_csv_data_dir}]")
            _,_, val_label_data_dir_path = description_base_dir(dir_path=local_val_raw_data_dir)
            val_label_images_paths, val_images_labels = description_label_dirs(label_data_dir_paths=val_label_data_dir_path)
            convert_into_csv_format(label_images_paths = val_label_images_paths,label_images_labels = val_images_labels, store_dir = local_val_csv_data_dir)
            
            # Train, test & validation csv file name
            train_csv_file = os.path.basename(local_train_csv_data_dir) + CSV_EXTENSION
            test_csv_file = os.path.basename(local_test_csv_data_dir) + CSV_EXTENSION
            val_csv_file = os.path.basename(local_val_csv_data_dir) + CSV_EXTENSION
            
            # Creating a path to train, test and csv data
            ingested_data_csv_train_file_path = os.path.join(local_train_csv_data_dir,train_csv_file)
            logging.info(f" Train csv data directory : [{ingested_data_csv_train_file_path}]")
            
            ingested_data_csv_test_file_path = os.path.join(local_test_csv_data_dir,test_csv_file)
            logging.info(f" Test csv data directory : [{ingested_data_csv_test_file_path}]")
            
            ingested_data_csv_val_file_path = os.path.join(local_val_csv_data_dir,val_csv_file)
            logging.info(f" Validation csv data directory : [{ingested_data_csv_val_file_path}]")
            
            
            data_ingestion_artifcat = DataIngestionArtifact(
                raw_data_train_file_path = local_train_raw_data_dir,
                raw_data_test_file_path = local_test_raw_data_dir,
                raw_data_val_file_path = local_val_raw_data_dir,
                ingested_data_csv_train_file_path = ingested_data_csv_train_file_path,
                ingested_data_csv_test_file_path= ingested_data_csv_test_file_path,
                ingested_data_csv_val_file_path= ingested_data_csv_val_file_path,
                is_ingested= True,
                message = f"Data Ingestion completed successfully"
            )
            
            logging.info(f" Data Ingestion Artifact : [{data_ingestion_artifcat}]")
            
            return data_ingestion_artifcat
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            local_zip_data_dir_path = self.download_zip_data()
            local_raw_data_dir_path = self.extract_zip_data(local_zip_data_dir_path=local_zip_data_dir_path)
            local_train_raw_data_dir, local_test_raw_data_dir, local_val_raw_data_dir = self.get_raw_data_train_test_val_path(local_raw_data_dir_path=local_raw_data_dir_path)
            local_train_csv_data_dir, local_test_csv_data_dir, local_val_csv_data_dir = self.get_ingested_csv_train_test_val_path()
            self.convert_raw_data_as_ingested_train_test_val_csv(local_train_csv_data_dir, local_test_csv_data_dir, local_val_csv_data_dir, local_train_raw_data_dir, local_test_raw_data_dir, local_val_raw_data_dir)
            
        except Exception as e:
            raise CustomException(e,sys) from e
    
    def __del__(self):
        logging.info(f"{'=' * 20} Data Ingestion Log Completed. {'=' * 20} \n\n")
    
    