import sys
sys.path.insert(0, 'D:\Kidney_tumor_detection\src')
from config.configuration import *
from components.data_ingestion import *
from logger import *
from exception import *


STAGE_NAME='DATA INGESTION STAGE'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config1=ConfigurationManager(CONFIG_FILE_PATH,PARAM_FILE_PATH)
        data_ingestion_config=config1.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_file()

if __name__=='__main__':
    try:
        logging.info('{STAGE_NAME} HAS STARTED')
        obj=DataIngestionPipeline()
        obj.main()
        logging.info('{STAGE_NAME} HAS COMPLETED')

    except Exception as e:
        logging.info('ERROR OCCURED IN DATA INGESTION PIPELINE')
        raise CustomException(e,sys)
