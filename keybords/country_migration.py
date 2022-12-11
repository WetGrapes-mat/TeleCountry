from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


cb_water = CallbackData('water', 'action')
i_button_yes_water = InlineKeyboardButton('Да', callback_data=cb_water.new(True))
i_button_no_water = InlineKeyboardButton('Нет', callback_data=cb_water.new(False))
ikb_water = InlineKeyboardMarkup(inline_keyboard=[[i_button_yes_water, i_button_no_water]])


cb_isBig = CallbackData('isBig', 'action')
i_button_yes_city = InlineKeyboardButton('Быстрый', callback_data=cb_isBig.new(1))
i_button_no_city = InlineKeyboardButton('Медленый', callback_data=cb_isBig.new(2))
ikb_city = InlineKeyboardMarkup(inline_keyboard=[[i_button_yes_city, i_button_no_city]])


cb_climat = CallbackData('climat', 'action')
i_button_1_climat = InlineKeyboardButton('Холодный ', callback_data=cb_climat.new(1))
i_button_2_climat = InlineKeyboardButton('Умереный', callback_data=cb_climat.new(2))
i_button_3_climat = InlineKeyboardButton('Жаркий', callback_data=cb_climat.new(3))
ikb_climat = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_climat, i_button_2_climat,i_button_3_climat]])


# cb_transport = CallbackData('transport', 'action')
# i_button_1_transport = InlineKeyboardButton('1', callback_data=cb_transport.new(1))
# i_button_2_transport = InlineKeyboardButton('2', callback_data=cb_transport.new(2))
# i_button_3_transport = InlineKeyboardButton('3', callback_data=cb_transport.new(3))
# i_button_4_transport = InlineKeyboardButton('4', callback_data=cb_transport.new(4))
# i_button_5_transport = InlineKeyboardButton('5', callback_data=cb_transport.new(5))
# ikb_transport = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_transport, i_button_2_transport, i_button_3_transport]])

cb_english = CallbackData('english', 'action')
i_button_1_english = InlineKeyboardButton('1', callback_data=cb_english.new(1))
i_button_2_english = InlineKeyboardButton('2', callback_data=cb_english.new(2))
i_button_3_english = InlineKeyboardButton('3', callback_data=cb_english.new(3))
i_button_4_english = InlineKeyboardButton('4', callback_data=cb_english.new(4))
i_button_5_english = InlineKeyboardButton('5', callback_data=cb_english.new(5))
ikb_english = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_english, i_button_2_english, i_button_3_english]])

cb_workplace = CallbackData('workplace', 'action')
i_button_1_workplace = InlineKeyboardButton('1', callback_data=cb_workplace.new(1))
i_button_2_workplace = InlineKeyboardButton('2', callback_data=cb_workplace.new(2))
i_button_3_workplace = InlineKeyboardButton('3', callback_data=cb_workplace.new(3))
i_button_4_workplace = InlineKeyboardButton('4', callback_data=cb_workplace.new(4))
i_button_5_workplace = InlineKeyboardButton('5', callback_data=cb_workplace.new(5))
ikb_workplace = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_workplace, i_button_2_workplace, i_button_3_workplace]])

cb_nightLife = CallbackData('nightLife', 'action')
i_button_1_nightLife = InlineKeyboardButton('1', callback_data=cb_nightLife.new(1))
i_button_2_nightLife = InlineKeyboardButton('2', callback_data=cb_nightLife.new(2))
i_button_3_nightLife = InlineKeyboardButton('3', callback_data=cb_nightLife.new(3))
i_button_4_nightLife = InlineKeyboardButton('4', callback_data=cb_nightLife.new(4))
i_button_5_nightLife = InlineKeyboardButton('5', callback_data=cb_nightLife.new(5))
ikb_nightLife = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_nightLife, i_button_2_nightLife, i_button_3_nightLife]])

cb_lgbt = CallbackData('lgbt', 'action')
i_button_1_lgbt = InlineKeyboardButton('Да', callback_data=cb_lgbt.new(True))
i_button_2_lgbt = InlineKeyboardButton('Нет', callback_data=cb_lgbt.new(False))

ikb_lgbt = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_lgbt, i_button_2_lgbt]])

cb_family = CallbackData('family', 'action')
i_button_1_member = InlineKeyboardButton('Один', callback_data=cb_family.new(1))
i_button_2_member = InlineKeyboardButton('Семьей', callback_data=cb_family.new(3))
ikb_family = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_member, i_button_2_member]])

cb_transportation = CallbackData('transport', 'action')
i_button_car = InlineKeyboardButton('своя машина', callback_data=cb_transportation.new("своя машина"))
i_button_public = InlineKeyboardButton('общественный транспорт',
                                       callback_data=cb_transportation.new("общественный транспорт"))
ikb_transportation = InlineKeyboardMarkup(inline_keyboard=[[i_button_car, i_button_public]])


cb_rent = CallbackData('flat', 'action')
i_button_1_c = InlineKeyboardButton('центре', callback_data=cb_rent.new("центре"))
i_button_3_nc = InlineKeyboardButton('окраине', callback_data=cb_rent.new("окраине"))
ikb_rent = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_c],[i_button_3_nc]])


cb_family_price = CallbackData('family_price', 'action')
i_button_1_family_price = InlineKeyboardButton('менее 3600', callback_data=cb_family_price.new('3600'))
i_button_2_family_price = InlineKeyboardButton('от 3600 до 5200', callback_data=cb_family_price.new('3600_5200'))
i_button_3_family_price = InlineKeyboardButton('более 5200', callback_data=cb_family_price.new('5200'))
ikb_family_price = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_family_price, i_button_2_family_price, i_button_3_family_price]])

cb_solo_price = CallbackData('solo_price', 'action')
i_button_1_solo_price = InlineKeyboardButton('менее 1300', callback_data=cb_solo_price.new('1300'))
i_button_2_solo_price = InlineKeyboardButton('от 1300 до 1800', callback_data=cb_solo_price.new('1300_1800'))
i_button_3_solo_price = InlineKeyboardButton('более 1800', callback_data=cb_solo_price.new('1800'))
ikb_solo_price = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_solo_price, i_button_2_solo_price, i_button_3_solo_price]])