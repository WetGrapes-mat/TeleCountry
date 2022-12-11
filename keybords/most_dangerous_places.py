from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb_menu = CallbackData("menu", "action")
i_btn_top = InlineKeyboardButton("ТОП-5 опасных стран", callback_data=cb_menu.new(True))
i_btn_check_condition = InlineKeyboardButton("Проверить состояние введенной страны", callback_data=cb_menu.new(False))
ikb_menu = InlineKeyboardMarkup(inline_keyboard=[[i_btn_top, i_btn_check_condition]])


# добавить ввод названия страны с клавиатуры
cb_name = CallbackData("name", "action")