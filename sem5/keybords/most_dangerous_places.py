from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from controller.controller import mdp

cb_menu = CallbackData("menu", "action")
i_btn_top = InlineKeyboardButton("ТОП опасных стран", callback_data=cb_menu.new(True))
i_btn_check_condition = InlineKeyboardButton("Проверить состояние введенной страны", callback_data=cb_menu.new(False))
ikb_menu = InlineKeyboardMarkup(inline_keyboard=[[i_btn_top], [i_btn_check_condition]])

cb_country = CallbackData('county', 'action')
country_list = []
for country in mdp.get_countries():
    i_button = InlineKeyboardButton(country, callback_data=cb_country.new(country))
    country_list.append([i_button])

ikb_country = InlineKeyboardMarkup(inline_keyboard=country_list)
