from aiogram import types, Dispatcher
from create_bot import bot
from keybords import other
from neo4j_country_db import rq
from keybords import start_keybord


answer_user = dict()


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет выбери кнопку', reply_markup=start_keybord.kb_start)
    except:
        pass


async def echo(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text=message.text)
    except:
        pass


async def water_cb(callback: types.CallbackQuery, callback_data: dict) -> None:
    await callback.message.edit_text(text='Столица', reply_markup=other.ikb_capital)
    answer_user['accessToSeaOrOcean'] = callback_data['action']


async def cities_are_good():
    final_message = str()
    cities_are_good = list()

    for c in rq.findCitiesWithAccessToWater(eval(answer_user['accessToSeaOrOcean'])):
        cities_are_good.append(c)

    if eval(answer_user['capital']) is True:
        cities = rq.findCapitalName(cities_are_good)
        for city in cities:
            info = rq.findFullInformationAboutCity(city)
            final_message += f'Название города: {info[0]["city.name"]}\n' \
                             f'Есть выход к морю: {info[0]["city.accessToSeaOrOcean"]}\n' \
                             f'Столица: True\n ' \
                             f'===================\n'
    elif eval(answer_user['capital']) is False:
        try:
            cities = rq.findCapitalName(cities_are_good)
            for _ in cities:
                cities_are_good.remove(_)
        except:
            pass
        for city in cities_are_good:
            info = rq.findFullInformationAboutCity(city)
            final_message += f'Название города: {info[0]["city.name"]}\n' \
                             f'Есть выход к морю: {info[0]["city.accessToSeaOrOcean"]}\n' \
                             f'===================\n'
    return final_message


async def capital_cb(callback: types.CallbackQuery, callback_data: dict) -> None:
    answer_user['capital'] = callback_data['action']
    final_message = await cities_are_good()
    if final_message:
        await callback.message.edit_text(text=final_message)
    else:
        await callback.message.edit_text(text="Нет городов которые вам походят")



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(echo)
    # dp.register_callback_query_handler(water_cb, other.cb_water.filter())
    # dp.register_callback_query_handler(capital_cb, other.cb_capital.filter())


