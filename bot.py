import telebot
from javascript import require, On, Once, AsyncTask, once, off
import os
from dotenv import load_dotenv
# Getting variables from .env file
load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_TOKEN'))
admins = [] # Array with users' id who allowed to manage bot (You can get your ID by using /getID command)

mineflayer = require('mineflayer')
mcbot = ''


@bot.message_handler(commands=['start', 'help'])
class MCBOT():
     def __init__(self, nickname, bot):
          self.nickname = nickname
          self.bot = bot
     def connect(self):
          self.bot  = mineflayer.createBot({ 'host': os.getenv('HOST_ADDRESS'), 'port': os.getenv('PORT_SERVER'), 'username': self.nickname, 'hideErrors': False })
     def message(self, msg):
          self.bot.chat(msg)
     def quit(self):
        self.bot.quit()
     def sender(self):
          pass # todo Method for sending messages from minecraft chat to Telegram one

          
mcbot_ = MCBOT('MCChat', mcbot) # minecraft bot's instance initialization with "MCChat" nickname

@bot.message_handler(commands=['connect'])
def connect(message):
    if not(message.from_user.id in admins):
         bot.send_message(message.chat.id, 'You do not have permissions to do that')
    else:
         mcbot_.connect()
        

@bot.message_handler(commands=['quit'])
def quit(message):
    if not(message.from_user.id in admins):
         bot.send_message(message.chat.id, 'You do not have permissions to do that')
    else:
         mcbot_.quit()

@bot.message_handler(commands=['getID'])
def getID(message):   
     bot.send_message(message.chat.id, message.from_user.id)
   

@bot.message_handler(func=lambda message: True)    
def echo_all(message):
     mcbot_.message(f'[TG:@{str(message.from_user.username)}]: {str(message.text)}')    

bot.infinity_polling()

