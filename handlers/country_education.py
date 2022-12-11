from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto
from create_bot import bot
from agents import country_education as cd
from neo4j_country_db import country_education_db as db
from keybords import country_education as keyboard

answer_user = dict()


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id,
                               text="Какому направлению вы хотите обучаться?",
                               reply_markup=keyboard.ikb_faculty)
    except:
        pass


async def faculty(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите программу обучения:',
                                     reply_markup=keyboard.ikb_program)
    answer_user['faculties'] = callback_data['action']


async def program(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text="Нужно ли вам место в общежитии?",
                                     reply_markup=keyboard.ikb_hostel)
    answer_user['programs'] = callback_data['action']


async def hostel(callback: types.CallbackQuery, callback_data: dict):
    delta = (db.find_max_cost() - db.find_min_cost()) // 3
    await callback.message.edit_text(text=f"Выберите примерную максимальную стоимость обучения: \n"
                                          f"1. от {db.find_min_cost()}$ до {db.find_min_cost() + delta}$;\n"
                                          f"2. до {db.find_max_cost() - delta}$;\n"
                                          f"3. до {db.find_max_cost() + 10}$",
                                     reply_markup=keyboard.ikb_cost)
    answer_user['hostel'] = callback_data["action"]


async def cost(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text="Сколько пачек сигарет в день вы курите?",
                                     reply_markup=keyboard.ikb_smoking_pack)
    answer_user["cost"] = int(callback_data['action'])


async def smoking1(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите средство передвижения',
                                     reply_markup=keyboard.ikb_transportation)
    answer_user['smoking'] = callback_data['action']


async def transportation1(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите недвижимость',
                                     reply_markup=keyboard.ikb_rent)
    answer_user['transportation'] = callback_data['action']


async def rent1(callback: types.CallbackQuery, callback_data: dict) -> None:
    answer_user['rent'] = callback_data['action']
    answer_user['child_preschool'] = 0
    answer_user['child_school'] = 0
    answer_user['members'] = 1
    answer_user['country'] = 'Рейтинг стран'
    await callback.message.edit_text(text=cd.agent.find_result(answer_user))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_образования'])
    dp.register_callback_query_handler(faculty, keyboard.cb_faculty.filter())
    dp.register_callback_query_handler(program, keyboard.cb_program.filter())
    dp.register_callback_query_handler(hostel, keyboard.cb_hostel.filter())
    dp.register_callback_query_handler(cost, keyboard.cb_cost.filter())
    dp.register_callback_query_handler(smoking1, keyboard.cb_cigarettes1.filter())
    dp.register_callback_query_handler(transportation1, keyboard.kb_transportation1.filter())
    dp.register_callback_query_handler(rent1, keyboard.kb_rent1.filter())

