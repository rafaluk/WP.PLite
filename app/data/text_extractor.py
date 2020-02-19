import requests
from bs4 import BeautifulSoup


class Extractor:
    def __init__(self, link):
        self._link = link
        raw_site = requests.get(self._link).text.encode('utf-8')
        self._parsed_site = BeautifulSoup(raw_site, features="html.parser")


class AbcZdrowieExtractor(Extractor):
    def get_article(self):
        art = self._parsed_site.find_all('div', {'class': 'article__text'},
                                         recursive=True)[0]
        paragraphs = art.find_all('p')
        return [par.get_text() for par in paragraphs]

    def get_title(self):
        return self._parsed_site.find_all('h1', 'article__h1',
                                          recursive=True)[0].get_text()


class ParentingExtractor(Extractor):
    def get_article(self):
        art = self._parsed_site.find_all('div', {'class': 'article__text'},
                                         recursive=True)[0]

        paragraphs = art.find_all(['h2', 'p'])
        return [par.get_text() for par in paragraphs]

    def get_title(self):
        return self._parsed_site.find_all('h1', 'article__h1',
                                          recursive=True)[0].get_text()


class WiadomosciExtractor(Extractor):
    def get_article(self):
        lead = self._parsed_site.find_all('div', {'class': 'article--lead'},
                                          recursive=True)[0].get_text()
        art = self._parsed_site.find_all('div', {'class': 'article--text'},
                                         recursive=True)
        par_blocks = []
        for div in art:
            paragraphs = div.find_all(['p', 'h2'])
            a = [par.get_text() for par in paragraphs]
            par_blocks.append(a)
        flat_list = [par for sublist in par_blocks for par in sublist]
        flat_list.insert(0, lead)
        return flat_list

    def get_title(self):
        return self._parsed_site.find_all('h1', 'article--title',
                                          recursive=True)[0].get_text()

# EXCLUDE SPORTOWE FAKTY
class TurystykaExtractor(Extractor):
    def get_article(self):
        lead = self._parsed_site.find_all('div', {'class': 'article--lead'},
                                          recursive=True)[0].get_text()

        art = self._parsed_site.find_all('div', {'class': 'article--text'},
                                         recursive=True)
        par_blocks = []
        for div in art:
            paragraphs = div.find_all(['p', 'h2'])
            a = [par.get_text() for par in paragraphs]
            par_blocks.append(a)
        flat_list = [par for sublist in par_blocks for par in sublist]
        flat_list.insert(0, lead)
        return flat_list


    def get_title(self):
        return self._parsed_site.find_all('h1', 'article--title',
                                          recursive=True)[0].get_text()


class KobietaExtractor(Extractor):
    def get_article(self):
        lead = self._parsed_site.find_all('div', {'class': 'article--lead'},
                                          recursive=True)[0].get_text()

        art = self._parsed_site.find_all('div', {'class': 'article--text'},
                                         recursive=True)
        par_blocks = []
        for div in art:
            paragraphs = div.find_all(['p', 'h2'])
            a = [par.get_text() for par in paragraphs]
            par_blocks.append(a)
        flat_list = [par for sublist in par_blocks for par in sublist]
        flat_list.insert(0, lead)
        return flat_list


    def get_title(self):
        return self._parsed_site.find_all('h1', 'article--title',
                                          recursive=True)[0].get_text()