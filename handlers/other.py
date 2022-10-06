from aiogram import types, Dispatcher
from create_bot import bot
from keybords import other
from neo4j_country_db import rq


answer_user = dict()


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вода', reply_markup=other.ikb_water)
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
    if eval(answer_user['capital']) is True:
        city = rq.findCapitalName()
        info = rq.findFullInformationAboutCity(city)
        final_message += f'Название города: {info[0]["city.name"]}\n' \
                         f'Есть выход к морю: {info[0]["city.accessToSeaOrOcean"]}\n' \
                         f'Столица: True\n ' \
                         f'===================\n'
    for c in rq.findCitiesWithAccessToWater(eval(answer_user['accessToSeaOrOcean'])):
        if c not in cities_are_good and c != rq.findCapitalName():
            cities_are_good.append(c)

    for city in cities_are_good:
        info = rq.findFullInformationAboutCity(city)

        final_message += f'Название города: {info[0]["city.name"]}\n' \
                         f'Есть выход к морю: {info[0]["city.accessToSeaOrOcean"]}\n' \
                         f'===================\n'
    return final_message


async def capital_cb(callback: types.CallbackQuery, callback_data: dict) -> None:
    answer_user['capital'] = callback_data['action']
    final_message = await cities_are_good()

    await callback.message.edit_text(text=final_message)



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(echo)
    dp.register_callback_query_handler(water_cb, other.cb_water.filter())
    dp.register_callback_query_handler(capital_cb, other.cb_capital.filter())


