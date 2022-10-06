from aiogram import types, Dispatcher
from create_bot import bot
from keybords import other


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


async def capital_cb(callback: types.CallbackQuery, callback_data: dict) -> None:
    await callback.message.edit_text(text='Все')
    answer_user['capital'] = callback_data['action']


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(echo)
    dp.register_callback_query_handler(water_cb, other.cb_water.filter())
    dp.register_callback_query_handler(capital_cb, other.cb_capital.filter())


