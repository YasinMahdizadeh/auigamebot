import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackQueryHandler
import time
token = '1037836554:AAEhuWo_Ix10EpAJ-hnEVuIpdb-QXC_6-cw'
group_id = -384730643
yasin_id =  320435181
is_game_running = False
players = set()
#https://api.telegram.org/bot1037836554:AAEhuWo_Ix10EpAJ-hnEVuIpdb-QXC_6-cw/getupdates

bot = telegram.Bot(token)
def update_type(update):
    if update.message: return "message"
    if update.edited_message: return "edited_message"
    if update.channel_post: return "channel_post"
    if update.edited_channel_post: return "edited_channel_post"
    if update.inline_query: return "inline_query"
    if update.chosen_inline_result: return "chosen_inline_result"
    if update.callback_query: return "callback_query"
    if update.shipping_query: return "shipping_query"
    if update.pre_checkout_query: return "pre_checkout_query"
    if update.poll: return "poll"
    if update.poll_answer: return "poll_answer"

def get_new_updates(id):
    updates = bot.get_updates()
    new_updates = []
    for u in updates:
        if u.update_id > id:
            new_updates.append(u)

    return new_updates

def max_update_id(updates):
    update_ids = []
    if updates:
        for u in updates:
            update_ids.append(u.update_id)
        return max(update_ids)
    else:
        return 0

def start_game():
    text = "روی دکمه زیر کلیک کنید تا وارد بازی شوید!"
    keyboard = [[InlineKeyboardButton("Join Game!", callback_data='user joined', url='https://t.me/auigamebot?start=test')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id= group_id, text=text, reply_markup=reply_markup)

def print_players_list():
    text = '{} بازیکن'.format(len(players))
    for player in players:
        text = text + '\n@{}'.format(player[1])
    bot.send_message(chat_id=group_id, text=text)

updates = bot.get_updates()
last_update_id = max_update_id(updates)

while (True):

    time.sleep(3.2)
    updates = bot.get_updates()
    new_updates = get_new_updates(last_update_id)
    last_update_id = max_update_id(updates)
    # print("newones= ",[u for u in new_updates],"\n\n")

    #############################################

    for update in new_updates :
        if update.message.chat.id == group_id:
            if update.message.text == '/start@auigamebot':
                if not is_game_running:
                    start_game()
                    is_game_running = True
                else:
                    bot.send_message(chat_id=group_id, text="بازی در حال اجراست!")
            if update.message.text == '/players@auigamebot':
                print_players_list()

        if update.message.text == "/start test":
            players.add((update.message.chat.id, update.message.chat.username))
            print_players_list()
