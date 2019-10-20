<h2 align="center">
	<img src="readme/examples/murr-logo.png" title="Murrengan" />
</h2>

**Выберите язык:**&nbsp; [<img src="readme/examples/en.png" title="Английский" />](readme/en) &nbsp; [<img src="readme/examples/pl.png" title="Польский" />](readme/pl)


[Сайт](http://murrengan.ru/murrs/)


## Социальная сеть, где люди помогают друг другу в достижении поставленных целей.

### Мы есть тут:

- [Telegram чат всей тусовки.](https://t.me/MurrenganChat)
- [Youtube канал со стримами и видосами.](https://www.youtube.com/murrengan)
- [Trello - список задач.](https://trello.com/b/yfjytAFU/murrengan)


Основой проекта является язык программирования python и javaScript // фреймворки django и vue.js


## Установка

##### Делаешь форк и ставишь звездочку

##### Создаешь дирректорию 

```shell script
mkdir murr_venv
```

##### Входишь в дирректорию

```shell script
cd murr_venv
```

##### Скачиваешь проект с github

    git clone ссылка_сгенерированная_в_твоем_репо (зеленая кнопка)

##### Открываешь скачанный проект в PyCharm

##### Создаешь виртуальное окружение для python

    PyCharm -> Preferences -> Project: murr project interpreter ->
    cogwheel -> Add... -> New environment location *workspase/murr/murr_venv -> Create

##### Открываешь терминал PyCharm

Убедиться, что `(murr_venv)` отображается слева

Если на **Unix** - удалите из `requirements.txt` библиотеки **pywin** и **pipwin**

##### Устанавливаешь зависимости

```shell script
pip install -r requirements.txt
```

##### Включаешь настройки для разработчика

Переименовываешь файл `_local_settings.py` в `local_settings.py`

##### Создаешь миграции для базы данных

```shell script
python manage.py makemigrations murr_game murr_chat MurrCard Murren
python manage.py migrate
```

##### Создать суперпользователя/пользователя/группу

```shell script
python manage.py shell
```

```python
from murr.helpers import BaseHelper
murr = BaseHelper()
murr.create_superuser("admin", "admin@admin.ru", "admin")
murr.create_user("Greg", "Greg@Greg.ru", "Murrengan1")
murr.group_create("Murrengan1")
```

##### Запустить сервер

```shell script
python manage.py runserver
```

Если возникла проблема с сертификатом у рекапчи -> https://stackoverflow.com/a/53310545  

## Да пребудет с нами сила!

## Команда

[<img src="https://avatars3.githubusercontent.com/u/40840064?s=460&v=4" width="150" height="150" />](https://github.com/Murrengan)  | [<img src="https://avatars2.githubusercontent.com/u/29122136?s=460&v=4" width="150" height="150" />](https://github.com/selincodes) | [<img src="https://avatars3.githubusercontent.com/u/23295612?s=400&v=4" width="150" height="150" />](https://github.com/dipperside) | [<img src="https://avatars0.githubusercontent.com/u/33005044?s=400&v=4" width="150" height="150" />](https://github.com/das-dev) | [<img src="https://avatars1.githubusercontent.com/u/36997266?s=400&v=4" width="150" height="150" />](https://github.com/jKEeY)
---|---|---|---|---
**Murrengan** | **Sergiej Selin** | **dipperside** | **das-dev** | **jKEeY**

[<img src="https://avatars0.githubusercontent.com/u/19286422?s=400&v=4" width="150" height="150" />](https://github.com/asechnaya)  | [<img src="https://avatars0.githubusercontent.com/u/33540273?s=400&v=4" width="150" height="150" />](https://github.com/Kuzyashin)  | [<img src="https://avatars2.githubusercontent.com/u/36294725?s=400&v=4" width="150" height="150" />](https://github.com/alexvelfr)  | [<img src="https://avatars3.githubusercontent.com/u/40520443?s=400&v=4" width="150" height="150" />](https://github.com/ast3310)  |
|---|---|---|---|
**Asja** | **Alexey Kuzyashin** | **alexvelfr** | **Astemir Unarokov**

## Частые вопросы/FAQ

---

### Как официально попасть в проект?

Сделать пулл реквест, который будет смержен в основной проект и пообщаться с текущей командой (голос/переписка/встреча в реале)
