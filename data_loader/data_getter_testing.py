import pandas as pd
import json

class Data_Getter_Testing:

    def __init__(self,file_object,logger_object):
        self.testing_file="../data/test.csv"
        self.logger_object=logger_object
        self.file_object=file_object

    def get_data(self):
        self.logger_object.log(self.file_object,"Entered the get_data method of data_getter_testing")
        try:
            self.data=pd.read_csv(self.testing_file,encoding='unicode_escape')
            self.logger_object.log(self.file_object,"data loaded successfully,exited the get_data method")
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,"Exception occured in the get_data method,Exception:"+str(e))
            self.logger_object.log(self.file_object,"Data load unsuccessful ,Exited the get_data method")
            raise Exception()
file_object=open("../data_logs/data_load_logs.txt","a+")
from application_logging import App_Logger
log_writer=App_Logger()
data=Data_Getter_Testing(file_object,log_writer)
data=data.get_data()
print(data.head())
