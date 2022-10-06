from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


cb_water = CallbackData('water', 'action')
i_button_yes_water = InlineKeyboardButton('Да', callback_data=cb_water.new('True'))
i_button_no_water = InlineKeyboardButton('Нет', callback_data=cb_water.new('False'))
ikb_water = InlineKeyboardMarkup(inline_keyboard=[[i_button_yes_water, i_button_no_water]])

cb_capital = CallbackData('capital', 'action')
i_button_yes_capital = InlineKeyboardButton('Да', callback_data=cb_capital.new('True'))
i_button_no_capital = InlineKeyboardButton('Нет', callback_data=cb_capital.new('False'))
ikb_capital = InlineKeyboardMarkup(inline_keyboard=[[i_button_yes_capital, i_button_no_capital]])