from cnnClassifier import logger
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipieline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config= data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
    
except Exception as e:
    raise e


STAGE_NAME = "Prepare base model"
try:
        logger.info(f"********************")
        logger.info(f"stage {STAGE_NAME} started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
        logger.exception(e)
        raise e