import states.situations
from keyboards.default.confirmation_button import tasdiqlash_button
from keyboards.default.topic_uz import topic_button_uz
from keyboards.default.menu_uz import menu_button_uz
from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.situations import *

# add_user

@dp.message_handler(text="Ro'yxatdan o'tish")
async def bot_echo(message: types.Message):

#ism
     await message.answer(text="Ismingizni Kiriting--> ",reply_markup=ReplyKeyboardRemove())
     await List.name_accept.set()
@dp.message_handler(state=List.name_accept)
async def bot_echo(message: types.Message,state:FSMContext):
     name = message.text
     await state.update_data({'name':name})

#fam

     await message.answer(text="Familyani  Kiriting--> ")
     await List.last_name_accept.set()
@dp.message_handler(state=List.last_name_accept)
async def bot_echo(message: types.Message,state:FSMContext):
     last_name = message.text
     await state.update_data({'fam':last_name})

#Ota
     await message.answer(text="Sharifingizni kiriting--> ")
     await List.middle_name_accept.set()
@dp.message_handler(state=List.middle_name_accept)
async def bot_echo(message: types.Message,state:FSMContext):
     middle_name = message.text
     await state.update_data({'middle_name': middle_name})

#number

     await message.answer(text="Telefon nomeringizni   kiriting--> ")
     await List.phone_number_accept.set()
@dp.message_handler(state=List.phone_number_accept)
async def bot_echo(message: types.Message,state:FSMContext):
     phone_number = message.text.strip()
     if not phone_number.isdigit():
         await message.answer("Iltimos, telefon raqamingizni to'g'ri ko'rinishda kiriting (999932567)")
         return

     await state.update_data(phone_number=phone_number)
     await List.next()

#viloyat
     await message.answer(text="Viloyatingizni kiriting --> ")
     await List.region_accept.set()
@dp.message_handler(state=List.region_accept)
async def bot_echo(message: types.Message,state:FSMContext):
     region = message.text
     await state.update_data({'region': region})
#tuman

     await message.answer(text="Shahar yoki Tumaningizni kiriting --->  ")
     await List.city_accept.set()
@dp.message_handler(state=List.city_accept)
async def bot_echo(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data({'city': city})

#qishloq

    await message.answer(text="MFY yoki QFY nomini kiriting--> ")
    await List.village_accept.set()
@dp.message_handler(state=List.village_accept)
async def bot_echo(message: types.Message, state: FSMContext):
    village = message.text
    await state.update_data({'village': village})

#home number
    await message.answer(text="Uy raqamingizni kiriting--> ")
    await List.home_number_accept.set()
@dp.message_handler(state=List.home_number_accept)
async def bot_echo(message: types.Message, state: FSMContext):
    home_number = message.text
    if not home_number.isdigit():
        await message.answer("Iltimos, Uy raqamingizni faqat son  ko'rinishda kiriting (Masalan: 2 )")
        return

    await state.update_data(home_number=home_number)
    await List.next()


#age
    await message.answer(text="Tug'ilgan kun/oy/yil kiriting--> ")
    await List.birth_day_accept.set()
@dp.message_handler(state=List.birth_day_accept)
async def bot_echo(message: types.Message, state: FSMContext):
    birth_day = message.text
    await state.update_data({'birth_day': birth_day})

#tall
    await message.answer(text="Bo'yingiz uzunligini kiriting(Masalan: 175 )--> ")
    await List.tall_accept.set()
@dp.message_handler(state=List.tall_accept)
async def bot_echo(message: types.Message, state: FSMContext):
    tall = message.text
    if not tall.isdigit():
        await message.answer("Iltimos, Bo'yingiz uzunligini faqat son  ko'rinishda kiriting (Masalan: 175 )")
        return

    await state.update_data(tall=tall)
    await List.next()

#weight
    await message.answer(text="Vazningizni kiriting (Masalan: 68 )--> ")
    await List.weight_accept.set()
@dp.message_handler(state=List.weight_accept)
async def bot_echo(message: types.Message, state: FSMContext):
    weight = message.text
    if not weight.isdigit():
        await message.answer("Iltimos, Tanangiz og'irligini faqat son  ko'rinishda kiriting (Masalan: 55 )")
        return

    await state.update_data(weight=weight)
    await List.next()

#password
    await message.answer(text="Shaxsiy kabinetingiz uchunparol kiriting--> ")
    await List.password_accept.set()
@dp.message_handler(state=List.password_accept)
async def bot_echo(message: types.Message,state:FSMContext):
     password = message.text
     await state.update_data({'password':password})
     information = await state.get_data()

     name = information.get("name")
     last_name = information.get("last_name")
     middle_name = information.get("middle_name")
     phone_number = information.get("phone_number")
     region = information.get("region")
     city = information.get("city")
     village = information.get("village")
     home_number = information.get("home_number")
     birth_day = information.get("birth_day")
     tall = information.get("tall")
     weight = information.get("weight")
     password =information.get("password")



     s = f"Ismi : {name}\n" \
         f"Familyasi : {last_name}\n" \
         f"Sharifi : {middle_name}\n" \
         f"Tel_nomeri: {phone_number}\n" \
         f"Viloyati : {region}\n" \
         f"Shaxar/Tuman : {city}\n" \
         f"MFY/QFY : {village}\n" \
         f"Uy nomeri : {home_number}\n" \
         f"Tug'ilgan kun/oy/yil : {birth_day}\n" \
         f"Bo'y uzunligi : {tall}\n" \
         f"Tana og'irligi : {weight}\n"\
         f"Parolingiz : {password}\n"\


     await bot.send_message(chat_id=message.from_id,text=s,reply_markup=tasdiqlash_button)
     await List.confirmation.set()


@dp.message_handler(state=List.confirmation,text="Ma'lumotni jonatish")
async def bot_echo(message: types.Message,state:FSMContext):
    tg_id = message.from_id
    information = await state.get_data()
    name = information.get("name")
    last_name = information.get("last_name")
    middle_name = information.get("middle_name")
    phone_number = information.get("phone_number")
    region = information.get("region")
    city = information.get("city")
    village = information.get("village")
    home_number = information.get("home_number")
    birth_day = information.get("birth_day")
    tall = information.get("tall")
    weight = information.get("weight")
    password = information.get("password")
    user_id = tg_id






    # Ma'lumotlarni API ga jo'natish
    url = 'http://api.onko-fergana.uz/user/add'
    headers = {
        'accept': 'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
        'Content-Type': 'application/json'
    }
    data = {
        "name": name,
        "last_name": last_name,
        "middle_name": middle_name,
        "phone_number": phone_number,
        "region": region,
        "city": city,
        "village": village,
        "home_number": home_number,
        "birth_day": birth_day,
        "tall": tall,
        "weight": weight,
        "password":password,
        "tg_id":tg_id


    }
    # API ga POST so'rovni jo'natish
    response = await bot.session.post(url, headers=headers, json=data)
    result = await response.json()

    # API javobini ko'rsatish
    await message.reply(result)
    await bot.send_message(chat_id=tg_id, text="Muvofaqiyatli ro'yxatdan o'tdingiz",reply_markup=topic_button_uz)
    await state.finish()

@dp.message_handler(state=List.confirmation,text='Bekor qilish')
async def bot_echo(message: types.Message,state:FSMContext):
     await bot.send_message(chat_id=message.from_user.id,text='Bekor qilish',reply_markup=menu_button_uz)
     await state.finish()