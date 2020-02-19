from bs4 import BeautifulSoup
import requests


class Downloader:
    def __init__(self):
        self._content = None
        self._source = None

    def get_wp(self):
        raw_site = requests.get("http://www.wp.pl").text.encode("utf-8")
        parsed_site = BeautifulSoup(raw_site, features="html.parser")
        self._source = 'wp'
        self._content = parsed_site
        return self._content

    def get_news(self):

        content = self._content

        dicts = []

        if self._source == 'wp':
            # headers for different main news areas
            headers = ['Glonews-glowny', 'Glonews-high', 'Glonews-low']

            # this is a class for main news. it doesn't change over time.
            glonews_class = 'lclzf3-0'

            for header in headers:
                glonews_areas = content.find_all("a", {'data-st-area': header})
                links = {}

                for a_area in glonews_areas:
                    title = a_area.find_all('div', {'class': glonews_class})[0].get_text()
                    # if title is too long, it probably contains some useless info
                    if len(title) > 100:
                        continue
                    link = a_area['href']
                    # exclude portals with videos or tons of useless content
                    exclusions = ['sportowefakty', 'moneyv.wp.pl',
                                  'wideo.wp.pl', 'o2.pl']
                    if any(elem in link for elem in exclusions):
                        continue
                    links[title] = link
                dicts.append(links)

        return dicts

