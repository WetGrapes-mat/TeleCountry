from aiogram import types, Dispatcher
from create_bot import bot


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text="В разработке")
    except:
        pass


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_образования'])
