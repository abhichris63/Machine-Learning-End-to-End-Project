from Housing.pipeline.pipeline import Pipeline
from Housing.exception import HousingException
from Housing.logger import logging
from Housing.config.configuration import Configuration
from Housing.component.data_transformation import DataTransformation
import os

def main():
    
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        pipeline.run_pipeline()

        # ROOT_DIR = os.getcwd() # to get current working directory.
        # CONFIG_DIR = "config"
        # CONFIG_FILE_NAME = "config.yaml"
        # CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
        # print(os.path.basename(CONFIG_FILE_PATH))



        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)

        # schema_file_path = r"C:\Users\ABHI\Desktop\Acer-data\Ineuron.Ai\Machine-Learning\Machine-Learning-End-to-End-Project\Machine-Learning-End-to-End-Project\config\schema.yaml"

        # file_path = r"C:\Users\ABHI\Desktop\Acer-data\Ineuron.Ai\Machine-Learning\Machine-Learning-End-to-End-Project\Machine-Learning-End-to-End-Project\Housing\artifact\data_ingestion\2023-11-22-13-44-45\ingested_data\train\housing.csv"

        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)

        # print(df.columns)
        # print(df.dtypes)



    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()