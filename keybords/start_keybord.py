from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/Цена_жизни')
b2 = KeyboardButton('/Страна_для_образования')
b3 = KeyboardButton('/Страна_для_миграции')
b4 = KeyboardButton('/Страна_для_путешествия')
b5 = KeyboardButton('/Самые_опасные_места')
b6 = KeyboardButton('/Уровень_жизни')

kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_start.add(b1)
kb_start.add(b2)
kb_start.add(b3)
kb_start.add(b4)
kb_start.add(b5)
kb_start.add(b6)
