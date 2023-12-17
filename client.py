from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from api_token import bot_token
from buttons import *
import requests
from all_clients import all_clients
from main import generate_test, check_answer
import asyncio, json
import os.path




#Инициализация бота
bot = Client(
    "Бот для подготовки к ЕГЭ",
    api_id = 23993649,
    api_hash = '10796da2b5633b606b55d2762ab4b00c',
    bot_token = bot_token
)



#Получение действий пользователя
async def get_client_actions(user_id):
    return all_clients[user_id]


#Обновление действий пользователя
async def update_client_actions(user_id, data):
    all_clients[user_id].append(data)


@bot.on_message(~filters.command('start') & ~filters.command('auth') & ~filters.command('stat'))
async def user_answers(bot, message):
    s = message.reply_to_message.entities[0].url
    if message.text == await check_answer(s):
        await bot.send_message(
            chat_id = message.from_user.id, 
            text = "Молодец, ответ на задание " + s + " верный!", 
        )
    else:
        await bot.send_message(
            chat_id = message.from_user.id, 
            text = "К сожалению, ответ на задание " + s +" неверный(", 
        )


#Получение сообщения /start
@bot.on_message(filters.command('start'))
async def first_mes_reply(bot, message):
    all_clients.update({message.from_user.id: []})
    await bot.send_message(
        chat_id = message.from_user.id, 
        text = "Привет! Тебя приветствует бот по подготовке к ЕГЭ!", 
        reply_markup = InlineKeyboardMarkup(start_buttons)
    )


#Получение команды регистрации
@bot.on_message(filters.command('auth'))
async def first_mes_reply(bot, message):
    all_clients.update({message.from_user.id: []})
    await bot.send_message(
        chat_id = message.from_user.id, 
        text = '''Источник: <a href=\"http://127.0.0.1:8000/api/v1/autth/reg/\">Регистрация</a>''', 
    )


#Получение команды статистики (возможна при регистрации)
@bot.on_message(filters.command('stat_all'))
async def first_mes_reply(bot, message):
    all_clients.update({message.from_user.id: []})
    await bot.send_message(
        chat_id = message.from_user.id, 
        text = '''Источник: <a href=\"http://127.0.0.1:8000/sic/stat\">Статистика всех пользователей</a>''', 
    )


@bot.on_message(filters.command('stat'))
async def first_mes_reply(bot, message):
    all_clients.update({message.from_user.id: []})
    await bot.send_message(
        chat_id = message.from_user.id, 
        text = '''Источник: <a href=\"http://127.0.0.1:8000/sic/stat\">Статистика всех пользователей</a>''', 
    )
# #Получение нажатия кнопки *Выбрать предмет*
# @bot.on_message(filters.regex('Выбрать предмет'))
# async def choose_sub(bot, message):
#     await bot.send_message(
#         chat_id = message.from_user.id, 
#         text = "Выбери интересующий тебя предмет, по которому ты хочешь проверить свои знания", 
#         reply_markup = InlineKeyboardMarkup(choose_sub)
#     )



#Обработка колбэков
@bot.on_callback_query()
async def callback_query(Client, CallbackQuery):
    #Выбрать предмет
    print(CallbackQuery.data)
    if CallbackQuery.data == "Choose subject":
        await update_client_actions(CallbackQuery.from_user.id, {"First_choose" :CallbackQuery.data})
        await CallbackQuery.edit_message_text(
            text = "Выбери интересующий тебя предмет, по которому ты хочешь проверить свои знания", 
            reply_markup = InlineKeyboardMarkup(choose_sub)
        )


    #После выбранного предмета
    if CallbackQuery.data in ('Inf, Math, Eng, Rus, Chem, Phys'):
        await update_client_actions(CallbackQuery.from_user.id, {"subject" :CallbackQuery.data})
        await CallbackQuery.edit_message_text(
            text = "Выбери тему или сгенерируй тест по всем темам по данному предмету", 
            reply_markup = InlineKeyboardMarkup(buttons_aft_choose_s)
        )


    #Выбрать темы
    if CallbackQuery.data == 'Choose theme':
        await update_client_actions(CallbackQuery.from_user.id, {"Second choose" :CallbackQuery.data})
        await CallbackQuery.edit_message_text(
            text = "Выбери тему", 
            reply_markup = InlineKeyboardMarkup(inf_themes)
        )


    #Выбранная тема
    

    #После выбранной темы:
    if 'theme_inf' in CallbackQuery.data:
        await update_client_actions(CallbackQuery.from_user.id, {"theme" :CallbackQuery.data})
        await CallbackQuery.edit_message_text(
            text = "Какое количество вопросов ты хочешь, чтобы было в тесте?", 
            reply_markup = InlineKeyboardMarkup(quantity_choose_t)
        )


    #Генерация теста    
    #Сделать amount, если введено свое количество
    if all(x.isdigit() for x in CallbackQuery.data) or CallbackQuery.data == 'own quantity':
            await update_client_actions(CallbackQuery.from_user.id, {"amount" :CallbackQuery.data})
            await CallbackQuery.edit_message_text(
                text = "Генерируем...", 
            )
            tasks = await generate_test(await get_client_actions(CallbackQuery.from_user.id))
            await CallbackQuery.edit_message_text(
                text = """Итоговый тест:
                          Чтобы дать ответ на задание, введи ответ в ответ на сообщение с ссылкой на задание.""", 
            )
            # tasks = await call_tasks(get_client_actions(CallbackQuery.from_user.id), test)
            for i in tasks:
                #1 задание
                    print(i)
                    await bot.send_message(
                            chat_id = CallbackQuery.from_user.id, 
                            text = i[0]
                    )
                    await bot.send_photo(
                                chat_id = CallbackQuery.from_user.id, 
                            photo = i[1]
                    )


async def main():
    print(Client)

if __name__ == "__main__":
    bot.run()
    asyncio.run(main())