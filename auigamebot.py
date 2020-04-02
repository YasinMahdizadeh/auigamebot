import requests
import json
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup



token = '1037836554:AAEhuWo_Ix10EpAJ-hnEVuIpdb-QXC_6-cw'
username = 'auigamebot'
group_id = -384730643

is_game_running = False
bot_url = 'https://api.telegram.org/bot%s/' %token

#https://api.telegram.org/bot1037836554:AAEhuWo_Ix10EpAJ-hnEVuIpdb-QXC_6-cw/getupdates
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(update["update_id"])
    return max(update_ids)

def update_type( update):
    u = list(update.keys())
    u.remove('update_id')
    return u[0]

def get_updates (offset= None):
    url = bot_url + 'getupdates'
    '''if offset:
        url += "?offset={}".format(offset)'''
    ans = requests.get(url)
    answer = ans.content.decode("utf8")
    js = json.loads(answer)
    return js

# my chat id : 320435181
#-384730643 Game group id

def send_message(text, chat_id):
    url = bot_url + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def send_reply_markup(chat_id):
    keyboard = [[InlineKeyboardButton("1", callback_data='1'),
                 InlineKeyboardButton("2", callback_data='2')],

                [InlineKeyboardButton("3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    url = bot_url + "sendMessage?text={}&chat_id={}&reply_markup={}".format("A", chat_id,reply_markup)
    requests.get(url)

last_id = 0
while(True):
    #keyboard = [['1','2'],'3']
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot = telegram.Bot(token)
    bot.send_message(chat_id=320435181, text="ptb.", reply_markup=reply_markup)
    updates = bot.get_updates()
    print(updates, len(updates))
    print([u.message.text for u in updates])
    #send_reply_markup(320435181)

    '''new_updates = []

    for update in updates["result"]:
        update_id = update["update_id"]
        if update_id > last_id:
            new_updates.append(update)

    last_id = get_last_update_id(updates)
    print("!!!last_id = ", last_id)

    
    
    for update in new_updates:
        
        print("u...",update_type(update))
        text = update['message']['text']

        chat_id = update['message']['chat']['id']

        if chat_id == group_id and text == '/about@auigamebot':
            print("about!")
        if chat_id == group_id and text == '/start@auigamebot':
            if not is_game_running:
                print("start!")
            if is_game_running:
                print("there is a game running now. you can stop it and start a new one!")
                '''


