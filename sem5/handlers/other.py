from aiogram import types, Dispatcher
from create_bot import bot
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


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(echo)
