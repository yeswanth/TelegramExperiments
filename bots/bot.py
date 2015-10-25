from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from production_settings import key,user_id
import random

OFFSET_FILE = "data.txt"
GOOD_MORNING_FILE = "goodmorning.txt"

"""
Setup the bot
"""

bot = TelegramBot(key)
bot.update_bot_info().wait()
#print(bot.username)

#print bot.set_webhook('http://45.55.196.234:8443/')


"""
Send a message to a user
"""

#result = bot.send_message(user_id, 'test message body').wait()
#print(result)
def get_random_good_morning():
    messages = open(GOOD_MORNING_FILE).read().split('\n\n')
    index = random.randint(0,len(messages)-1)
    return messages[index]

def update_offset(offset):
    open(OFFSET_FILE,"w").write(str(offset))

def get_offset():
    try:
        offset = open(OFFSET_FILE,"r").read().strip()
        return int(offset)
    except IOError,e:   
        return 0

def process(text):
    print text 
    if text == "/goodmorning":
       bot.send_message(user_id, get_random_good_morning()).wait()

"""
Get updates sent to the bot
"""
def get_updates(offset):
    if offset == 0:
        updates = bot.get_updates().wait()
    else:
        updates = bot.get_updates(offset=offset+1,limit=5).wait()
    for update in updates:
        process(update.message.text)
    if(len(updates) > 0):
        update_offset(updates[-1].update_id)

get_updates(get_offset())

