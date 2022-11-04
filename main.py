from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from random import randrange
from names import get_full_name

bot = TeleBot('5705391311:AAHUQicjt3vrigC-sBy2b-i_mSRI31NmdQM')


@bot.message_handler(commands=['start'])
def start(msg):
    """
    on start
    -
    Respond to /start command
    """
    chat_id = msg.chat.id
    first_name = msg.chat.first_name
    hello = f"مرحبا {first_name},\nأضغط احد الازرار الاتية"
    markup = ReplyKeyboardMarkup()
    markup.resize_keyboard = True
    markup.add(KeyboardButton('صورة عشوائية'))
    markup.add(KeyboardButton('إسم عشوائي'))
    markup.add(KeyboardButton('إخفاء الازرار'))
    return bot.send_message(chat_id,hello,reply_markup=markup)

@bot.message_handler(func=lambda msg:True)
def new_msg(msg):
    """
    on new message
    -
    check if message text is equal to one of our buttons text
    """
    chat_id = msg.chat.id
    text = msg.text
    img_url = f'https://picsum.photos/{randrange(720,1080)}'
    name = get_full_name()
    hide_text = 'تم اخفاء الأزرار اضغط /start لأضهارها '
    if text == 'صورة عشوائية':
        return bot.send_photo(chat_id,img_url,"صورة عشوائية")
    elif text == 'إسم عشوائي':
        return bot.send_message(chat_id,name)
    elif text == 'إخفاء الازرار':
        return bot.send_message(chat_id,hide_text,reply_markup=ReplyKeyboardRemove())
bot.polling()
