# JSON-and-XML-Django-server-converter

## Описание

JSON-and-XML-Django-server-converter - это веб-приложение, разработанное на фреймворке Django, предназначенное для конвертации данных между форматами JSON и XML и их валидации. Приложение позволяет пользователям передавать файлы в одном из форматов и преобразовывать их в другой формат.

## Установка и настройка

### Требования

Для работы приложения необходимо иметь установленное:

- Python 3.6 или выше
- Django 3.2 или выше

### Установка (пример на Windows)

1. Клонируйте репозиторий на свой компьютер:
```bash
git clone https://github.com/LilChicha174/JSON-and-XML-Django-server-converter.git
```

2. Перейдите в каталог проекта:
```bash
cd JSON-and-XML-Django-server-converter/DjangoLetiTest
```

3. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

Приложение теперь доступно по адресу `http://127.0.0.1:8000/`.

### Использование

Для конвертации `JSON->XML`: 

Необходимо сделать JSON-запрос на адрес `http://127.0.0.1:8000/converter/json-to-xml/`. 

Для конвертации `XML->JSON`:

Необходимо сделать XML-запрос на адрес `http://127.0.0.1:8000/converter/xml-to-json/`. 

Примеры XML и JSON запросов находятся в директории `/converter/schemas/` в файлах `App_info.xml` и `App_info.json` соответственно.
В этой же директории находятся данные в условии XSD-схемы для валидации запросов `Add_Entrant_List.xml` и `Get_Entrant_List.xsd`. При несоответствии XML-данных XSD-схеме, сервер отправляет ответ, указывающий на то, какие данные и почему не соответствуют схеме. 

## Ход разработки

В процессе разработки были внесены следующие изменения в исходный JSON-запрос:

1. Из-за отсутствия обязательных ключей `isregistration`, `idregion`, и `city` в исходном JSON-запросе, они были добавлены.
2. Форматы значений-дат у ключей `passport_begda` и `diploma_date` были изменены из-за несоответствия их формата xsd-схеме.

## Разработчики

- LilChicha174 - автор проекта и основной разработчик
