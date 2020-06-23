from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

host_keyboard = InlineKeyboardMarkup(row_width=2)

be_host = InlineKeyboardButton(text='Стати ведучим', callback_data='be_host')
host_keyboard.insert(be_host)

host_help = InlineKeyboardMarkup(row_width=2)

next_word = InlineKeyboardButton(text='Наступне Слово', callback_data='next_word')
host_help.insert(next_word)

show_word = InlineKeyboardButton(text='Показати слово', callback_data='show_word')
host_help.insert(show_word)
