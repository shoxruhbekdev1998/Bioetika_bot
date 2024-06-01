from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

topic_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Testni tanlash"),

        ],
],
resize_keyboard=True
)


from aiogram import types
import requests
from loader import dp

@dp.message_handler(text="Testni tanlash")
async def bot_start(message: types.Message):
    url = "https://bioetika.onrender.com/topic/?id=0&page=1&limit=5"
    headers = {'username':'string',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzEzMzAzMTh9.O_Egv0M5rc56jemzjYAxTDNJGAzsdiUggznmnuXPwWM'
               }
    files = [

    ]
    response = requests.request("GET",url,headers=headers,files=files)
    print(response.json(),"ffffffffffffffffffffffffffffff")

    # for t in response.json()['data'][0]:
    #     print(t)
    #     # for x in t.get('topic_name'):
    #     #     print(x,"________________")


    l=[]
    for topics in response.json()['data']:
         topic_name=topics.get('topic_name')
         l.append(topic_name)
         index = 0
         i = 0
         royxat = []
         for menu in l:
             if i % 2 == 0 and i != 0:
                 index += 1
             if i % 2 == 0:
                 royxat.append([KeyboardButton(text=menu)])
             else:
                 royxat[index].append(KeyboardButton(text=menu))
             i += 1

         topic_buttun = ReplyKeyboardMarkup(keyboard=royxat, resize_keyboard=True)

    await message.answer(
        text="Test mavzularini tanglang", reply_markup=topic_buttun)

