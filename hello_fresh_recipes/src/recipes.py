#!/usr/bin/env python
from __future__ import (  # We require Python 2.6 or later
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os
import configparser
import sys
import requests

from bs4 import BeautifulSoup
from utils.db import db, Recipe, Asset

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
    #downloader.download()
    db = db()
    recipe = Recipe()
    recipe.uid = 'test'
    recipe.country = 'US'
    recipe.description = 'test description'
    recipe.name = 'test name'

    pdf = Asset()
    pdf.path = './downloads/pdfs'
    pdf.filename = 'recipe.pdf'
    pdf.size = 12345
    pdf.size_unit = 'kb'

    recipe.assets.append(pdf)

    db.add(recipe)