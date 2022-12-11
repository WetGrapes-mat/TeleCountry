from aiogram import types, Dispatcher
from create_bot import bot
from keybords import cost_living


answer_user = dict()


async def command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выберите вариант работы бота',
                               reply_markup=cost_living.ikb_country_choice)
    except:
        pass


async def country_choice(callback: types.CallbackQuery, callback_data: dict):
    answer = callback_data['action']
    if answer == 'Подсчитать для 1 страны':
        await callback.message.edit_text(text='Выберите страну',
                                         reply_markup=cost_living.ikb_country_name)
    elif answer == 'Рейтинг стран':
        await callback.message.edit_text(text='Выберите количество членов семьи',
                                         reply_markup=cost_living.ikb_members_amount)
        answer_user['country'] = callback_data['action']


async def country_name(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите количество членов семьи',
                                     reply_markup=cost_living.ikb_members_amount)
    answer_user['country'] = callback_data['action']


async def members_amount(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите количество ваших детей, посещающих частный детский сад',
                                     reply_markup=cost_living.ikb_child_preschool)
    answer_user['members'] = callback_data['action']


async def child_preschool(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите количество ваших детей, посещающих частную международную школу',
                                     reply_markup=cost_living.ikb_child_school)
    answer_user['child_preschool'] = callback_data['action']


async def child_school(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите количество пачек сигарет, которые вы выкуриваете в день',
                                     reply_markup=cost_living.ikb_smoking_pack)
    answer_user['child_school'] = callback_data['action']


async def smoking(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите средство передвижения',
                                     reply_markup=cost_living.ikb_transportation)
    answer_user['smoking'] = callback_data['action']


async def transportation(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите недвижимость',
                                     reply_markup=cost_living.ikb_rent)
    answer_user['transportation'] = callback_data['action']


async def rent(callback: types.CallbackQuery, callback_data: dict) -> None:
    answer_user['rent'] = callback_data['action']
    final_message = get_answer()
    if final_message:
        await callback.message.edit_text(text=final_message)
    else:
        await callback.message.edit_text(text="Хз")


def get_answer():
    cost_living.cl.get_information()
    user_answers = answer_user
    # print(user_answers)
    message = cost_living.cl.out(int(user_answers["child_preschool"]),
                                               int(user_answers["child_school"]),
                                               int(user_answers["members"]),
                                               int(user_answers["smoking"]),
                                               user_answers["transportation"],
                                               user_answers["rent"],
                                               user_answers["country"])

    return message


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Цена_жизни'])
    dp.register_callback_query_handler(country_choice, cost_living.kb_country_choice.filter())
    dp.register_callback_query_handler(country_name, cost_living.kb_country_name.filter())
    dp.register_callback_query_handler(members_amount, cost_living.kb_members_amount.filter())
    dp.register_callback_query_handler(child_preschool, cost_living.kb_child_preschool.filter())
    dp.register_callback_query_handler(child_school, cost_living.kb_child_school.filter())
    dp.register_callback_query_handler(smoking, cost_living.kb_smoking_pack.filter())
    dp.register_callback_query_handler(transportation, cost_living.kb_transportation.filter())
    dp.register_callback_query_handler(rent, cost_living.kb_rent.filter())



