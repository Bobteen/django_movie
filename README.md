### Описание проекта:
Сайт кино-библиотека.


### Инструменты разработки

**Стек:**
- Python >= 3.9
- Django == 3.2.4
- sqlite3

## Разработка


##### 1) Клонировать репозиторий

    git clone https://github.com/Bobteen/django_movie.git

##### 2) Создать виртуальное окружение

    cd django_movie
    
    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 4) Устанавливить зависимости:

    pip install -r req.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить сервер

    python manage.py runserver