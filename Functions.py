import configparser
import os
from os import path
import pymysql
import sys
import logging.config
from datetime import datetime
import time
import re


# ************************  File Logger Class **************************************************************************
class logFileHand(logging.FileHandler):
    def __init__(self, filename, mode):
        self.filename = datetime.now().strftime(filename + '%H_%M_%d_%m_%Y.log')
        logDir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Logs/')
        super(logFileHand, self).__init__(logDir + self.filename, mode)


def singleton(myClass):
    instances = {}

    def get_instance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]

    return get_instance()


@singleton
class Logger:
    def __init__(self):
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.conf')
        logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
        self.logr = logging.getLogger('LogAgent')


# **********************************************************************************************************************
def readConst(section, file):
    config = configparser.ConfigParser()
    filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Utilities/' + file + '.ini')
    variable = config.read(filePath)
    if variable:
        dictionary = {}
        try:
            options = config.options(section)
        except configparser.NoSectionError:
            Logger.logr.error("Section " + section + " does not exist in " + filePath)
        else:
            for option in options:
                dictionary[option] = config.get(section, option)
            return dictionary
    else:
        Logger.logr.info("File " + file + ".ini doesn't exist under provided path:" + filePath)


def clearLayout(layout):
    """ To clear widgets displayed upon last checked button """
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


def buildPrdDtl(selectedProd):
    product = ['']
    for i in selectedProd:
        if (re.match('^[A0-Z0]*$', i)) and filter(lambda x: not re.match(r'^\s*$', x), i):
            # if not len(product):
            if len(product) == 1:
                product.append(i)
            else:
                product[1] = product[1] + i
        else:
            if len(product) == 2 or i.replace('.', '', 1).isdigit():
                # ***************** Adding product default qty before price ********************************************
                if i.replace('.', '', 1).isdigit():
                    product.append('1')
                # ******************************************************************************************************
                product.append(i)
            elif len(product) == 3 and filter(lambda x: not re.match(r'^\s*$', x), i):
                product[2] = product[2] + "-" + i
    product = tuple(product)
    return product
