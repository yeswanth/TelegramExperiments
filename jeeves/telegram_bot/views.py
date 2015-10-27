from django.shortcuts import render
import telegram
from django.http import HttpResponse,Http404

def webhook():
    update = telegram.update.Update.de_json(request.get_json(force=True))
    bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')
    return HttpResponse("Thank You.")
