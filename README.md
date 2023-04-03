# JSON-and-XML-Django-server-converter
Django-сервер осуществляющий конвертацию данных, переданных в запросе, в необходимый xml-формат и наоборот
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T2A]{fontenc}
\usepackage[russian]{babel}
\usepackage{hyperref}

\title{JSON-and-XML-Django-server-converter}
\date{}
\begin{document}

\maketitle

\section*{Описание}

JSON-and-XML-Django-server-converter - это веб-приложение, разработанное на фреймворке Django, предназначенное для конвертации данных между форматами JSON и XML. Приложение позволяет пользователям загружать файлы в одном из форматов и преобразовывать их в другой формат, а затем скачивать результат.

\section*{Установка и настройка}

\subsection*{Требования}

Для работы приложения необходимо иметь установленное:

\begin{itemize}
\item Python 3.6 или выше
\item Django 3.2 или выше
\end{itemize}

\subsection*{Установка}

\begin{enumerate}
\item Клонируйте репозиторий на свой компьютер:

\begin{verbatim}
git clone https://github.com/LilChicha174/JSON-and-XML-Django-server-converter.git
\end{verbatim}

\item Перейдите в каталог проекта:

\begin{verbatim}
cd JSON-and-XML-Django-server-converter
\end{verbatim}

\item Создайте и активируйте виртуальное окружение:

\begin{verbatim}
python3 -m venv venv
source venv/bin/activate
\end{verbatim}

\item Установите зависимости:

\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}

\item Примените миграции:

\begin{verbatim}
python manage.py migrate
\end{verbatim}

\item Запустите сервер разработки:

\begin{verbatim}
python manage.py runserver
\end{verbatim}

\end{enumerate}

Приложение теперь доступно по адресу \url{http://127.0.0.1:8000/}.

\section*{Использование}

\begin{enumerate}
\item Откройте веб-приложение в браузере по адресу \url{http://127.0.0.1:8000/}.
\item Выберите файл в формате JSON или XML, который вы хотите конвертировать.
\item Нажмите кнопку "Загрузить файл" для загрузки файла на сервер.
\item Выберите формат, в который хотите преобразовать загруженный файл: JSON или XML.
\item Нажмите кнопку "Конвертировать" для начала процесса конвертации.
\item Скачайте преобразованный файл, нажав кнопку "Скачать".
\end{enumerate}

\section*{Разработчики}

\begin{itemize}
\item LilChicha174 - автор проекта и основной разработчик
\end{itemize}

\section*{Лицензия}

Этот проект лицензирован под MIT License - см. файл \texttt{LICENSE} для получения дополнительной информации.

\end{document}
