<h1 align="center">Бот по финансовой грамотности</h1>


  [![leon'studio](https://img.shields.io/badge/made%20by-leon'%20studio-inactive)](https://kwork.ru/user/leonmaxwell)
  ![python](https://img.shields.io/badge/Language-Python-red)
  ![Django](https://img.shields.io/badge/Framework-Django-brightgreen)
  ![Bootstrap](https://img.shields.io/badge/Client%20framework-Bootstrap-blueviolet) 
  ![MySQL](https://img.shields.io/badge/Database-MySQL-yellow) 
  ![HTML](https://img.shields.io/badge/Markup-HTML-important)
  ![CSS](https://img.shields.io/badge/Stylesheets-CSS-9cf)
  
<h2 align="center">Разворачивание проекта</h2>

<p>Когда проект будет загружен на сервер требуется перейти в корневую папку проекта и выполнить следующие команды: </p>


* Устаналиваем виртуальное окружение
```
sudo apt install python3-venv
```
* Активируем виртуальное окружение
```
/usr/bin/python3 -m venv myvenv
source myvenv/bin/activate
```
* Устанавливаем бибилотеки которые требуются для запуска проекта
```
pip install -r requeriments.txt
```

* Делаем миграцию базы данных
```
python manage.py makemigrations
python manage.py migrate --run-syncdb
```
* Создаем суперпользователя
```
python manage.py createsuperuser
```
* Запускаем проект
```
python manage.py runserver
```

<h2 align="center">Работа с MySQL</h2>

<h3 align="center">Подключение базы MySQL</h2>

<p>Для подключение базы данных MySQL к проекту требуется выполнить несколько шагов</p>

* Для начала надо перейти в настройки проекта
```
cd skybotsPanel
nano settings.py
```
* При открытии документа требуется опустится вниз до метки
``` MySQL connector```

* После чего удаляем все ``` # ``` которые относятся к ``` db_confg ``` 
* Заполняем структуру авторизации в соответствующих полях
* Теперь надо активировать код для этого нужен файл ``` views.py ```
 ```
 cd skybots
 nano views.py
```
* После чего в этом документе удаляем все ``` # ```. Главное ненарушить структуру кода из за чего работать не будет.
* Перезапускаем проект
```
python manage.py runserver
```
<p> Теперь если сервер с БД доступен, открыты порты и есть доступ базе с разных хостов то будет работать.</p>

<h3 align="center">Работа с MySQL</h2>

<p>При работе с базой MySQL требуется знать:</p>
  * База должна быть изначчально пуста иначе при добавлении/изменении(особенно)/удалении данных с таблиц могут быть конфликты из за несоответствующих id.

* Работать с таблицами в базе которые относятся к сайту нельзя. Так как любое изменение в таблице могут вызывать конфликты при работы сайтас базой. Если и хотите работать с базой то работайте через сайт.

* Создавать новые таблицы не будут мешать работе, но новые таблицы не будут на сайте.
