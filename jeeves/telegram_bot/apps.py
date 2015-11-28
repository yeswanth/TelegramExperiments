from django.apps import AppConfig
import telegram
from django.conf import settings 
from django.core.urlresolvers import reverse
import os

class Bot(object):
    def __init__(self):
        self.bot = telegram.Bot(settings.TELEGRAM_KEY)
  
    def configure_webhook(self):
        webhook_url = settings.APPLICATION_URL+reverse('telegram_bot:webhook',args=(settings.TELEGRAM_KEY,)) 
        print webhook_url
        if os.path.exists(settings.SSL_CERTIFICATE_LOCATION):
            self.bot.setWebhook(webhook_url,open(settings.SSL_CERTIFICATE_LOCATION,'rb'))



class TelegramBotConfig(AppConfig):
    name = 'telegram_bot'
    verbose_name = 'Telegram Bot'
    def ready(self):         
        bot = Bot()
        bot.configure_webhook()
