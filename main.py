import sys

from networksecurity.component.data_ingestion import DataIngestion
from networksecurity.component.data_validation import DataValidation


from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngetionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngetionConfig(trainingpipelineconfig)
        data_ingetion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        
        dataingestionartifact = data_ingetion.initiate_data_ingestion()
        logging.info('Data Initiation Completed')
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        
        data_validation_artifact = data_validation.initiate_data_validation()   
        logging.info('Data Validation Completed')
        print(data_validation_artifact)

        
        
        
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)
