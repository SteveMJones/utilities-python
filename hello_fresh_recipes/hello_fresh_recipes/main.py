#!/usr/bin/env python
import requests

from bs4 import BeautifulSoup

from database.session import Session
from database.model import Recipe, Asset
from database.util import init as database_init


class Downloader(object):
    def download(self):
        print('Updating recipe cache...')
        req = requests.get('https://www.hellofresh.com/archive/recipes/',
                           params={'count': '100000'})
        print(req.content)


# Main
def main():
    database_init()
    downloader = Downloader()
    # downloader.download()

    session = Session()

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

    session.add(recipe)
    session.commit()


if __name__ == '__main__':
    main()
