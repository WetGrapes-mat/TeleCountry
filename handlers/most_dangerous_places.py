from aiogram import types, Dispatcher
from create_bot import bot
from controller.controller import contrl

from keybords import most_dangerous_places

answer_user = dict()


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text="Выберите действие:",
                               reply_markup=most_dangerous_places.ikb_menu)
    except:
        pass


async def menu(callback: types.CallbackQuery, callback_data: dict):
    answer = callback_data['action']
    if answer == 'False':  # 1 страна
        await callback.message.edit_text(text='Выберите страну',
                                         reply_markup=most_dangerous_places.ikb_country)
    elif answer == 'True':  # Рейтинг стран
        answer_user['country'] = "Рейтинг"
        final_message = contrl.control_most_dangerous_places(answer_user["country"])
        if final_message:
            await callback.message.edit_text(text=final_message)
        else:
            await callback.message.edit_text(text="Хз")


async def country(callback: types.CallbackQuery, callback_data: dict):
    answer_user['country'] = callback_data['action']
    final_message = contrl.control_most_dangerous_places(answer_user["country"])
    if final_message:
        await callback.message.edit_text(text=final_message)
    else:
        await callback.message.edit_text(text="Хз")


# def count():
#     mdp.get_all_information()
#     user_answer = answer_user
#     message =  mdp.count(user_answer["country"])
#     return message


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Самые_опасные_места'])
    dp.register_callback_query_handler(menu, most_dangerous_places.cb_menu.filter())
    dp.register_callback_query_handler(menu, most_dangerous_places.cb_menu.filter())
    dp.register_callback_query_handler(country, most_dangerous_places.cb_country.filter())
