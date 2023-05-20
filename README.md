# sendmail_to_telegram

Send system mail to telegram


## Как установить

1. Скачать `git clone https://github.com/theurs/sendmail_to_telegram.git`
2. `cd sendmail_to_telegram`
3. Сделать симлинк (возможно перед этим придется удалить уже имеющийся sendfile) `sudo ls -s sendmail.py /usr/bin/sendmail`
4. `sudo chmod +x pip install pyTelegramBotAPI`
5. Установить зависимости `pip install pyTelegramBotAPI`
6. Отредактировать файл `sendmail.py` подставив там свой токен бота и id пользователя которому бот будет посылать сообщения
7. Проверить работу `echo "test" | sendmail`
