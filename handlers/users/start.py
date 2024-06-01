import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.topic_uz import topic_button_uz
from keyboards.inline.lenguages import lenguage_buttun
from keyboards.default.menu_uz import menu_button_uz
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Tillarni tanlang-->\n'
                         f'Выберите языки-->\n'
                         f"Bu bot sizga  kassaliklarni erta aniqlashga va shifoxonalarga yo'naltirishga ko'rsatmalar beradi. \n"
                         f"Этот бот поможет вам выявить случаи заболевания на ранней стадии и направить их в больницы.",reply_markup=lenguage_buttun)




#uz

@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    tg_id = xabar.from_user.id
    url = f'http://api.onko-fergana.uz/user/?id=0&tg_id={tg_id}&page=1&limit=20&status=true'
    headers = {'username': 'string',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTYyMjl9._cHal68WYV101-A6xVD1OPeBhuHdfg8OgAxJvInOdYo'
               }
    files = []
    response1 = requests.request("GET", url, headers=headers, files=files)
    if response1.json()['data'] == []:
        await xabar.message.answer(f"Ro'yxatdan o'tish uchun ro'yxatdan o'tish tugmasiga bosing ",
                                   reply_markup=menu_button_uz)
    else:
        await xabar.message.answer(f"Testlarni ishlashni boshlang",reply_markup=topic_button_uz)




