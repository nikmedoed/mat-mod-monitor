from ober import *
from time import sleep
from time import time
from datetime import datetime
from getData import getDataS
from selenium import webdriver

def getNames(service, spreadsheetId, rangeName = 'E1:X1'):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values')[0]
    # print(values)
    return values

def getTaskNum(service, spreadsheetId, rangeName = 'D3:D'):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = list(map(lambda x: x[0], result.get('values')))
    # print(values)
    return values

sch = 1
browser = webdriver.Chrome()
while 1:
    CREDENTIALS_FILE = 'geol-mod-17-key.json'  # имя файла с закрытым ключом

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                      'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    spreadsheetId = '1d5UjabePXB9QpW2oTY6QtUkjn7NDMgBMvQzpkW_ccZ0'

    tasklist = getTaskNum(service, spreadsheetId)
    na = getNames(service, spreadsheetId)

    names, data = getDataS(browser, sch)
    if sch == 5:#21:
        sch=0
    if len(data) > 0:
        if len(na) > len(names):
            names = na
        # data.sort(key = lambda x: x[0])
        names = list(names)
        names.sort()
        try:
            del(names[names.index('11 11')])
        except:
            pass
        matrix = []
        for i in range(len(tasklist)):
            matrix.append([""]* len(names))

        errors = open("errors.txt", "a")

        for d in data:
            try:
                i = tasklist.index(d[2].split(".")[0])
                j = names.index(d[0])
                now = round(int(d[4])/100.0, 2) if d[3] in ['OK', 'Зачтено/Принято', 'Частичное решение'] else 0
                # print(round(int(d[4])/100.0, 2) , now, d[3]  )
                matrix[i][j] = now if matrix[i][j] == "" else max(now, matrix[i][j])
                # print("обработан", d , i, j, now, d[3], d[4], d[3] in ['OK', 'Зачтено/Принято', 'Частичное решение'])
            except:
                print("пропущен", d)
                errors.write( '\t'.join(d)+"\n")
            pass
        errors.close()

        results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "E3:X",
                 "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
                 "values": matrix},

                {"range": "E1:X1",
                 "majorDimension": "ROWS",  # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
                 "values": [names]}
            ]
        }).execute()
        print("\nРезультаты записаны\n")
    else:
        print(datetime.now(), "Ничего не поменялось. Счётчик:", sch)

    sch += 1
    sleep(30)

browser.close()

