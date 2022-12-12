from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

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


async def command_test(message: types.Message):

    # await bot.send_message(message.from_user.id, '<a href="https://www.estudarfora.org.br/wp-content/uploads/2020/04/unipo.jpg">&#8203;</a>', parse_mode="HTML")
    await bot.send_media_group(message.chat.id, [InputMediaPhoto('https://www.estudarfora.org.br/wp-content/uploads/2020/04/unipo.jpg','привет'),
                                           InputMediaPhoto('https://www.ru.studies-in-europe.eu/img/uczelnie/a1673/g/Berlin-Universitat-zwischen-1890-und-1900-p2961.jpg'),
                                           InputMediaPhoto('https://www.univ-tlse2.fr/medias/photo/universite_1500638826879-jpg?ID_FICHE=191397')])


async def echo(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text=message.text)
    except:
        pass




def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_test, commands=['test'])
    dp.register_message_handler(echo)
    # dp.register_callback_query_handler(water_cb, other.cb_water.filter())
    # dp.register_callback_query_handler(capital_cb, other.cb_capital.filter())


