import sys
sys.path.insert(0, 'D:\Kidney_tumor_detection\src')
from utils import *
from constants import *
from entity.config_entity import *


class ConfigurationManager:
    def __init__(self,config_path=CONFIG_FILE_PATH,params_path=PARAM_FILE_PATH):
        self.config=read_yaml(config_path)
        self.params=read_yaml(params_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(config.root_dir,config.source_url,config.local_data_file,config.unzip_dir)
        return data_ingestion_config