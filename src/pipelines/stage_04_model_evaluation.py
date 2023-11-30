import os
import sys
sys.path.insert(0, 'D:\Kidney_tumor_detection\src')
from logger import *
from exception import *
from config.configuration import *
from components.model_evaluation_mlflow import *


stage_name="EVALUATION STAGE"

class EvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:

            config=ConfigurationManager(CONFIG_FILE_PATH,PARAM_FILE_PATH)
            eval_config=config.get_evaluation_config()
            evaluation1=Evaluation(eval_config)
            evaluation1.evaluation()
            evaluation1.save_score()
            evaluation1.log_into_mlflow()
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    try:
        logging.info(f"stage {stage_name} started ")
        obj = EvaluationPipeline()
        obj.main()
        logging.info(f"stage {stage_name} completed")
    except Exception as e:
        logging.info("error occured in runnig of the model evaluation pipeline")
        raise CustomException(e,sys)
    
