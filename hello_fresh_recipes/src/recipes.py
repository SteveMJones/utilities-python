#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import configparser
import sys
import requests


from bs4 import BeautifulSoup

#################################-MAIN CLASSES-###########################################
class HelloFreshRecipeDownloader(object):
    def __init__(self, cfgFilePath):
        self.cfgFilePath = cfgFilePath
        self.configuration = configparser.ConfigParser()

        if not self.configuration.read(self.cfgFilePath):
            raise configparser.Error('{} file not found'.format(self.cfgFilePath))
        
        self.downloadFolderPath = self.configuration.get("DOWNLOAD_DATA", 'downloadFolderPath')

        if not os.path.exists(self.downloadFolderPath):
            message = "Download folder path: '{}' doesn't exist".format(self.downloadFolderPath)
            raise ValueError(message)
    
    def download(self):
        print('Updating recipe cache...')
        req = requests.get('https://www.hellofresh.com/archive/recipes/', params={'count': '100000'})
        print(req.content)

#Main
if __name__ == '__main__':
    cfgFilePath = os.path.join(os.getcwd(), "configFile.cfg")
    downloader = HelloFreshRecipeDownloader(cfgFilePath)
    downloader.download()