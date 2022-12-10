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


async def water_access(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Вы хотите жить в большом городе или маленьком', reply_markup=country_migration.ikb_city)
    answer_user['water'] = callback_data['action']

async def isBig(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Какой климат вы бы предпочли \n холодный - среднее годовая темепратура меньше 10'
                                          '\n умереный - среднее годовая темепратура от 10 до 20\n'
                                          'жаркий - среднее годовая темепратура более 20', reply_markup=country_migration.ikb_climat)
    answer_user['isBig'] = callback_data['action']


async def climat_in_country(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Оцените насколько важен для вас общественый транспорт от 1 до 5\n (1 - без разницы, 5 - жизнено необходим)', reply_markup=country_migration.ikb_transport)
    answer_user['climat'] = callback_data['action']

async def transport(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Оцените насколько важен для вас английский язык у населения от 1 до 5\n (1 - без разницы, 5 - жизнено необходимо)', reply_markup=country_migration.ikb_english)
    answer_user['transport'] = callback_data['action']

async def english(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Оцените насколько важено разнообразие рабочих мест от 1 до 5\n (1 - без разницы, 5 - жизнено необходимо)', reply_markup=country_migration.ikb_workplace)
    answer_user['english'] = callback_data['action']

async def workplace(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Оцените насколько важено разбнообразие мест для развелечения от 1 до 5\n (1 - без разницы, 5 - жизнено необходимо)', reply_markup=country_migration.ikb_nightLife)
    answer_user['workplace'] = callback_data['action']

async def nightlife(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Оцените насколько важно толерантное отношение к лгбт от 1 до 5\n (1 - без разницы, 5 - жизнено необходимо)', reply_markup=country_migration.ikb_lgbt)
    answer_user['nightlife'] = callback_data['action']

async def lgbt(callback: types.CallbackQuery, callback_data: dict):
    answer_user['lgbt'] = callback_data['action']
    print(answer_user)
    await callback.message.edit_text(text=cm.agent.calculate(answer_user))





def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_миграции'])
    dp.register_callback_query_handler(water_access, country_migration.cb_water.filter())
    dp.register_callback_query_handler(isBig, country_migration.cb_isBig.filter())
    dp.register_callback_query_handler(climat_in_country, country_migration.cb_climat.filter())
    dp.register_callback_query_handler(transport, country_migration.cb_transport.filter())
    dp.register_callback_query_handler(english, country_migration.cb_english.filter())
    dp.register_callback_query_handler(workplace, country_migration.cb_workplace.filter())
    dp.register_callback_query_handler(nightlife, country_migration.cb_nightLife.filter())
    dp.register_callback_query_handler(lgbt, country_migration.cb_lgbt.filter())


