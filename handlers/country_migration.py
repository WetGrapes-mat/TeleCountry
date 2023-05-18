from aiogram import types, Dispatcher
from create_bot import bot
from controller.controller import contrl
from keybords import country_migration

answer_user = dict()


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text="Важно ли для вас наличие моря/океана?",
                               reply_markup=country_migration.ikb_water)
    except:
        pass


async def water_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(
        text='Вы предпочитаете быстрый темп жизни или размеренный темп и отсутствие суеты?',
        reply_markup=country_migration.ikb_city)
    answer_user['water'] = callback_data['action']


async def isBig_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(
        text='Какой климат вы бы предпочли: \n1. холодный - средняя годовая температура меньше 10 градусов;'
             '\n2. умеренный - средняя годовая температура от 10 до 20 градусов;\n'
             '3. жаркий - средняя годовая температура более 20 градусов?', reply_markup=country_migration.ikb_climat)
    answer_user['isBig'] = callback_data['action']


async def climat_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Вы планируете переехать один или семьей (2 взрослых, 1 школьник)?',
                                     reply_markup=country_migration.ikb_family)
    answer_user['climat'] = callback_data['action']


async def family_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(
        text='Вы планируете передвигаться на общественном транспорте или на собственном автомобиле?',
        reply_markup=country_migration.ikb_transportation)
    answer_user['family'] = callback_data['action']


async def transport_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Где вы планируете снимать жилье: в центре или на окраине?',
                                     reply_markup=country_migration.ikb_rent)
    answer_user['transport'] = callback_data['action']


async def flat_answer(callback: types.CallbackQuery, callback_data: dict):
    if answer_user['family'] == "1":
        await callback.message.edit_text(
            text='Выберите заработок, на который вы рассчитываете (если мы не сможем найти в нужном диапазоне, '
                 'найдем ближайший подходящий)',
            reply_markup=country_migration.ikb_solo_price)
    elif answer_user['family'] == "3":
        await callback.message.edit_text(
            text='Выберите заработок, на который вы рассчитаваете (если мы не сможем найти в нужном диапазоне, '
                 'мы найдем ближайший подходящий)',
            reply_markup=country_migration.ikb_family_price)
    answer_user['flat'] = callback_data['action']


async def money_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Важна ли для вас толерантность к ЛГБТ?', reply_markup=country_migration.ikb_lgbt)
    answer_user['price'] = callback_data['action']


async def lgbt(callback: types.CallbackQuery, callback_data: dict):
    answer_user['lgbt'] = callback_data['action']
    print(answer_user)
    await callback.message.edit_text(text=contrl.control_migration_bot(answer_user))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_миграции'])
    dp.register_callback_query_handler(water_answer, country_migration.cb_water.filter())
    dp.register_callback_query_handler(isBig_answer, country_migration.cb_isBig.filter())
    dp.register_callback_query_handler(climat_answer, country_migration.cb_climat.filter())
    dp.register_callback_query_handler(family_answer, country_migration.cb_family.filter())
    dp.register_callback_query_handler(transport_answer, country_migration.cb_transportation.filter())
    dp.register_callback_query_handler(flat_answer, country_migration.cb_rent.filter())
    dp.register_callback_query_handler(money_answer, country_migration.cb_solo_price.filter())
    dp.register_callback_query_handler(money_answer, country_migration.cb_family_price.filter())
    dp.register_callback_query_handler(lgbt, country_migration.cb_lgbt.filter())
