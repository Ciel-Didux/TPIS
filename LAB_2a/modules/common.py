import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform
    
def evenNumbers(toggle):
    return list(range(2 if toggle else 1, 100, 2))
    
def exceptionFunc(int):
    return 10 / int