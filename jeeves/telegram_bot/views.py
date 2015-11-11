from django.shortcuts import render
import telegram
import json
from django.http import HttpResponse,Http404
from telegram_bot.bot import Bot 
from django.views.decorators.csrf import csrf_exempt
import sys

@csrf_exempt
def webhook(request,token):
    if request.method == 'POST':
        body = request.body.replace('\n','')
        json_body = json.loads(body)
        update = telegram.update.Update.de_json(json_body)
        bot = Bot()
        print update.message.text
        bot.process(update.message.chat_id,update.message.text)
    return HttpResponse("Thank You.")
