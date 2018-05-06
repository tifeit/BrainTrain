import config
import telebot
import pandas as pd

bot = telebot.TeleBot(config.token)
  
tasks=pd.read_csv('tasks.csv',sep=';',encoding='utf-8')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    row=tasks.sample(n=1)
    bot.send_message(message.chat.id, row['description'].values[0])
    
    bot.send_message(message.chat.id, row['tasks'].values[0])
    

if __name__ == '__main__':
     bot.polling(none_stop=True)