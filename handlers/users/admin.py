from aiogram import types
from keyboards.default.crud_j import crud_j_button
from keyboards.default.crud_m import crud_m_button
from keyboards.default.crud_s import crud_s_button
from loader import dp
from keyboards.default.menu_admin import menu_button_admin
from keyboards.default.crud_f import crud_f_button
from keyboards.inline.lenguages import lenguage_buttun

@dp.message_handler(commands='admin' ,chat_id= '1961871634')
async def bot_start(message: types.Message):
     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_button_admin)

# menu

@dp.message_handler(text="Foydalanuvchilar")
async def bot_start(message: types.Message):
     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=crud_f_button)



@dp.message_handler(text="Javoblar")
async def bot_start(message: types.Message):
     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=crud_j_button)

@dp.message_handler(text="Mavzular")
async def bot_start(message: types.Message):
     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=crud_m_button)


@dp.message_handler(text="Savollar")
async def bot_start(message: types.Message):
     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=crud_s_button)


#orqaga
@dp.message_handler(text="Bosh menu")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_button_admin)



