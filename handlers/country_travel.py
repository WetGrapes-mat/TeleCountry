from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto
from create_bot import bot
from agents import country_travel as ct
from keybords import country_travel
#
answer = dict()
#
#
# async def command(message: types.Message) -> None:
#     try:
#         await bot.send_message(message.from_user.id,
#                                text="Сейчас мы подберём Вам страну для путешествия. Выберите тип путешествия, который вам больше всего подходит.",
#                                reply_markup=country_travel.ikb_type)
#     except:
#         pass
#
#
# async def type_answer(callback: types.CallbackQuery, callback_data: dict):
#     await callback.message.edit_text(text='Выберите страну из списка:', reply_markup=country_travel.ikb_countries)
#     answer['type'] = callback_data['action']
#
#
# async def countries_answer(callback: types.CallbackQuery, callback_data: dict):
#     answer['country'] = callback_data['action']
#     if answer['type'] == 'Beach Holidays':
#         links, txt = ct.resorts_agent.find1(answer)
#         media = list()
#         for link in links:
#             media.append(InputMediaPhoto(link))
#         await callback.message.delete()
#         await bot.send_media_group(callback.message.chat.id, media)
#         await bot.send_message(callback.message.chat.id, txt)
#     elif answer['type'] == 'Ski Resort Holidays':
#         links, txt = ct.resorts_agent.find2(answer)
#         media = list()
#         for link in links:
#             media.append(InputMediaPhoto(link))
#         await callback.message.delete()
#         await bot.send_media_group(callback.message.chat.id, media)
#         await bot.send_message(callback.message.chat.id, txt)
#     elif answer['type'] == 'Tourism trip':
#         links, txt = ct.resorts_agent.find3(answer)
#         media = list()
#         for link in links:
#             media.append(InputMediaPhoto(link))
#         await callback.message.delete()
#         await bot.send_media_group(callback.message.chat.id, media)
#         await bot.send_message(callback.message.chat.id, txt)
#
#
# def register_handlers(dp: Dispatcher):
#     dp.register_message_handler(command, commands=['Страна_для_путешествия'])
#     dp.register_callback_query_handler(type_answer, country_travel.cb_type.filter())
#     dp.register_callback_query_handler(countries_answer, country_travel.cb_countries.filter())

async def command(message: types.Message) -> None:
    try:
        await bot.send_message(message.from_user.id,
                               text="Сейчас мы подберём Вам страну для путешествия. Выберите тип путешествия, который вам больше всего подходит.",
                               reply_markup=country_travel.ikb_type)
    except:
        pass


async def type_answer(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.edit_text(text='Выберите страну из списка:', reply_markup=country_travel.ikb_countries)
    answer['type'] = callback_data['action']


async def countries_answer(callback: types.CallbackQuery, callback_data: dict):
    answer['country'] = callback_data['action']
    if answer['type'] == 'Beach Holidays':
        links, txt = ct.resorts_agent.find1(answer)
        media = list()
        for link in links:
            media.append(InputMediaPhoto(link))
        await callback.message.delete()
        await bot.send_media_group(callback.message.chat.id, media)
        await bot.send_message(callback.message.chat.id, txt)
    elif answer['type'] == 'Ski Resort Holidays':
        links, txt = ct.resorts_agent.find2(answer)
        media = list()
        for link in links:
            media.append(InputMediaPhoto(link))
        await callback.message.delete()
        await bot.send_media_group(callback.message.chat.id, media)
        await bot.send_message(callback.message.chat.id, txt)
    elif answer['type'] == 'Tourism trip':
        links, txt = ct.resorts_agent.find3(answer)
        media = list()
        for link in links:
            media.append(InputMediaPhoto(link))
        await callback.message.delete()
        await bot.send_media_group(callback.message.chat.id, media)
        await bot.send_message(callback.message.chat.id, txt)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command, commands=['Страна_для_путеществия'])
    dp.register_callback_query_handler(type_answer, country_travel.cb_type.filter())
    dp.register_callback_query_handler(countries_answer, country_travel.cb_countries.filter())