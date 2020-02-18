import requests
from bs4 import BeautifulSoup


class Extractor:
    def __init__(self, link):
        self._link = link
        raw_site = requests.get(self._link).text.encode('utf-8')
        self._parsed_site = BeautifulSoup(raw_site, features="html.parser")


class PortalAbcZdrowieExtractor(Extractor):
    def get_article(self):
        art = self._parsed_site.find_all('div', {'class': 'article__text'},
                                         recursive=True)[0]
        paragraphs = art.find_all('p')
        return [par.get_text() for par in paragraphs]

    #todo: zrobic ze zrodla link
    #todo: sformatowac, zeby bylo czytelnie

    def get_title(self):
        title = self._parsed_site.find_all('h1', 'article__h1',
                                           recursive=True)[0].get_text()
        return title