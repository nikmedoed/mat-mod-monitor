from selenium import webdriver
from time import sleep


def getData(browser, link, fsid=""):
    browser.get(link)
    try:
        push = browser.find_element_by_xpath('//*[@id="Pagination"]/a[2]')
        if push.text == "1":
            push.click()
            print("clicked")
    except:
        pass
    sleep(3)
    new = []
    firstid = browser.find_element_by_xpath('//*[@id="Searchresult"]/table/tbody/tr[2]/td[1]').text
    # print(firstid)
    pagenum = 1
    tfirst = 0
    bre = False

    try:
        while 1:
            elem = browser.find_elements_by_xpath('//*[@id="Searchresult"]/table/tbody/tr')
            del (elem[0])
            for el in elem:
                e = el.find_elements_by_tag_name('td')
                resus = list(map(lambda a: a.text, e))
                re = list(map(lambda a: resus[a], [0, 1, 2, 7]))
                if fsid == re[0] or tfirst == re[0]:
                    bre = True
                    break
                new.append(re)
            # next = browser.find_element_by_class_name("next")
            print("Cтраница\t", pagenum, "\tнайдено элементов", len(elem))
            tfirst = browser.find_element_by_xpath('//*[@id="Searchresult"]/table/tbody/tr[2]/td[1]').text
            if bre:
                break
            browser.find_element_by_class_name("next").click()
            sleep(1)
            pagenum += 1
    except:
        print("Exception", pagenum)

    names = set(map(lambda m: m[1], new))
    return [firstid, names, new]


def autorize(br, log, pas):
    try:
        br.get('https://informatics.msk.ru/login/index.php')
        br.find_element_by_xpath('//*[@id="username"]').send_keys(log)
        br.find_element_by_xpath('//*[@id="password"]').send_keys(pas)
        br.find_element_by_xpath('//*[@id="login"]/div/div[5]/input[2]').click()
        return True
    except:
        print('Нет получилось авторизироваться, произошла ошибка')
        return False


if __name__ == "__main__":
    link = 'https://informatics.msk.ru/moodle/submits/view.php?group_id=10328'
    browser = webdriver.Chrome()
    fsid = 0
    log, pas = 'nikmedoed', '21122012'

    autorize(browser, log, pas)

    fsid, names, data = getData(browser, link, fsid)
    print(names)
    print(data)
