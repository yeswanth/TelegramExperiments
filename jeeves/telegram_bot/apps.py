from django.apps import AppConfig
from .bot import Bot

class TelegramBotConfig(AppConfig):
    name = 'telegram_bot'
    verbose_name = 'Telegram Bot'
    def ready(self):         
        bot = Bot()
        bot.configure_webhook()
