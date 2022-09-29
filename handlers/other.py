from aiogram import types, Dispatcher
from create_bot import bot
from keybords import kb_start


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет я курсач', reply_markup=kb_start)
    except:
        pass


async def echo(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text=message.text)
        # print(message.from_user.id , message.from_user.first_name , message.text)
    except:
        pass


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(echo)
