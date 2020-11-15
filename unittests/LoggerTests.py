#!/usr/bin/env python
"""
model tests
"""

import os, sys
import csv
import unittest
from ast import literal_eval
import pandas as pd
from datetime import date
sys.path.insert(1, os.path.join('..', os.getcwd()))

## import model specific functions and variables
from logger import update_train_log, update_predict_log



class LoggerTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        ensure log file is created
        """

        log_file = os.path.join("logs", "train-test.log")
        if os.path.exists(log_file):
            os.remove(log_file)
        
        ## YOUR CODE HERE
        ## Call the update_train_log() function from logger.py with arbitrary input values and test if the log file 
        ## exists in you file system using the assertTrue() base method from unittest.

        data_shape = (10,2)
        eval_test = {'rmse':0.9}
        runtime = "00:00:00"
        model_version = 1.0
        model_version_note = "training"
        
        update_train_log(data_shape,eval_test, runtime,
                         model_version, model_version_note ,test=True)
        
    def test_02_train(self):
        """
        ensure that content can be retrieved from log file
        """
        
        log_file = os.path.join("logs", "train-test.log")
        
        ## YOUR CODE HERE
        ## Log arbitrary values calling update_train_log from logger.py. Then load the data
        ## from this log file and assert that the loaded data is the same as the data you logged.

        data_shape = (10,2)
        eval_test = {'rmse':0.9}
        runtime = "00:00:00"
        model_version = 1.0
        model_version_note = "training"
        
        update_train_log(data_shape,eval_test, runtime,
                         model_version, model_version_note ,test=True)
                         
        df = pd.read_csv(log_file)
        data_shape_test = [literal_eval(i) for i in df['x_shape'].copy()][-1]
        self.assertEqual(data_shape,data_shape_test)
        
        

    def test_03_predict(self):
        """
        ensure log file is created
        """

        log_file = os.path.join("logs", "predict-test.log")
        if os.path.exists(log_file):
            os.remove(log_file)
        
        ## YOUR CODE HERE
        ## Call the update_predict_log() function from logger.py with arbitrary input values and test if the log file 
        ## exists in you file system using the assertTrue() base method from unittest.
        
        y_pred = [0]
        y_proba = [0.9,0.1]
        runtime = "00:00:00"
        model_version = 2.0
        query = ['uk', 30, 'aavail_basic', 2]

        update_predict_log(y_pred,y_proba,query,runtime,
                           model_version, test=True)
        
        self.assertTrue(os.path.exists(log_file))
    
    def test_04_predict(self):
        """
        ensure that content can be retrieved from log file
        """ 

        log_file = os.path.join("logs", "predict-test.log")

        ## YOUR CODE HERE
        ## Log arbitrary values calling update_predict_log from logger.py. Then load the data
        ## from this log file and assert that the loaded data is the same as the data you logged.
    
        y_pred = [0]
        y_proba = [0.9,0.1]
        runtime = "00:00:00"
        model_version = 2.0
        query = ['uk', 30, 'aavail_basic', 2]

        update_predict_log(y_pred,y_proba,query,runtime,
                           model_version, test=True)
        
        self.assertTrue(os.path.exists(log_file))
    
        df = pd.read_csv(log_file)
        logged_y_pred = [literal_eval(i) for i in df['y_pred'].copy()][-1]
        self.assertEqual(y_pred,logged_y_pred)

### Run the tests
if __name__ == '__main__':
    unittest.main()
      
