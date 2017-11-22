from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests
from lxml import html

from selenium import webdriver


def getData():
    link = "http://informatics.mccme.ru/moodle/submits/view.php?group_id=8137#1"
    browser = webdriver.Chrome()
    browser.get(link)
    assert "Личные " in browser.title
    # elem = browser.find_element_by_name("tbody")
    # e = browser.
    browser.close()
    # requests.packages.urllib3.disable_warnings()
    # u = requests.api.request('post', link, data={'bar': 'baz'}, json=None, verify=False).text
    # print(u)
    # h = html.document_fromstring(u)
    # res = h.xpath('table/tbody')

    # res = h
    # page = urlopen(link)
    # soup = BeautifulSoup(page, 'html.parser')
    # print(soup)
    #
    # urls_tag = soup.findAll("tbody")
    # print(urls_tag)
    # res = urls_tag[0].string
    res = 0 #elem
    return res


if __name__ == "__main__":
    print(getData())