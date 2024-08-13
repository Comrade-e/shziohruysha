import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command

import mylogger


import saver_reader as sr
import ai
from config import TOKEN

lg = mylogger.MyLogger('info','main.log')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message):
    print(lg)
    lg.log('info', f'User {message.from_user.id} had started the bot.')
    await message.answer('Это эксперимент "Шизохрюша". /generate <n> - сгенерировать текст по промпту из n случайных '
                         'слов, уже существующих в текстах, хранящихся в памяти. /load <текст> - загрузить текст в память')

@dp.message(Command('generate'))
async def cmd_generate(message):
    amount = int(message.text.split(' ')[-1])
    print(amount)
    if amount > 350:
        await message.answer('Слишком много!')
    else:
        await message.answer('Генерация...')
        text = await ai.gen('command-r+', 'Создайте эссе по ключевым словам на русском языке: ' + ' ,'.join(sr.randomwords(amount, 'data.txt')) + 'Текст должен быть тематически однороден')
        await message.answer(text)

@dp.message(Command('load'))
async def cmd_load(message):
    txt = message.text.replace('/load', '')
    sr.save(txt, 'data.txt')
    await message.answer('Ваш текст принят.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())