from aiogram import types, Dispatcher
from create_bot import bot
from neo4j_country_db import most_dangerous_places_db


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text="В разработке")
    except:
        pass


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Самые_опасные_места'])
