from selenium import webdriver
from time import sleep


def getData(browser, link, fsid=""):
    browser.get(link)
    try:
        push = browser.find_element_by_xpath('//*[@id="Pagination"]/ul/li[2]/a')
        if push.text == "1":
            push.click()
            print("clicked")
    except:
        pass
    sleep(3)
    new = []
    firstid = browser.find_element_by_xpath('//*[@id="Searchresult"]/table/tbody/tr[2]/td').text
    # print(firstid)
    pagenum = 1
    tfirst = 0
    bre = False

    while 1:
        try:
            elem = browser.find_elements_by_xpath('//*[@id="Searchresult"]/table/tbody/tr')
            del (elem[0])
            for el in elem[::2]:
                e = el.find_elements_by_tag_name('td')
                res = list(map(lambda a: e[a], [0, 1, 2, 7]))
                resus = list(map(lambda a: a.text, res))
                resus.append(
                    e[5].find_element_by_xpath('*//option[@selected="selected"]').text.strip().replace('\n', ''))
                if fsid == resus[0] or tfirst == resus[0]:
                    bre = True
                    break
                new.append(resus)
            # next = browser.find_element_by_class_name("next")
            print("Cтраница\t", pagenum, "\tнайдено элементов", len(elem))
            tfirst = browser.find_element_by_xpath('//*[@id="Searchresult"]/table/tbody/tr[2]/td[1]').text
            if bre:
                break
            browser.find_element_by_class_name("next").click()
            sleep(3)
            pagenum += 1
        except:
            print("Exception", pagenum)

    names = set(map(lambda m: m[1], new))
    return [firstid, names, new]


def autorize(br, log, pas, link):
    try:
        br.get(link) #'https://informatics.msk.ru/login/index.php'
        br.find_element_by_xpath('//ul[2]/li[3]/div/span/a').click()
        br.find_element_by_id('username').send_keys(log)
        br.find_element_by_id('password').send_keys(pas)
        br.find_element_by_id('loginbtn').click()
        return True
    except:
        print('Нет получилось авторизироваться, произошла ошибка')
        return False


if __name__ == "__main__":
    pass
