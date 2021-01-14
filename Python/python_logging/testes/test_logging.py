import pytest
import os
import logging


logging.basicConfig(filename='example.log', level=logging.DEBUG)
mylogger = logging.getLogger()

def setup_module(module):
    '''
        setup for the entire module
    '''
    mylogger.info('Inside Setup')
    
    # Do the actual setup stuff here
    pass


def setup_functions(func):
    '''
        Setup for test functions
    '''

    if func == test_one:
        mylogger.info('Hurray!!')


def test_save_log_file():
    '''
        Save logs inside files
    '''
    if isinstance(1, int):
        mylogger.debug('Hurray!!')
    


if __name__ == '__main__':
    mylogger.info(' About to start the tests ')
    pytest.main(args=['-s', os.path.abspath(__file__)])
    mylogger.info(' Done executing the tests ')