import os
import sys

from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataInjesionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')

class DataInjesion:
    def __init__(self) -> None:
        self.injesion_config = DataInjesionConfig()
    
    def initiate_data_injesion(self):
        logging.info('entered data injesion method or component')
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read dataset as dataframe')

            os.makedirs(os.path.dirname(self.injesion_config.train_data_path), exist_ok=True)
            df.to_csv(self.injesion_config.raw_data_path, index=False, header=True)
            logging.info('Train test split initiated')

            train_set,test_set = train_test_split(df, test_size=0.2, random_state=123)
            train_set.to_csv(self.injesion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.injesion_config.test_data_path, index=False, header=True)
            logging.info('injesion of the data is completed')
            return (
                self.injesion_config.train_data_path,
                self.injesion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
            pass

if __name__ == "__main__":
    obj = DataInjesion()
    obj.initiate_data_injesion()
