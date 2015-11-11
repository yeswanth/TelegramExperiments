import telegram
from django.core.urlresolvers import reverse
from django.conf import settings 
import random

class Bot(object):
    def __init__(self):
        self.bot = telegram.Bot(settings.TELEGRAM_KEY)
  
    def send_message(self,chat_id,message):
        print "Sending Message"
        self.bot.sendMessage(chat_id=chat_id,
                            text=message)

    def configure_webhook(self):
        webhook_url = settings.APPLICATION_URL+reverse('telegram_bot:webhook',args=(settings.TELEGRAM_KEY,)) 
        print webhook_url
        self.bot.setWebhook(webhook_url,open(settings.SSL_CERTIFICATE_LOCATION,'rb'))

    def process(self,chat_id,text):
        if text == "/goodmorning":
            print "Matched"
            print chat_id
            self.send_message(chat_id, get_random_good_morning())
        elif text == '/goodmorning@GooodMorningBot':
            print "Matched"
            self.send_message(chat_id, get_random_good_morning())

def get_random_good_morning():
    messages = open(settings.GOOD_MORNING_FILE).read().split('\n\n')
    index = random.randint(0,len(messages)-1)
    return messages[index]
