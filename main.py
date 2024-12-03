import telebot
import requests

token = '***' # токен яндекс.музыки
bot = telebot.TeleBot('***') # токен бота в тг
tgid = 111 # айди в тг

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(tgid, 'hello')

@bot.message_handler(commands=['now'])
def now(message):
    response = requests.get(f"https://api.mipoh.ru/get_current_track_beta?ya_token={token}") # запрос к апи для получения текущего трека
    if 'entity_type' in response.json():
    	bot.send_photo(tgid, photo = response.json()['track']['img'], caption = f'_whattfkk_ is currently listening to: *{response.json()['track']['title']}*, *{response.json()['track']['artist']}*', parse_mode="Markdown")
    else:
    	bot.send_photo(tgid, photo = f'{response.json()[0]['cover']['uri'][-2:]}1000x1000', caption = f'_whattfkk_ is currently listening to: *{response.json()[0]['title']}*, *{response.json()[0]['name']}*', parse_mode="Markdown")

bot.polling(interval = 0, none_stop = True)
