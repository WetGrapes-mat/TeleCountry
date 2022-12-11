from aiogram import types, Dispatcher
from create_bot import bot
from agents import country_migration as cm
from neo4j_country_db import country_migration_db
from keybords import country_migration

answer_user = dict()


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text="Важно ли для вас наличие море/океана в новой стране", reply_markup=country_migration.ikb_water)
    except:
        pass


async def water_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Вы хотите жить где скорость жизни быстрая или где скорость жизни маленькая и нет суеты', reply_markup=country_migration.ikb_city)
    answer_user['water'] = callback_data['action']

async def isBig_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Какой климат вы бы предпочли \n холодный - среднее годовая темепратура меньше 10'
                                          '\n умереный - среднее годовая темепратура от 10 до 20\n'
                                          'жаркий - среднее годовая темепратура более 20', reply_markup=country_migration.ikb_climat)
    answer_user['isBig'] = callback_data['action']

async def climat_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Вы планируете переехать один или семьей(2 взрослых, 1 школьник)', reply_markup=country_migration.ikb_family)
    answer_user['climat'] = callback_data['action']

async def family_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Вы планируете передвигаться на общественом транспорте или на собственом автомобиле', reply_markup=country_migration.ikb_transportation)
    answer_user['family'] = callback_data['action']

async def transport_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Где вы планируете снимать жилье в центре на окраине', reply_markup=country_migration.ikb_rent)
    answer_user['transport'] = callback_data['action']

async def flat_answer(callback: types.CallbackQuery, callback_data: dict):
    if answer_user['family'] == "1":
        await callback.message.edit_text(text='Выберете заработок на который вы расчитаваете (если мы не сможем найти в нужном диапазоне мы найдет ближайший подходящий)', reply_markup=country_migration.ikb_solo_price)
    elif answer_user['family'] == "3":
        await callback.message.edit_text(text='Выберете заработок на который вы расчитаваете (если мы не сможем найти в нужном диапазоне мы найдет ближайший подходящий)', reply_markup=country_migration.ikb_family_price)
    answer_user['flat'] = callback_data['action']

async def money_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Важна ли толерантность к ЛГБТ', reply_markup=country_migration.ikb_lgbt)
    answer_user['price'] = callback_data['action']


# async def workplace(callback: types.CallbackQuery, callback_data: dict):
#     await callback.message.edit_text(text='Оцените насколько важено разбнообразие мест для развелечения от 1 до 3\n (1 - без разницы, 3 - жизнено необходимо)', reply_markup=country_migration.ikb_nightLife)
#     answer_user['workplace'] = callback_data['action']
#
# async def nightlife(callback: types.CallbackQuery, callback_data: dict):
#     await callback.message.edit_text(text='Оцените насколько важно толерантное отношение к лгбт от 1 до 3\n (1 - без разницы, 3 - жизнено необходимо)', reply_markup=country_migration.ikb_lgbt)
#     answer_user['nightlife'] = callback_data['action']
#
async def lgbt(callback: types.CallbackQuery, callback_data: dict):
    answer_user['lgbt'] = callback_data['action']
    print(answer_user)
    await callback.message.edit_text(text=cm.agent.calculate(answer_user))





def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_миграции'])
    dp.register_callback_query_handler(water_answer, country_migration.cb_water.filter())
    dp.register_callback_query_handler(isBig_answer, country_migration.cb_isBig.filter())
    dp.register_callback_query_handler(climat_answer, country_migration.cb_climat.filter())
    dp.register_callback_query_handler(family_answer, country_migration.cb_family.filter())
    dp.register_callback_query_handler(transport_answer, country_migration.cb_transportation.filter())
    dp.register_callback_query_handler(flat_answer, country_migration.cb_rent.filter())
    dp.register_callback_query_handler(money_answer, country_migration.cb_solo_price.filter() )
    dp.register_callback_query_handler(money_answer, country_migration.cb_family_price.filter())

    dp.register_callback_query_handler(lgbt, country_migration.cb_lgbt.filter())


