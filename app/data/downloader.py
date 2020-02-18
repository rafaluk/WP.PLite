from bs4 import BeautifulSoup
import requests

# import regex
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


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
        """
        :return: a list dictionaries: TITLE:LINK
        """

        if self._content is None or self._source is None:
            raise AssertionError("Content is empty! Get the site first using get_wp method.")

        content = self._content

        if self._source == 'wp':
            # headers for different main news areas
            headers = ['Glonews-glowny', 'Glonews-high', 'Glonews-low']

            # this is a class for main news. it doesn't change over time.
            glonews_class = 'lclzf3-0'

            # TODO: this structure might not fit for other websites
            dicts = []

            for header in headers:

                glonews_areas = content.find_all("a", {'data-st-area': header})
                links = {}

                for a_area in glonews_areas:
                    title = a_area.find_all('div', {'class': glonews_class})[0].get_text()
                    if len(title) > 100:
                        continue
                    link = a_area['href']
                    links[title] = link
                dicts.append(links)

        return dicts

