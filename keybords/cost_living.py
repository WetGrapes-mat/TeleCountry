from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
# from agents.cost_living import CostLiving
from agents.cost_living import cl


# cl = CostLiving()

kb_transportation = CallbackData('transportation', 'action')
i_button_taxi = InlineKeyboardButton('такси', callback_data=kb_transportation.new("такси"))
i_button_car = InlineKeyboardButton('своя машина', callback_data=kb_transportation.new("своя машина"))
i_button_public = InlineKeyboardButton('общественный транспорт',
                                       callback_data=kb_transportation.new("общественный транспорт"))
ikb_transportation = InlineKeyboardMarkup(inline_keyboard=[[i_button_taxi, i_button_car, i_button_public]])

kb_rent = CallbackData('rent', 'action')
i_button_1_c = InlineKeyboardButton('1-к в центре', callback_data=kb_rent.new("1-к в центре"))
i_button_3_c = InlineKeyboardButton('3-к в центре', callback_data=kb_rent.new("3-к в центре"))
i_button_1_nc = InlineKeyboardButton('1-к на окраине', callback_data=kb_rent.new("1-к на окраине"))
i_button_3_nc = InlineKeyboardButton('3-к на окраине', callback_data=kb_rent.new("3-к на окраине"))
i_button_own = InlineKeyboardButton('своё жильё', callback_data=kb_rent.new("своё жильё"))
ikb_rent = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_c], [i_button_3_c], [i_button_1_nc], [i_button_3_nc], [i_button_own]])

kb_members_amount = CallbackData('members_amount', 'action')
i_button_1_member = InlineKeyboardButton('1', callback_data=kb_members_amount.new(1))
i_button_2_member = InlineKeyboardButton('2', callback_data=kb_members_amount.new(2))
i_button_3_member = InlineKeyboardButton('3', callback_data=kb_members_amount.new(3))
i_button_4_member = InlineKeyboardButton('4', callback_data=kb_members_amount.new(4))
i_button_5_member = InlineKeyboardButton('5', callback_data=kb_members_amount.new(5))
i_button_6_member = InlineKeyboardButton('6', callback_data=kb_members_amount.new(6))
ikb_members_amount = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_member, i_button_2_member, i_button_3_member,
                                                            i_button_4_member, i_button_5_member, i_button_6_member]])

kb_child_preschool = CallbackData('child_preschool', 'action')
i_button_0_cps = InlineKeyboardButton('0', callback_data=kb_child_preschool.new(0))
i_button_1_cps = InlineKeyboardButton('1', callback_data=kb_child_preschool.new(1))
i_button_2_cps = InlineKeyboardButton('2', callback_data=kb_child_preschool.new(2))
i_button_3_cps = InlineKeyboardButton('3', callback_data=kb_child_preschool.new(3))
i_button_4_cps = InlineKeyboardButton('4', callback_data=kb_child_preschool.new(4))
i_button_5_cps = InlineKeyboardButton('5', callback_data=kb_child_preschool.new(5))
ikb_child_preschool = InlineKeyboardMarkup(inline_keyboard=[[i_button_0_cps, i_button_1_cps, i_button_2_cps,
                                                             i_button_3_cps, i_button_4_cps, i_button_5_cps]])


kb_child_school = CallbackData('child_school', 'action')
i_button_0_cs = InlineKeyboardButton('0', callback_data=kb_child_school.new(0))
i_button_1_cs = InlineKeyboardButton('1', callback_data=kb_child_school.new(1))
i_button_2_cs = InlineKeyboardButton('2', callback_data=kb_child_school.new(2))
i_button_3_cs = InlineKeyboardButton('3', callback_data=kb_child_school.new(3))
i_button_4_cs = InlineKeyboardButton('4', callback_data=kb_child_school.new(4))
i_button_5_cs = InlineKeyboardButton('5', callback_data=kb_child_school.new(5))
ikb_child_school = InlineKeyboardMarkup(inline_keyboard=[[i_button_0_cs, i_button_1_cs, i_button_2_cs, i_button_3_cs,
                                                          i_button_4_cs, i_button_5_cs]])


kb_smoking_pack = CallbackData('smoking_pack', 'action')
i_button_0_sm = InlineKeyboardButton('0', callback_data=kb_smoking_pack.new(0))
i_button_1_sm = InlineKeyboardButton('1', callback_data=kb_smoking_pack.new(1))
i_button_2_sm = InlineKeyboardButton('2', callback_data=kb_smoking_pack.new(2))
i_button_3_sm = InlineKeyboardButton('3', callback_data=kb_smoking_pack.new(3))
i_button_4_sm = InlineKeyboardButton('4', callback_data=kb_smoking_pack.new(4))
ikb_smoking_pack = InlineKeyboardMarkup(inline_keyboard=[[i_button_0_sm, i_button_1_sm, i_button_2_sm, i_button_3_sm,
                                                          i_button_4_sm]])

kb_country_choice = CallbackData('country_choice', 'action')
i_button_1_country = InlineKeyboardButton("Подсчитать для 1 страны",
                                          callback_data=kb_country_choice.new("Подсчитать для 1 страны"))
i_button_rating = InlineKeyboardButton("Рейтинг стран", callback_data=kb_country_choice.new("Рейтинг стран"))
ikb_country_choice = InlineKeyboardMarkup(inline_keyboard=[[i_button_1_country, i_button_rating]])


kb_country_name = CallbackData('county_name', 'action')
country_list = []
for country in cl.get_countries():
    i_button = InlineKeyboardButton(country, callback_data=kb_country_name.new(country))
    country_list.append([i_button])

ikb_country_name = InlineKeyboardMarkup(inline_keyboard=country_list)


