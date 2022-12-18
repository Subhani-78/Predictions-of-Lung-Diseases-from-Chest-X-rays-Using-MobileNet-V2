from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",[
    
    "raw_data_train_file_path",
    "raw_data_test_file_path",
    "raw_data_val_file_path",
    "ingested_data_csv_train_file_path",
    "ingested_data_csv_test_file_path",
    "ingested_data_csv_val_file_path",
    "is_ingested",
    "message"
])


DataValidationArtifact = namedtuple("DataValidationArtifact",[
    
    "schema_file_path",
    "data_validation_reports_file_path",
    "is_validated",
    "message"
])

DataTransformationArtifact = namedtuple('DataTransformationArtifact',[
    
    "transformed_train_data",
    "transformed_test_data",
    "transformed_val_data",
    "transformed_train_data_dir",
    "transformed_test_data_dir",
    "transformed_val_data_dir",
    "is_transformed",
    "message"
    
])