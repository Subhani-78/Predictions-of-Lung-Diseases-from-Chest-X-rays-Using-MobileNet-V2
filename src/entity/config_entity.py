from collections import namedtuple

DataIngestionConfig = namedtuple( "DataIngestionConfig",[
    
    "data_source_url",
    "local_zip_data_dir",
    "local_raw_data_dir",
    "local_ingested_csv_data_dir",
    "local_train_csv_data_dir",
    "local_test_csv_data_dir",
    "local_val_csv_data_dir"
])


TrainingPipelineConfig = namedtuple( "TrainingPipelineConfig",["artifact_dir"])

