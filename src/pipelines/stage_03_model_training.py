import os
import sys
sys.path.insert(0, 'D:\Kidney_tumor_detection\src')
from logger import *
from exception import *
from config.configuration import *
from components.model_training import *

STAGE_NAME='TRAINING'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager(CONFIG_FILE_PATH,PARAM_FILE_PATH)
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            logging.info('error occured during training')
            raise CustomException(e,sys)
        
if __name__=='__main__':
    try:

        obj=ModelTrainingPipeline()
        logging.info(f'{STAGE_NAME} HAS STARTED')
        obj.main()
        logging.info(f'{STAGE_NAME} DONE')
    except Exception as e:
        logging.info("error has occured in training pipeline")
        raise CustomException(e,sys)