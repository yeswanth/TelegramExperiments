import telegram
from django.core.urlresolvers import reverse
from django.conf.settings import TELEGRAM_KEY,SSL_CERTIFICATE_LOCATION,APPLICATION_URL

class Bot(object):
    def __init__(self):
        self.bot = telegram.Bot(key)
  
    def send_message(self,chat_id,message):
        bot.sendMessage(chat_id=chat_id,
                            text=message)

    def configure_webhook(self):
        bot.setWebhook(APPLICATION_URL) 

