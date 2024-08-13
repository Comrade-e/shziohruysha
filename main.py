import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command

from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types.error_event import ErrorEvent

import mylogger
import time


import saver_reader as sr
import ai
from config import TOKEN

lg = mylogger.MyLogger('info',f'{time.time()}.log')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.error(ExceptionTypeFilter(Exception), F.update.message.as_("message"))
async def handle_my_custom_exception(event: ErrorEvent, message):
    lg.log('error', f'An error occured! {event.exception}')
    await message.answer("Oops, something went wrong!")

@dp.message(CommandStart())
async def cmd_start(message):
    lg.log('info', f'User {message.from_user.id} had started the bot.')
    await message.answer('Это эксперимент "Шизохрюша". /generate <n> - сгенерировать текст по промпту из n случайных '
                         'слов, уже существующих в текстах, хранящихся в памяти. /load <текст> - загрузить текст в память')

@dp.message(Command('generate'))
async def cmd_generate(message):
    amount = int(message.text.split(' ')[-1])
    lg.log('info', f'User {message.from_user.id} requests to generate by {amount}')
    if amount > 350:
        await message.answer('Слишком много!')
    else:
        await message.answer('Генерация...')
        text = await ai.gen('gpt-3.5-turbo', 'Создайте эссе по ключевым словам на русском языке: ' + ' ,'.join(sr.randomwords(amount, 'data.txt')) + 'Текст должен быть тематически однороден')
        await message.answer(text)

@dp.message(Command('load'))
async def cmd_load(message):
    lg.log('info', f'User {message.from_user.id} loads the text.')
    txt = message.text.replace('/load', '')
    sr.save(txt, 'data.txt')
    await message.answer('Ваш текст принят.')

@dp.message(F.text == '_error_')
async def errortest(message):
    await message.answer(str(1/0))



async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        lg.log('critical', f'Error! {str(e)}')


if __name__ == '__main__':
    asyncio.run(main())