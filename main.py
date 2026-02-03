import sys
from src.logger import logging as logger
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion


def main():
    try:
        logger.info("Application started")

        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()

        logger.info(f"Data ingestion completed")
        logger.info(f"Train data path: {train_path}")
        logger.info(f"Test data path: {test_path}")

    except Exception as e:
        logger.error("Error occurred in main execution")
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
