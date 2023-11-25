import sys
sys.path.insert(0, 'D:\Kidney_tumor_detection\src')
from logger import logging
from exception import CustomException
from src.pipelines.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME='DATA INGESTION STAGE'
try:
        logging.info('{STAGE_NAME} HAS STARTED')
        obj=DataIngestionPipeline()
        obj.main()
        logging.info('{STAGE_NAME} HAS COMPLETED')

except Exception as e:
        logging.info('ERROR OCCURED IN DATA INGESTION PIPELINE')
        raise CustomException(e,sys)