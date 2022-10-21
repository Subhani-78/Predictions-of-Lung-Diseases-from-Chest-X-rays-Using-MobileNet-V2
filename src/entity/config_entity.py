from collections import namedtuple

DataIngestionConfig = namedtuple( "DataIngestionConfig",[
    
    "data_source_url",
    "local_zip_data_dir",
    "local_unzip_data_dir",
    "local_train_data_dir",
    "local_test_data_dir",
    "local_val_data_dir"

])

