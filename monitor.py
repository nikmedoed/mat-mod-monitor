from app.getData import getData, autorize, checkAuth
from app.browser import getBrowser
from app.printer import getGservice, writeData
import json
from time import sleep
from datetime import datetime
import traceback


if __name__ == "__main__":
    good = False
    while not good:
        try:
            good = True
            settings = json.loads(open("settings.json", "r").read())
            names = set()
            browser = getBrowser()
            service = getGservice(settings['keyname'])
            fsid = 0
            ssID = settings['spreadshitID']
            data = []
            sch = 0
            while datetime.now() < datetime.strptime(settings['stop'], '%d.%m.%Y'):
                if not checkAuth(browser):
                    if not autorize(browser, settings['login'], settings['password'], settings['link']):
                        print('Неудачная авторизация')
                else:
                    fsid, name, dat = getData(browser, settings['link'], fsid)
                    names.update(name)
                    data.extend(dat)
                    if len(dat) > 0:
                        writeData(ssID, service, names, data)
                    else:
                        print(datetime.now(), "Ничего не поменялось. Счётчик: ", sch, 'ID:', fsid)
                    sch += 1
                    sleep(30)
        except Exception as e:
            print('ошибка браузера:\n', traceback.format_exc())
            good = False
        try:
            browser.close()
        except Exception as e:
            print("Даже закрыться не смог")
    print("Вот и всё", datetime.now())

