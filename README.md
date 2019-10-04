<h2 align="center">
	<img src="readme/examples/murr-logo.png" title="Murrengan" />
</h2>

**Выберите язык:**&nbsp; [<img src="readme/examples/en.png" title="Английский" />](readme/en) &nbsp; [<img src="readme/examples/pl.png" title="Польский" />](readme/pl)


[Сайт](http://murrengan.ru/murrs/)


<h2>
Социальная сеть, где люди помогают друг другу в достижении поставленных целей.
</h2>

<h3>
Мы есть тут:
</h3>


[Telegram чат всей тусовки.](https://t.me/MurrenganChat) 


[Youtube канал со стримами и видосами.](https://www.youtube.com/murrengan)


[Trello - список задач.](https://trello.com/b/yfjytAFU/murrengan) 


Основой проекта является язык программирования python и javaScript // фреймворки django и vue.js //


<h2>Установка:</h2>
<pre>
Делаешь форк и ставишь звездочку.
Дальше все просто:
    
    создать дирректорию mkdir murr_venv
    
    войти в дирректорию cd murr_venv
    
    скачать murr с github git clone ссылка_сгенерированная_в_твоем_репо
    
    открыть murr в PyCharm
    
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
