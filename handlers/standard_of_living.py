from aiogram import types, Dispatcher
from create_bot import bot
from neo4j_country_db import standard_of_living
from agents.standard_of_living import st


async def command(message: types.Message) -> None:
    a = st.get_country_rating()
    try:
        await bot.send_message(message.from_user.id, text=a)
    except:
        pass


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Уровень_жизни'])
