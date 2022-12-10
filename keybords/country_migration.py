from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


cb_water = CallbackData('water', 'action')
i_button_yes_water = InlineKeyboardButton('Да', callback_data=cb_water.new(True))
i_button_no_water = InlineKeyboardButton('Нет', callback_data=cb_water.new(False))
ikb_water = InlineKeyboardMarkup(inline_keyboard=[[i_button_yes_water, i_button_no_water]])


cb_isBig = CallbackData('isBig', 'action')
i_button_yes_city = InlineKeyboardButton('Большом', callback_data=cb_isBig.new(True))
i_button_no_city = InlineKeyboardButton('Маленьком', callback_data=cb_isBig.new(False))
ikb_city = InlineKeyboardMarkup(inline_keyboard=[[i_button_yes_city, i_button_no_city]])


cb_climat = CallbackData('climat', 'action')
i_button_1_climat = InlineKeyboardButton('Холодный ', callback_data=cb_climat.new(1))
i_button_2_climat = InlineKeyboardButton('Умереный', callback_data=cb_climat.new(2))
i_button_3_climat = InlineKeyboardButton('Жаркий', callback_data=cb_climat.new(3))
ikb_climat = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_climat, i_button_2_climat,i_button_3_climat]])


cb_transport = CallbackData('transport', 'action')
i_button_1_transport = InlineKeyboardButton('1', callback_data=cb_transport.new(1))
i_button_2_transport = InlineKeyboardButton('2', callback_data=cb_transport.new(2))
i_button_3_transport = InlineKeyboardButton('3', callback_data=cb_transport.new(3))
i_button_4_transport = InlineKeyboardButton('4', callback_data=cb_transport.new(4))
i_button_5_transport = InlineKeyboardButton('5', callback_data=cb_transport.new(5))
ikb_transport = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_transport, i_button_2_transport, i_button_3_transport,
                                                            i_button_4_transport, i_button_5_transport]])

cb_english = CallbackData('english', 'action')
i_button_1_english = InlineKeyboardButton('1', callback_data=cb_english.new(1))
i_button_2_english = InlineKeyboardButton('2', callback_data=cb_english.new(2))
i_button_3_english = InlineKeyboardButton('3', callback_data=cb_english.new(3))
i_button_4_english = InlineKeyboardButton('4', callback_data=cb_english.new(4))
i_button_5_english = InlineKeyboardButton('5', callback_data=cb_english.new(5))
ikb_english = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_english, i_button_2_english, i_button_3_english,
                                                            i_button_4_english, i_button_5_english]])

cb_workplace = CallbackData('workplace', 'action')
i_button_1_workplace = InlineKeyboardButton('1', callback_data=cb_workplace.new(1))
i_button_2_workplace = InlineKeyboardButton('2', callback_data=cb_workplace.new(2))
i_button_3_workplace = InlineKeyboardButton('3', callback_data=cb_workplace.new(3))
i_button_4_workplace = InlineKeyboardButton('4', callback_data=cb_workplace.new(4))
i_button_5_workplace = InlineKeyboardButton('5', callback_data=cb_workplace.new(5))
ikb_workplace = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_workplace, i_button_2_workplace, i_button_3_workplace,
                                                            i_button_4_workplace, i_button_5_workplace]])

cb_nightLife = CallbackData('nightLife', 'action')
i_button_1_nightLife = InlineKeyboardButton('1', callback_data=cb_nightLife.new(1))
i_button_2_nightLife = InlineKeyboardButton('2', callback_data=cb_nightLife.new(2))
i_button_3_nightLife = InlineKeyboardButton('3', callback_data=cb_nightLife.new(3))
i_button_4_nightLife = InlineKeyboardButton('4', callback_data=cb_nightLife.new(4))
i_button_5_nightLife = InlineKeyboardButton('5', callback_data=cb_nightLife.new(5))
ikb_nightLife = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_nightLife, i_button_2_nightLife, i_button_3_nightLife,
                                                            i_button_4_nightLife, i_button_5_nightLife]])

cb_lgbt = CallbackData('lgbt', 'action')
i_button_1_lgbt = InlineKeyboardButton('1', callback_data=cb_lgbt.new(1))
i_button_2_lgbt = InlineKeyboardButton('2', callback_data=cb_lgbt.new(2))
i_button_3_lgbt = InlineKeyboardButton('3', callback_data=cb_lgbt.new(3))
i_button_4_lgbt = InlineKeyboardButton('4', callback_data=cb_lgbt.new(4))
i_button_5_lgbt = InlineKeyboardButton('5', callback_data=cb_lgbt.new(5))
ikb_lgbt = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_lgbt, i_button_2_lgbt, i_button_3_lgbt,
                                                            i_button_4_lgbt, i_button_5_lgbt]])