
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import InlineKeyboardButton,inline_keyboard,InlineKeyboardMarkup

bot = Bot(token=api_token)
dp=Dispatcher(bot)


btn1 = InlineKeyboardButton("photo",callback_data="photo")
keyboard_bt1 = InlineKeyboardMarkup(row_width=1).add(btn1)
@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer("sdsdsdsdsds",reply_markup=keyboard_bt1)


@dp.callback_query_handler()
async def center(call:types.CallbackQuery):
    if call.data =="photo":
        file = open("Untitled-2.jpg","rb")
        await call.message.answer_photo(photo=file)



if __name__=="__main__":
    executor.start_polling(dp)
