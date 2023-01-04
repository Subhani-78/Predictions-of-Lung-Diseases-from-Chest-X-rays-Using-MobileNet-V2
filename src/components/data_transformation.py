
from src.constant import *
from src.config.configuration import Configuration
from src.entity.config_entity import *
from src.logger import logging
from src.utils.utils import *
from src.exception import CustomException
from src.entity.artifact_entity import *

import tensorflow as tf
import efficientnet.keras as efn
from tensorflow.keras.callbacks import Callback
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.metrics import Recall, Precision
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class DataTransformation:
    
    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifcat: DataIngestionArtifact):
        try:
            logging.info(f"{'>>' * 30}Data Transformation Started{'<<' * 30}")
            
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifcat
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def get_data_generator_flow(self):
        
        """
        It returns kwargs of data generator and data flow.
        
            Parameters: None

            Returns: 
                datagen_kwargs (generator), dataflow_kwargs (generator)
        """
        
        try:
            
            datagen_kwargs = dict(rescale = IMAGE_RESCALE)
            dataflow_kwargs = dict(target_size=(IMAGE_SIZE, IMAGE_SIZE), 
                        batch_size = BATCH_SIZE, 
                        interpolation = INTERPOLATION, 
                        class_mode = CLASS_MODE)
            
            return datagen_kwargs, dataflow_kwargs
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def get_train_data_generator(self, datagen_kwargs, dataflow_kwargs):
        
        """
        It returns train data generator and store genrated data in 
        transformed_train_data directory.
        
            Parameters: 
                datagen_kwargs (generator), dataflow_kwargs (generator)

            Returns: 
                train_datagen (Generator containing transformed training images for modeling)
        """
        
        try:
            
            # Path to label directory in transformed_train_data_dir
            label_zero_train_data_dir = os.path.join(
                self.data_transformation_config.transformed_train_data_dir,
                LABELS[0])
            
            label_one_train_data_dir = os.path.join(
                self.data_transformation_config.transformed_train_data_dir,
                LABELS[1])
            
            # Creating label directory in transformed_train_data_dir
            os.makedirs(label_zero_train_data_dir, exist_ok=True)
            os.makedirs(label_one_train_data_dir, exist_ok=True)
            
            for label in LABELS:
                
                train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=5,
                    horizontal_flip=True,
                    width_shift_range=0.1, 
                    height_shift_range=0.1,
                    shear_range=0.1, 
                    zoom_range=0.1,
                    **datagen_kwargs)
                
                train_generator = train_datagen.flow_from_directory(
                    directory = self.data_ingestion_artifact.raw_data_train_file_path, 
                    subset="training", 
                    shuffle=True, 
                    save_to_dir = self.data_transformation_config.transformed_train_data_dir +'/'+ label, 
                    save_prefix='aug', 
                    classes=[label],
                    **dataflow_kwargs)
                
                batch = next(train_generator)
                
            return train_datagen
                
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def get_test_data_generator(self, datagen_kwargs, dataflow_kwargs):
        
        """
        It returns test data generator and store genrated data in 
        transformed_test_data directory.
        
            Parameters: 
                datagen_kwargs (generator), dataflow_kwargs (generator)

            Returns: 
                test_datagen (Generator containing transformed testing images for modeling)
        """
        
        try:
            
            # Path to label directory in transformed_train_data_dir
            label_zero_test_data_dir = os.path.join(
                self.data_transformation_config.transformed_test_data_dir,
                LABELS[0])
            
            label_one_test_data_dir = os.path.join(
                self.data_transformation_config.transformed_test_data_dir,
                LABELS[1])
            
            # Creating label directory in transformed_train_data_dir
            os.makedirs(label_zero_test_data_dir, exist_ok=True)
            os.makedirs(label_one_test_data_dir, exist_ok=True)
            
            for label in LABELS:
                
                test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=5,
                    horizontal_flip=True,
                    width_shift_range=0.1, 
                    height_shift_range=0.1,
                    shear_range=0.1, 
                    zoom_range=0.1,
                    **datagen_kwargs)
                
                test_generator = test_datagen.flow_from_directory(
                    directory = self.data_ingestion_artifact.raw_data_test_file_path, 
                    subset="training", 
                    shuffle=True, 
                    save_to_dir = self.data_transformation_config.transformed_test_data_dir +'/'+ label, 
                    save_prefix='aug', 
                    classes=[label],
                    **dataflow_kwargs)
                
                batch = next(test_generator)
                
            return test_datagen
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def get_val_data_generator(self, datagen_kwargs, dataflow_kwargs):
        
        """
        It returns validation data generator and store genrated data in 
        transformed_val_data directory.
        
            Parameters: 
                datagen_kwargs (generator), dataflow_kwargs (generator)

            Returns: 
                test_datagen (Generator containing transformed validation images for modeling)
        """
        
        try:
            
            # Path to label directory in transformed_train_data_dir
            label_zero_val_data_dir = os.path.join(
                self.data_transformation_config.transformed_val_data_dir,
                LABELS[0])
            
            label_one_val_data_dir = os.path.join(
                self.data_transformation_config.transformed_val_data_dir,
                LABELS[1])
            
            # Creating label directory in transformed_train_data_dir
            os.makedirs(label_zero_val_data_dir, exist_ok=True)
            os.makedirs(label_one_val_data_dir, exist_ok=True)
            
            for label in LABELS:
                
                val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=5,
                    horizontal_flip=True,
                    width_shift_range=0.1, 
                    height_shift_range=0.1,
                    shear_range=0.1, 
                    zoom_range=0.1,
                    **datagen_kwargs)
                
                val_generator = val_datagen.flow_from_directory(
                    directory = self.data_ingestion_artifact.raw_data_val_file_path, 
                    subset="training", 
                    shuffle=True, 
                    save_to_dir = self.data_transformation_config.transformed_val_data_dir +'/'+ label, 
                    save_prefix='aug', 
                    classes=[label],
                    **dataflow_kwargs)
                
                batch = next(val_generator)
                
            return val_datagen
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        
        try:
            
            datagen_kwargs, dataflow_kwargs = self.get_data_generator_flow()
            transformed_train_data = self.get_train_data_generator(datagen_kwargs=datagen_kwargs, dataflow_kwargs=dataflow_kwargs)
            transformed_test_data = self.get_test_data_generator(datagen_kwargs=datagen_kwargs, dataflow_kwargs=dataflow_kwargs)
            transformed_val_data = self.get_val_data_generator(datagen_kwargs=datagen_kwargs, dataflow_kwargs=dataflow_kwargs)
            
            data_transformation_artifact = DataTransformationArtifact(
                
                transformed_train_data = transformed_train_data,
                transformed_test_data = transformed_test_data,
                transformed_val_data = transformed_val_data,
                transformed_train_data_dir = self.data_transformation_config.transformed_train_data_dir,
                transformed_test_data_dir = self.data_transformation_config.transformed_test_data_dir,
                transformed_val_data_dir = self.data_transformation_config.transformed_val_data_dir,
                is_transformed = True,
                message = "Data Transformation is completed"
            )
            
            logging.info(f"Data Transformation Artifact : {data_transformation_artifact}")
            
            return data_transformation_artifact
            
            
        except Exception as e:
            raise CustomException(e, sys) from e
        
    
        
    

