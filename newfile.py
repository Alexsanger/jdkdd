import os
import openai
import re
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = "6167795888:AAH0mveMSDe7SsGGYH_FOXQjgE-lNgTWBnI"
openai.api_key = "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"

bot = Bot(token)
dp = Dispatcher(bot)
print("Bot Ready")


async def get_bot_username():
  user = await dp.bot.me
  return user.username


@dp.message_handler()
async def send(message: types.Message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
  )
  bot_username = await get_bot_username()
  if re.search(fr"@{bot_username}\b", message.text, re.IGNORECASE):

    print(response)
    #await message.answer(response['choices'][0]['text'])
    await bot.send_message(chat_id=message.chat.id,
                           text=response['choices'][0]['text'])
 


#// НИКОГДА НЕ ЗАСЫПАЕТ, ЧТО БЫ НЕ БЫЛО ТУТ

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
