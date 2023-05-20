# sendmail_to_telegram

Утилита позволяет перенаправить почту для рута (от крона итп) в телеграм.

## Как установить

1. Скачать `git clone https://github.com/theurs/sendmail_to_telegram.git`
2. `cd sendmail_to_telegram`
3. Сделать симлинк (возможно перед этим придется удалить уже имеющийся sendmail) `sudo ln -s "$PWD/sendmail.py" "/usr/bin/sendmail"`
4. `sudo chmod +x /usr/bin/sendmail`
5. Установить зависимости `sudo pip install pyTelegramBotAPI --system`
6. Отредактировать файл `sendmail.py` подставив там свой токен бота и id пользователя которому бот будет посылать сообщения
7. Проверить работу `echo "test" | sendmail`
