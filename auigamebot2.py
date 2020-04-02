import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import time
token = '1037836554:AAEhuWo_Ix10EpAJ-hnEVuIpdb-QXC_6-cw'
group_id = -384730643
yasin_id =  320435181

# https://api.telegram.org/bot1037836554:AAEhuWo_Ix10EpAJ-hnEVuIpdb-QXC_6-cw/getupdates

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

def remove_markup(id):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=id, text="Reply Removed", reply_markup=reply_markup)

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

keyboard = [[InlineKeyboardButton("Join Game!", callback_data='user joined')]]
reply_markup = InlineKeyboardMarkup(keyboard)
bot.send_message(chat_id= group_id, text="روی دکمه زیر کلیک کنید تا وارد بازی شوید!", reply_markup=reply_markup)

last_update_id = 0
while (True):
    # keyboard = [['1','2'],'3']
    #remove_markup(yasin_id)
    time.sleep(3.2)
    updates = bot.get_updates()
    new_updates = get_new_updates(last_update_id)


    #new_updates = get_new_updates()
    print("$$$.upda =  ",[u for u in updates], [update_type(u) for u in updates], "\n")
    print("!!!newones = ",[u for u in new_updates],"\n\n")
    last_update_id = max_update_id(updates)