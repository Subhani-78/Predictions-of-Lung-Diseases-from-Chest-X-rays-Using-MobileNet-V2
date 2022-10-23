import yaml
from typing import Tuple
from src.exception import CustomException
from ensure import ensure_annotations
from src.constant import *
import sys,os
import csv

def read_yaml_file(file_path:str) -> dict:
    
    """
    Walks through a yml file and returns a dictionary.
    
    Args:
    file_path (str): path of yml file
    
    Returns: 
    1. A dictionary containing key:value in yml file.
    
    """
    
    try:
        with open(file=file_path,mode='rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise CustomException(e,sys) from e
    

def description_base_dir(dir_path:str)-> Tuple[str,list,list]:
    
    """
    Walks through the base dir and returns it's content -> tuple[str,list,list]
    
    Args:
    dir_path (str): target directory
    
    Returns:
    
    1. Count of label data directory (str)
    2. Names of label data directory (list)
    3. Paths of label data directory (list)
    
    """
    
    label_data_dir_names = os.listdir(dir_path)
    label_data_dir_count = len(label_data_dir_names)
    label_data_dir_paths:list = []
        
    for names in label_data_dir_names:
        label_data_dir_paths.append(os.path.join(dir_path,names))
        
    return label_data_dir_count, label_data_dir_names, label_data_dir_paths


def description_label_dirs(label_data_dir_paths:list)-> Tuple[list,list]:
    
    """
    Walks through the base dir and returns it's content -> tuple[list,list]
    
    Args:
    label_data_dir_paths (list): A list of paths of label data from the base directory 
    
    Returns:
    
    1. Paths of all Label images (list)
    2. Labels of all label images paths (list)
    
    """
    
    
    label_images_labels: list = [] 
    label_images_paths:list = []
    
    for paths in label_data_dir_paths:
        for label_data_dir_path, label_data_dir_names, label_images_name in os.walk(paths):
            label_name = os.path.basename(label_data_dir_path)
            
            for count in range(len(label_images_name)):
                label_images_labels.append(label_name)
                
            for names in label_images_name:
                label_images_paths.append(os.path.join(paths,names))
            
    return label_images_paths, label_images_labels

def convert_into_csv_format(label_images_paths:list,label_images_labels:list, store_dir:str) -> None:
    
    """
    Converts data into a csv file -> None
    
    Args:
    label_images_paths (list) : A list of label image paths
    label_images_labels (list) : A list of image labels
    base_dir (str) : Base Directory
    
    Returns: None
    
    """
    
    row_data:list = []
    basename = os.path.basename(store_dir) + '.csv'
    filepath = os.path.join(store_dir,basename)
    
    column_names = [LABEL_IMAGE_PATH,IMAGE_LABEL]
    
    for i in range(len(label_images_paths)):
        row:list = []
        row.append(label_images_paths[i])
        row.append(label_images_labels[i])
        row_data.append(row)
        
    # writing to csv file 
    with open(filepath, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(column_names) 
        csvwriter.writerows(row_data)
    