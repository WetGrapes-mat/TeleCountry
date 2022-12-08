from aiogram import types, Dispatcher
from create_bot import bot
from neo4j_country_db import country_migration_db
from keybords import country_migration

answer_user = dict()


async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id, text="В разработке")
    except:
        pass


async def members_amount(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Хотите жить в городе где есть выход к морю/океану', reply_markup=country_migration)
    answer_user['washes'] = callback_data['action']


async def child_preschool(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выбирете какой климот хотите', reply_markup=country_migration)
    answer_user['climat'] = callback_data['action']


async def child_school(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Насколько важна комуникация на английском ', reply_markup=country_migration)
    answer_user['communication'] = callback_data['action']


async def smoking(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Развитость общественого транспорта', reply_markup=country_migration)
    answer_user['transport'] = callback_data['action']


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_миграции'])
