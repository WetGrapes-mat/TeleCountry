from aiogram import types, Dispatcher
from create_bot import bot
from controller.controller import contrl


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text=contrl.control_standard_of_living())
    except:
        pass


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Уровень_жизни'])
