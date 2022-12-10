# bonus_card
Веб-приложение для управления базой данных бонусных карт.
Реализован генератор карт, изменение статуса карты.
Сделан поиск по картам.


## Технологии:
Python 3.7, 
Django 2.2.19, 
PostgreSQL

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/E-bean/bonus_card
```

```
cd bonus_card
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:
```
cd bonus_card
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
