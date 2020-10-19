from app.getData import getData, autorize
from app.browser import getBrowser
from app.printer import getGservice, writeData
import json
from time import sleep
from datetime import datetime


if __name__ == "__main__":
    settings = json.loads(open("settings.json", "r").read())
    names = set()
    browser = getBrowser()
    if autorize(browser, settings['login'], settings['password'], settings['link']):
        service = getGservice(settings['keyname'])
        fsid = 0
        ssID = settings['spreadshitID']
        data = []
        sch = 0
        try:
            while datetime.now() < datetime.strptime(settings['stop'], '%d.%m.%Y'):
                fsid, name, dat = getData(browser, settings['link'], fsid)
                names.update(name)
                data.extend(dat)
                if len(dat) > 0:
                    writeData(ssID, service, names, data)
                else:
                    print(datetime.now(), "Ничего не поменялось. Счётчик: ", sch, 'ID:', fsid)
                sch += 1
                sleep(30)
        except:
            print('ошибка браузера')
    else:
        print('Неудачная авторизация')
    browser.close()