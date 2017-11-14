from ober import *

CREDENTIALS_FILE = 'geol-mod-17-key.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1d5UjabePXB9QpW2oTY6QtUkjn7NDMgBMvQzpkW_ccZ0'

results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "B2:C3",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": [["This is B2", "This is C2"], ["This is B3", "This is C3"]]},

        {"range": "D5:E6",
         "majorDimension": "COLUMNS",  # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
         "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
    ]
}).execute()

# rangeName = 'A2:E'
# result = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheetId, range=rangeName).execute()
# values = result.get('values', [])
#
# if not values:
#     print('No data found.')
# else:
#     print('Name, Major:')
#     for row in values:
#         # Print columns A and E, which correspond to indices 0 and 4.
#         print(row)

#
# spreadsheet = service.spreadsheets().create(body = {
#     'properties': {'title': 'Сие есть название документа', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Сие есть название листа',
#                                'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
# }).execute()
#
# driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
# shareRes = driveService.permissions().create(
#     fileId = spreadsheet['spreadsheetId'],
#     body = {'type': 'anyone', 'role': 'reader'},  # доступ на чтение кому угодно
#     fields = 'id'
# ).execute()

# p = spreadsheet
# print(p)