import requests
import json
import time

##We can use https://api.telegram.org/bot<token>/getme to get Information about our bot_token

##The simplest way for us to retrieve
##messages sent to our Bot is through the getUpdates call.
##If you visit https://api.telegram.org/bot<your-bot-token>/getUpdates


##Sending a message through our browser:
##https://api.telegram.org/bot<your-bot-token>/sendMessage?chat_id=<chat-id>&text=TestReply

bot_username = 'roboselfbot'
bot_token = '898769638:AAFCcjEsZ60G9ywLJtpEcBnecZXQBEW7zuQ'

bot_url='https://api.telegram.org/bot%s/'%(bot_token)
text = "Hello, it's me!"

#https://api.telegram.org/bot898769638:AAFCcjEsZ60G9ywLJtpEcBnecZXQBEW7zuQ/sendMessage?text={%22hey%22}&chat_id={320435181}
##MychatID = 320435181

## and We can also use URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    pasokh = requests.get(url)
    content = pasokh.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads( content )
    return js

def get_updates(offset=None):
    url = bot_url + 'getupdates'
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    if (num_updates != 0):
        last_update = num_updates-1
        text = updates["result"][last_update]["message"]["text"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        return (text, chat_id)
    else:
        return (None, None)

def send_message(text, chat_id):
    url = bot_url + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_last_update_id(updates):
    update_ids = []
    for i in updates['result']:
        update_ids.append(int(i["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        send_message(text, chat_id)

##this part of code helps us to run this code continusely, instead of one-time
##Running by terminal!

'''
def main():
    last_chat_id = None
    while True:
        updates = get_updates(last_chat_id)

        if (len(updates["result"]) > 0 ):
            last_update_id = get_last_update_id(updates)

            #echo_all(updates)
        time.sleep(0.5)
'''

def main():
    last_textchat = (None,None)
    while True:
        send_message()
        text, chat = get_last_chat_id_and_text(get_updates())
        print(text, chat)
        if ( (text,chat) != last_textchat ):
            send_message(text, chat)
            last_textchat = (text, chat)
        time.sleep(0.5)

main()

##but what if two persons send same messages? previous method ignored the second
#one. we use update-id for get_updates() . update-id is incremental and
#we can offset chat-id numbers.
