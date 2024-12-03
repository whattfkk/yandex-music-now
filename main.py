import telebot
import requests

token = 'yamusictoken'
bot = telebot.TeleBot('bottoken')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(tgid, 'hello')

@bot.message_handler(commands=['now'])
def now(message):
    response = requests.get(f"https://api.mipoh.ru/get_current_track_beta?ya_token={token}")
    if 'entity_type' in response.json():
        bot.send_photo(tgid, photo = response.json()['track']['img'], caption = f'_whattfkk_ is currently listeni>    else:
        bot.send_photo(tgid, photo = f'{response.json()[0]['cover']['uri'][-2:]}1000x1000', caption = f'_whattfkk>

bot.polling(interval = 0, none_stop = True)
