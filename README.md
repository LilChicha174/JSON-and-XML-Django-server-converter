# JSON-and-XML-Django-server-converter

## Описание

JSON-and-XML-Django-server-converter - это веб-приложение, разработанное на фреймворке Django, предназначенное для конвертации данных между форматами JSON и XML. Приложение позволяет пользователям загружать файлы в одном из форматов и преобразовывать их в другой формат, а затем скачивать результат.

## Установка и настройка

### Требования

Для работы приложения необходимо иметь установленное:

- Python 3.6 или выше
- Django 3.2 или выше

### Установка

1. Клонируйте репозиторий на свой компьютер:
git clone https://github.com/LilChicha174/JSON-and-XML-Django-server-converter.git

2. Перейдите в каталог проекта:
cd JSON-and-XML-Django-server-converter

3. Создайте и активируйте виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

4. Установите зависимости:
pip install -r requirements.txt

5. Запустите сервер разработки:
python manage.py runserver


Приложение теперь доступно по адресу `http://127.0.0.1:8000/`.

## Использование

1. Откройте веб-приложение в браузере по адресу `http://127.0.0.1:8000/`.

2. Выберите файл в формате JSON или XML, который вы хотите конвертировать.

3. Нажмите кнопку "Загрузить файл" для загрузки файла на сервер.

4. Выберите формат, в который хотите преобразовать загруженный файл: JSON или XML.

5. Нажмите кнопку "Конвертировать" для начала процесса конвертации.

6. Скачайте преобразованный файл, нажав кнопку "Скачать".

## Разработчики

- LilChicha174 - автор проекта и основной разработчик

## Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для получения дополнительной информации.







