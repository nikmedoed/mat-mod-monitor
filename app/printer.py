import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def getGservice(file):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(file,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    return service


def getTaskNum(service, spreadsheetId, rangeName = 'D5:D'):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = list(map(lambda x: x[0], result.get('values')))
    # print(values)
    return values


def writeData(ssID, service, names, data):
    names = list(names)
    names.sort()
    tasklist = getTaskNum(service, ssID)
    matrix = []
    for i in range(len(tasklist)):
        matrix.append([""] * len(names))
    errors = open("errors.txt", "a")

    for d in data:
        try:
            i = tasklist.index(d[2].split(".")[0])
            j = names.index(d[1])
            if d[4].split('\n')[0] in ['OK', 'Зачтено/Принято']: d[3] = 100
            now = round(int(d[3]) / 100.0, 2) # if d[3] in ['OK', 'Зачтено/Принято', 'Частичное решение'] else 0
            matrix[i][j] = now if matrix[i][j] == "" else max(now, matrix[i][j])
        except:
            print("пропущен", d)
            errors.write('\t'.join(d) + "\n")
        pass
    errors.close()

    service.spreadsheets().values().batchUpdate(spreadsheetId=ssID, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "E5:W",
             "majorDimension": "ROWS",
             # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
             "values": matrix},

            {"range": "E1:W1",
             "majorDimension": "ROWS",
             # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
             "values": [names]}
        ]
    }).execute()
    print("\nРезультаты записаны", datetime.now(), '\n')

