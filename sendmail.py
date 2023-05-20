#!/usr/bin/python3
#pip install pyTelegramBotAPI

import sys, platform, io, datetime
import telebot

token   = 'xxx'
id      = yyy


bot = telebot.TeleBot(token)


if __name__ == "__main__":

    header = '[' + platform.node() + '] ' + str(sys.argv)
    text = sys.stdin.read()

    now = datetime.datetime.now()
    date_time = now.strftime("%d-%m-%Y %H-%M-%S")

    bot.send_message(id, header, disable_notification=True)

    if len(text) > 4096:
        with io.BytesIO() as f:
            f.write(text.encode())
            f.seek(0)
            bot.send_document(id, f, disable_notification=True, caption = f'{date_time}.txt')
    else:
        bot.send_message(id, text, disable_notification=True)
