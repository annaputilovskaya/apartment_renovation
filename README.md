**Задача:**

Имеется таблица работников бригады вида:

![image](https://github.com/user-attachments/assets/67b0243a-3b26-4a51-9de3-58b2a6bbc2d7)

Написать микросервис, реализующий следующие методы:

get .../api/v1/team/<team_id>/WorkerList

get .../api/v1/worker/<worker_id>

---
**Технические требования:**

- Язык программирования:
  - Python 3.11
- Фреймворк:
  - Django Rest Framework 3.15.2
- ORM:
  - Django 5.1.4
- Хранение данных:
  - SQLite 

---
**Запуск проекта:**

- клонируйте проект
- создайте в директории src/ файл .env по образцу. (Файл .env.sample)
- установите зависимости
- примените миграции
- запустите проект

---
**Структура базы данных:**

Таблица Worker (Рабочий): 

- id,
- ФИО,
- Номер бригады,
- Заработная плата,
- Специализация.

---
**Функционал:**

![image](https://github.com/user-attachments/assets/3c9569e3-ded5-4b40-b9df-5a476b5d74c2)


get .../api/v1/team/<team_id>/WorkerList - Возвращает список работников в бригаде

get .../api/v1/worker/<worker_id> - Возвращает описание мастера

***Функционал покрыт тестами на 91%***