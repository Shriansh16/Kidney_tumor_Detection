import sys
sys.path.insert(0, 'D:\Kidney_tumor_detection\src')
from logger import logging
from exception import CustomException
from src.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from src.pipelines.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.pipelines.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME='DATA INGESTION STAGE'
STAGE_NAME2='PREPARE BASE MODEL STAGE'
STAGE_NAME3='TRAINING'
try:
        logging.info(f'{STAGE_NAME} HAS STARTED')
        obj=DataIngestionPipeline()
        obj.main()
        logging.info(f'{STAGE_NAME} HAS COMPLETED')

except Exception as e:
        logging.info('ERROR OCCURED IN DATA INGESTION PIPELINE')
        raise CustomException(e,sys)


try:
        obj2=PrepareBaseModelPipeline()
        logging.info(f'{STAGE_NAME2} HAS STARTED')
        obj2.main()
        logging.info(f'{STAGE_NAME2} HAS completed')
except Exception as e:
        logging.info("error occured in prepare base model pipeline")
        raise CustomException(e,sys)


try:

        obj=ModelTrainingPipeline()
        logging.info(f'{STAGE_NAME} HAS STARTED')
        obj.main()
        logging.info(f'{STAGE_NAME} DONE')
except Exception as e:
        logging.info("error has occured in training pipeline")
        raise CustomException(e,sys)