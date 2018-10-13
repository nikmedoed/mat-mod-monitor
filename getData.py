from selenium import webdriver
from time import sleep

def getDataS(browser, i = 0):
    return  [{'Анна Межуева', 'Анна Сапегина', 'Надежда Никишаева', '11 11', 'Екатерина Кочеткова', 'Анна Артамонова'},
             [['Надежда Никишаева', '2088-432898', '2938. Дележ яблок - 1', 'OK', '100'],
              ['Надежда Никишаева', '2088-432896', '2937. Следующее и предыдущее', 'Частичное решение', '0'],
              ['Надежда Никишаева', '2088-432893', '2937. Следующее и предыдущее', 'Частичное решение', '0'],
              ['Надежда Никишаева', '2088-432890', '2937. Следующее и предыдущее', 'Частичное решение', '0'],
              ['Надежда Никишаева', '2088-432889', '2937. Следующее и предыдущее', 'Ошибка компиляции', ''],
              ['Анна Межуева', '2088-432888', '2938. Дележ яблок - 1', 'OK', '100'],
              ['Надежда Никишаева', '2088-432887', '2937. Следующее и предыдущее', 'Частичное решение', '0'],
              ['Анна Межуева', '2088-432883', '2937. Следующее и предыдущее', 'Частичное решение', '0'],
              ['Анна Межуева', '2088-432882', '2937. Следующее и предыдущее', 'Ошибка компиляции', ''],
              ['Екатерина Кочеткова', '2116-127020', '3064. Длина последовательности', 'OK', '100'],
              ['Екатерина Кочеткова', '2088-432388', '2938. Дележ яблок - 1', 'OK', '100'],
              ['Екатерина Кочеткова', '2088-432387', '2937. Следующее и предыдущее', 'OK', '100'],
              ['Екатерина Кочеткова', '154-27143', '74. a + b = c', 'OK', '100'],
              ['Анна Артамонова', '2088-427632', '2936. Гипотенуза', 'Зачтено/Принято', '100'],
              ['Надежда Никишаева', '2088-427629', '2936. Гипотенуза', 'Зачтено/Принято', '100'],
              ['Екатерина Кочеткова', '2088-427616', '2936. Гипотенуза', 'Зачтено/Принято', '100'],
              ['11 11', '2088-427613', '2936. Гипотенуза', 'Частичное решение', '0'],
              ['Екатерина Кочеткова', '2088-427604', '2936. Гипотенуза', 'Частичное решение', '0'],
              ['Анна Сапегина', '2088-427599', '2936. Гипотенуза', 'Зачтено/Принято', '100'],
              ['Анна Межуева', '2088-427598', '2936. Гипотенуза', 'Зачтено/Принято', '100'],
              ['Екатерина Кочеткова', '2088-427595', '2936. Гипотенуза', 'Частичное решение', '0']]] \
        if i == 0 else getData(browser, i)

def getData(browser, sch = 5, pagenum = "1"):
    pagenum = str(pagenum)
    if sch == 5:
        last ='2088-427591'
    else:
        with  open("laspos.txt","r") as f:
            last = f.read()
            f.close()
    print("Текущий последний:", last, "sch", sch)
    link = "http://informatics.mccme.ru/moodle/submits/view.php?group_id=8137#" + pagenum
    # browser = webdriver.Chrome()
    browser.get(link)
    # browser.getCurrentUrl()
    # browser.
    try:
        push = browser.find_element_by_xpath('//*[@id="Pagination"]/a[2]')
        if push.text == "1":
            push.click()
            print("clicked")
    except:
        pass
    sleep(3)

    # names = set()
    new = []

    while 1:
        try:
            elem = browser.find_elements_by_xpath('//*[@id="Searchresult"]/table/tbody/tr')
            del(elem[0])
            print("Cтраница\t", pagenum, "\tнайдено элементов", len(elem))
            for el in elem:
                e = el.find_elements_by_tag_name('td')
                resus = list(map(lambda a: a.text, e))
                re = list(map(lambda a: resus[a], [1,0,2,5,7]))
                if last == re[1]:
                    break
                # name = e[1].text
                # task = e[2].text.split(".")[0]
                # state = e[5].text
                # score = e[7].text #round(int(e[7].text)/100,2)
                # names.add(re[0])
                # print(re)
                new.append(re)
            if last == re[1]:
                break
            browser.find_element_by_class_name("next").click()
            sleep(3)
            pagenum = int(pagenum)+1 # browser.find_element_by_class_name("current").text
        except:
            print ("Exception", pagenum)
            sleep(2)

    # browser.close()
    if len(new)>0:
        with open("laspos.txt", "w") as f: #'2088-427591'
            f.write(new[0][1])
            print("Первый элемент", new[0][1], "\n")
            f.close()
        names = set(map(lambda m:m[0],new))
    # print(names)
        return [names, new]
    else:
        return [[],[]]

if __name__ == "__main__":
    print(getData(16))

