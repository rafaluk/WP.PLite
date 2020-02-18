from bs4 import BeautifulSoup
import requests

# import regex
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


class Downloader():
    def __init__(self):
        self._content = None
        self._source = None


    #todo: zrobic z tego get_content i z arguemntem source
    def get_wp(self):
        raw_site = requests.get("http://www.wp.pl").text.encode("utf-8")
        parsed_site = BeautifulSoup(raw_site, features="html.parser")
        self._source = 'wp'
        self._content = parsed_site
        return self._content

    def get_news(self):
        """
        :return: a dictionary of TITLE:LINK
        """

        if self._content is None:
            raise AssertionError("Content is empty! Get content first using get_wp or get_onet method.")
        #todo: if source is none

        links_glowny, links_high, links_low = {}, {}, {}

        if self._source == 'wp':
            content = self._content


            # take pierwszy news, take z niego class
            # wyszukaj a_areas z tymi class
            glonews_class = 'lclzf3-0'
            glonews_glowny_areas = content.find_all("a", {'data-st-area': 'Glonews-glowny'})

            # todo: delete multiredundancy!!!
            #todo: change data fromat to list of tuples: [(title, link)]
            for a_area in glonews_glowny_areas:
                title = a_area.find_all('div', {'class': glonews_class})[0].get_text()
                if len(title) > 100:
                    continue
                link = a_area['href']
                links_glowny[title] = link

            glonews_high_areas = content.find_all("a", {'data-st-area': 'Glonews-high'})

            for a_area in glonews_high_areas:
                title = a_area.find_all('div', {'class': glonews_class})[0].get_text()
                if len(title) > 100:
                    continue
                link = a_area['href']
                links_high[title] = link

            glonews_low_areas = content.find_all("a", {'data-st-area': 'Glonews-low'})

            for a_area in glonews_low_areas:
                title = a_area.find_all('div', {'class': glonews_class})[0].get_text()
                if len(title) > 100:
                    continue
                link = a_area['href']
                links_low[title] = link

        return links_glowny, links_high, links_low