from Housing.pipeline.pipeline import Pipeline
from Housing.exception import HousingException
from Housing.logger import logging
from Housing.config.configuration import Configuration

def main():
    
    try:
        # pipeline = Pipeline()
        # pipeline.run_pipeline()
        data_validation_config = Configuration().get_data_transformation_config()
        print(data_validation_config)

    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()