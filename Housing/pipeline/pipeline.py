from Housing.config.configuration import Configuration
from Housing.exception import HousingException
from Housing.logger import logging
import os,sys
from Housing.entity.artifact_entity import DataIngestionArtifact
from Housing.entity.config_entity import DataIngestionConfig
from Housing.component.data_ingestion import DataIngestion



class Pipeline:

    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_module_evaluation(self):
        pass

    def start_module_pusher(self):
        pass
        
    def run_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e
