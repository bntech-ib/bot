import os
import requests
from  telegram.ext import Updater, CommandHandler

def make_greeting(update,context):
    
    context.bot.send_message(chat_id=update.effective_chat.id,text=greeting())
    
def make_good_by(update,context):
    
    context.bot.send_message(chat_id=update.effective_chat.id,text=goodBy())
    
   
def start(update,context):
    
    context.bot.send_message(chat_id=update.effective_chat.id,text='hello im new bot')
    
 
 
def greeting():
    
    
    return 'hello you are welcome'

def goodBy():
    
    return 'good by'
    
def main():
    
    TOKEN = ''
    updater = Updater(token=TOKEN ,use_context=True)
    dispatcher =updater.dispatcher
    
    
    greeting_hander = CommandHandler('greeting',make_greeting)
    goodBy_hander = CommandHandler('goodBy',make_good_by)
    
    dispatcher.add_handler(greeting_hander)
    dispatcher.add_handler(goodBy_hander)
    
    PORT = int(os.environ.get('PORT','443'))
    HOOK_URL = '',
    
    updater.start_webhook(listen='0.0.0.0',port=PORT,url_path=TOKEN,webhook_url=HOOK_URL)
    updater.idle()
    
    
    
    
    
if __name__ == '__main__':
    main()