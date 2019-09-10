<h2 align="center">
	<img src="readme/examples/murr-logo.png" title="Murrengan" />
</h2>

**Выберите язык:**&nbsp; [<img src="readme/examples/en.png" title="Английский" />](readme/en) &nbsp; [<img src="readme/examples/pl.png" title="Польский" />](readme/pl)

<pre>



</pre>


<h2>
Социальная сеть, где люди помогают друг другу в достижении поставленных целей.
</h2>

<h3>
Если у тебя есть вопросы или предложения:
</h3>


[Telegram чат всей тусовки.](https://t.me/MurrenganChat) 


[Youtube канал со стримами и видосами.](https://www.youtube.com/murrengan)


[Trello - список задач.](https://trello.com/b/yfjytAFU/murrengan) 

Проект разрабатывается на фреймворке Django 2. Официальная <a href="https://docs.djangoproject.com">документация</a> .

<h3 align="center">
Разработка осуществляется через ветку develop - будь внимателен!
</h3>




Рекомендации по настройке murr

Основой проекта является язык программирования python и javaScript // фреймворки django и vue.js //

Для работы с ментальной картой и сценарием используется приложение xmind zen https://www.xmind.net/zen/

<h2>Установка:</h2>
<pre>
    сделать форк и ставишь звездочку =)
    
    создать дирректорию mkdir murr_venv
    
    войти в дирректорию cd murr_venv
    
    скачать murr с github git clone ссылка_сгенерированная_в_твоем_репо
    
    откройте murr в PyCharm
    
    создать виртуальное окружение для python  PyCharm -> Preferences -> Progect: murr project interpreter -> 
    cogwheel -> Add... -> New environment location *workspase/murr/murr_venv -> Create
    
    открыть термина PyCharm // убедиться, что (murr_venv) отображается слева
    
    если вы на unix - удалите из requirements.txt pywin и pipwin
    
    установить зависимости pip install -r requirements.txt
    
    переименовать _local_settings.py в local_settings.py
    
    создать миграции для базы данных python manage.py makemigrations murr_game murr_chat MurrCard Murren
    
    мигрировать python manage.py migrate
    
    создать суперпользователя/пользователя/группу :  
        python manage.py shell 
        from murr.helpers import BaseHelper
        murr = BaseHelper()
        murr.create_superuser("admin", "1@2.ru", "admin")
        murr.create_user("Greg", "1@2.ru", "Murrengan1")
        murr.group_create("Murrengan1")
        
    запустить сервер python manage.py runserver
    
    если возникла проблема с сертификатом у рекапчи -> https://stackoverflow.com/a/53310545
   
</pre>



##### 0. 

##### 1. Скачиваешь себе на машину из своего репозитория:

`git clone ссылка_сгенерированная_в_твоем_репо`

##### 2. Переименовываешь `_local_settings.py` в `local_settings.py`

##### 3. Устанавливаешь зависимости:

`pip install -r requirements.txt`


##### 4. Применяешь миграции:

`python manage.py makemigrations murr_game murr_chat MurrCard Murren`

`python manage.py migrate`


##### 5. Запускаешь сервер:

`python manage.py runserver`


<h3 align="center">
После того как скачал к себе в гит проект и хочешь его синхронизировать с основной веткой, когда она изменилась:
</h3>

##### 1. добавляем удалённый репозиторий
`git remote add  название_бранча_на_локальной_машине https://github.com/Murrengan/murr`

##### 2. Смотрим появился ли он 
`git remote -v`

##### 3. Синхронизируем с основной веткой на своей машине
`git pull название_бранча_на_локальной_машине develop`

##### 4. Внесенные изменения добавляем в ветку в своем репозитории и пушим в свой удаленный репозиторий

`git add .`

`git commit -m "четкое_и_понятное_описание_проделанной_работы""`

`git push`

##### 5. Делаем пулл реквест в основной ветке Мурренгана в develop branch


<h2>
Да пребудет с нами сила!
</h2>

## Команда

[<img src="https://avatars3.githubusercontent.com/u/40840064?s=460&v=4" width="150" height="150" />](https://github.com/Murrengan)  | [<img src="https://avatars2.githubusercontent.com/u/29122136?s=460&v=4" width="150" height="150" />](https://github.com/selincodes) | [<img src="https://avatars3.githubusercontent.com/u/23295612?s=400&v=4" width="150" height="150" />](https://github.com/dipperside) | [<img src="https://avatars0.githubusercontent.com/u/33005044?s=400&v=4" width="150" height="150" />](https://github.com/das-dev) | [<img src="https://avatars1.githubusercontent.com/u/36997266?s=400&v=4" width="150" height="150" />](https://github.com/jKEeY)
---|---|---|---|---
**Murrengan** | **Sergiej Selin** | **dipperside** | **das-dev** | **jKEeY**



[<img src="https://avatars0.githubusercontent.com/u/19286422?s=400&v=4" width="150" height="150" />](https://github.com/asechnaya)  | [<img src="https://avatars0.githubusercontent.com/u/33540273?s=400&v=4" width="150" height="150" />](https://github.com/Kuzyashin)  | [<img src="https://avatars2.githubusercontent.com/u/36294725?s=400&v=4" width="150" height="150" />](https://github.com/alexvelfr)  | [<img src="https://avatars3.githubusercontent.com/u/40520443?s=400&v=4" width="150" height="150" />](https://github.com/ast3310)  |
|---|---|---|---|
**Asja** | **Alexey Kuzyashin** | **alexvelfr** | **Astemir Unarokov**

<h2>
Частые вопросы/FAQ
</h2>
<hr>
<h3>
Как официально попасть в проект?
</h3>
Сделать пулл реквест, который будет смержен в основной проект и пообщаться с текущей командой (голос/переписка/встреча в реале)
