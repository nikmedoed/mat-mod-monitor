Это монитор для визаулизации результатов сдачи заданий вашей группы на сайте https://informatics.msk.ru/.

Для всех действий вам потребует аккаунт на сайте.

Результаты группы после создания её доступны по ссылке:
https://informatics.msk.ru/moodle/submits/view.php?group_id=#######

Чтобы найти такую ссылку, необходимо:
- Ссоздать новую группу в разделе "Мои группы" и набрать в неё участников.
- Перейти в раздел ["Мои группы"](https://informatics.msk.ru/groups/view.php).
- Выбрать посылки соответствующей группы.

Для запуска монитора необходимо сделать копию таблицы: 
https://docs.google.com/spreadsheets/d/1sQw7rBVq_8Q8cTOEwrs4xYcI1pDNOFkJ3hlzJf-iiYM/edit?usp=sharing
Потребуется заполнить лист с задачами и условиями зачёта.

Шаги для запуска монитора после скачивания:
1) pip install -r requirements.txt
2) Создать сервис аккаунт для  Google API
- Зайти в [Google Developers Console](https://console.developers.google.com/iam-admin/projects) и создать новый проект (либо использовать какой-то их тех, что уже есть).
- Включить для этого проекта Drive API и Sheets API.
- Создать сервисный аакаунт и сохранить закрытый ключ от него в JSON в корне монитора
- Можно использовать сущесствующий аккаунт, для этого зайдите в проекте в раздел "Сервисные аккаунты" и создайте ключ, либо используйте уже существующий
- Дать доступ на редактирование таблицы вашему сервис аккаунту (у него почта вида ХХХ@ХХХ.iam.gserviceaccount.com)

3) Заполнить файл настроек (settings-example.json) и сохранить с названием "settings.json":
```
{
	"login": "",
	"password": "",
	"keyname": ".json",
	"link": "",
	"spreadshitID": "ваш id таблицы",
    "stop": "дата остановки"
}
```
4) Установить chromium подобный браузер (google chrome).
5) Запустить монитор с помощью python 3

Возможно потребуется обновить драйвера selemiun, искать тут:
- https://docs.seleniumhq.org/download/
- https://sites.google.com/a/chromium.org/chromedriver/downloads
- https://github.com/mozilla/geckodriver/releases
