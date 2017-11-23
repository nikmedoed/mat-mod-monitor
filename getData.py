from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests
from lxml import html

from selenium import webdriver
from time import sleep

def getData():

    last = '2088-427591'
    link = "http://informatics.mccme.ru/moodle/submits/view.php?group_id=8137#1"
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(3)

    names = set()
    new = []

    elem = browser.find_elements_by_xpath('//*[@id="Searchresult"]/table/tbody/tr')
    del(elem[0])
    start = elem[1].text.split()[0]
    print("Найдено элементов",len(elem))
    for el in elem:
        e= el.find_elements_by_tag_name('td')
        name = e[1].text
        tlast = e[0].text
        task = e[2].text.split(".")[0]
        score = round(int(e[7].text)/100,2)
        names.add(name)


        print(len(e))
    #     te = elem[1].text
    # print(elem[1].text)



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