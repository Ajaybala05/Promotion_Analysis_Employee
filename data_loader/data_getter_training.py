import pandas as pd
import json


class Data_Getter_Training:


    def __init__(self, file_object, logger_object):
        self.training_file = 'data/train.csv'
        self.file_object = file_object
        self.logger_object = logger_object

    def get_data(self):

        self.logger_object.log(self.file_object, 'Entered the get_data method of the Data_Getter_training class')
        try:
            self.data = pd.read_csv(self.training_file, encoding='unicode_escape')  # reading the data file
            self.logger_object.log(self.file_object,
                                   'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_data method of the Data_Getter class. Exception message: ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()
file_object = open("../data_logs/data_load_logs.txt", 'a+')
from application_logging import App_Logger
log_writer = App_Logger()
data=Data_Getter_Training(file_object,log_writer)

