import telegram
from django.core.urlresolvers import reverse
from django.conf import settings 

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
