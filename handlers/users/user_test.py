from aiogram import types
import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, callback_query, CallbackQuery
from openpyxl import Workbook

from keyboards.default.topic_uz import topic_button_uz
from loader import dp, bot

url = "http://api.onko-fergana.uz/topic/?id=0&page=1&limit=20&status=true"
headers = {'username':'string',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'
               }
files = []
response1 = requests.request("GET",url,headers=headers,files=files)
@dp.message_handler(text=[i.get('topic_name') for i in response1.json()['data']])
async def bot_start(message: types.Message):
    name = message.text

    url = f"http://api.onko-fergana.uz/topic/?search={name}&id=0&page=1&limit=5&status=true"
    headers = {'username': 'string',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'
               }
    files = []
    response2 = requests.request("GET", url, headers=headers, files=files).json()['data'][0].get('id')



    url = f"http://api.onko-fergana.uz/question/?id=0&topic_id={response2}&page=1&limit=20&status=true"
    headers = {'username': 'string',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'
               }
    files = []
    question_id = requests.request("GET", url, headers=headers, files=files).json()['data'][0].get('id')

    # TEST QISMI



    url = f"http://api.onko-fergana.uz/question/?id={question_id}&topic_id={response2}&page=1&limit=20&status=true"

    headers = {'username': 'string',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'
               }
    files = [

    ]

    response3 = requests.request("GET", url, headers=headers, files=files)
    print(response3.json(), "ffffffffffffffffffffffffffffff333333333333333333")

    for question in response3.json()['data']:
        question_question = question.get('question')
        option_a = question.get('option_a')

        option_b = question.get('option_b')
        option_c = question.get('option_c')
        option_d = question.get('option_d')
        option_e = question.get('option_e')
        option_f = question.get('option_f')
        topic_id = question.get('topic_id')


        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f" {question_question}", callback_data='Savol')],
            [InlineKeyboardButton(text=f" {option_a}", callback_data=f'que1 a {question.get("id")} {topic_id} {1}')],
            [InlineKeyboardButton(text=f" {option_b}", callback_data=f'que2 b {question.get("id")} {topic_id} {2}')],
            [InlineKeyboardButton(text=f" {option_c}", callback_data=f'que3 c {question.get("id")} {topic_id} {3}')],
            [InlineKeyboardButton(text=f" {option_d}", callback_data=f'que4 d {question.get("id")} {topic_id} {4}')],
            [InlineKeyboardButton(text=f" {option_e}", callback_data=f'que5 e {question.get("id")} {topic_id} {5}')],
            [InlineKeyboardButton(text=f" {option_f}", callback_data=f'que6 f {question.get("id")} {topic_id} {6}')]
        ])

        await bot.send_message(chat_id=message.from_user.id, text="Savollarga o'zingizga mos holatni belgilang", reply_markup=keyboard)


















@dp.callback_query_handler()
async def bot_start(xabar: CallbackQuery):
                name = xabar.from_user.first_name
                data1 = xabar.data.split()
                print(name)
                question_id = int(data1[2])
                toopic_id = int(data1[3])



                url = f"http://api.onko-fergana.uz/question/?id={question_id+1}&topic_id={toopic_id}&page=1&limit=20&status=true"

                headers = {'username': 'string',
                           'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'}
                files = [

                ]

                response4 = requests.request("GET", url, headers=headers, files=files)




                if len(response4.json()['data'])<=0:
                    user_id = xabar.from_user.id
                    url = f"http://api.onko-fergana.uz/user/?id=0&tg_id={user_id}&page=1&limit=20&status=true"
                    headers = {'username': 'string',
                               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'
                               }
                    files = [

                    ]
                    response = requests.request("GET", url, headers=headers, files=files)
                    #vaznga qarab natija
                    j = 1
                    wb = Workbook()
                    boy = response.json()['data'][0].get('tall')
                    vazn = response.json()['data'][0].get('weight')
                    i = (vazn) / (boy * boy / 10000)
                    if i <= 16:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Tana vazningiz haddan ziyod kam ko'rsatkichda. Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "
                    elif 16 < i <= 18.5:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Tana vazningiz yetarli emas . Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "
                    elif 18.5 < i <= 25:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Tana vazningiz yetarli miqdorda. Xar 6 oyda Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "
                    elif 25 < i <= 30:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Ortiqcha tana vazni mavjud. Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "
                    elif 30 < i <= 35:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Semirishning 1-darajasi . Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "

                    elif 35 < i <= 40:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Semirishning 1-darajasi . Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "
                    else:
                        x = f" Massa indeksingiz quyidagi {i}   ko'rsatgichda. Semirishning 1-darajasi . Dietolog va Terapevt  shifokorlariga uchrashingiz so'raladi. O'z sog'lig'ingiz o'z qo'lingizda "


                    for user in response.json()['data']:
                        user_name = user.get('name')
                        user_last_name = user.get('last_name')
                        user_middle_name = user.get('middle_name')
                        user_tall = user.get('tall')
                        user_weight = user.get('weight')
                        user_phone_number = user.get('phone_number')
                        user_region = user.get('region')
                        user_city = user.get('city')
                        user_village = user.get('village')
                        user_birth_day = user.get('birth_day')
                        user_home_number = user.get('home_number')
                        tg_id = user.get('tg_id')




                        url = f"http://api.onko-fergana.uz/answer/?id=0&user_id={tg_id}&topic_id={toopic_id}&question_id=0&page=1&limit=18&status=true"
                        headers = {'username': 'string',
                                   'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw'
                                   }
                        files = [

                        ]
                        response = requests.request("GET", url, headers=headers, files=files)


                        for answers in response.json()['data']:
                            user_answer = answers.get('answer')

                            question = answers.get('questions')
                            user_question = question.get('question')

                            topic = answers.get('topic')
                            user_topic = topic.get('topic_name')




                            # exel fayl

                            sheet = wb.active
                            sheet['A1'] = "Ism"
                            sheet['A2'] = user_name

                            sheet['B1'] = "Familya"
                            sheet['B2'] = user_last_name

                            sheet['C1'] = "Otasini ismi"
                            sheet['C2'] = user_middle_name

                            sheet['D1'] = "Boy uzunligi"
                            sheet['D2'] = user_tall

                            sheet['F1'] = "Tana og'irligi"
                            sheet['F2'] = user_weight



                            sheet['E1'] = "Tug'ilgan kun/oy/yil"
                            sheet['E2'] = user_birth_day



                            sheet['G1'] = "Telefon_nomer"
                            sheet['G2'] = user_phone_number

                            sheet['H1'] = "Xudud"
                            sheet['H2'] = user_region

                            sheet['I1'] = "Tuman/Shaxar"
                            sheet['I2'] = user_city

                            sheet['J1'] = "Qishloq"
                            sheet['J2'] = user_village

                            sheet['K1'] = "Uy raqami"
                            sheet['K2'] = user_home_number

                            sheet['L1'] = "Savol turi"
                            sheet[f'L{j}'] = user_topic

                            sheet['M1'] = "Savol"
                            sheet[f'M{j}'] = user_question

                            sheet['N1'] = "Javob"
                            sheet[f'N{j}'] = user_answer



                            j += 1

                        wb.save(f'{name}.xlsx')


                    with open(f'{name}.xlsx', 'rb') as file:
                     await xabar.message.answer_document(file)




                    await xabar.message.reply(text=f" {x}. Bunday so'rovnomalardan o'tishingiz o'z sog'lig'ingiz haqida qayg'urish demakdir. ",
                        reply_markup=topic_button_uz)

                else:

                    for question in response4.json()['data']:
                        question_question = question.get('question')
                        option_a = question.get('option_a')
                        topic = question.get('topic')["topic_name"]



                        topic_name=topic
                        qustion_name=question_question



                        option_b = question.get('option_b')
                        option_c = question.get('option_c')
                        option_d = question.get('option_d')
                        option_e = question.get('option_e')
                        option_f = question.get('option_f')
                        topic_id = question.get('topic_id')
                        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text=f" {question_question}", callback_data='Savol')],
                            [InlineKeyboardButton(text=f" {option_a}",
                                                  callback_data=f'que1 a {question.get("id")} {topic_id} {1} ')],
                            [InlineKeyboardButton(text=f" {option_b}",
                                                  callback_data=f'que2 b {question.get("id")} {topic_id} {2} ')],
                            [InlineKeyboardButton(text=f" {option_c}",
                                                  callback_data=f'que3 c {question.get("id")} {topic_id} {3} ')],
                            [InlineKeyboardButton(text=f" {option_d}",
                                                  callback_data=f'que4 d {question.get("id")} {topic_id} {4} ')],
                            [InlineKeyboardButton(text=f" {option_e}",
                                                  callback_data=f'que5 e {question.get("id")} {topic_id} {5} ')],
                            [InlineKeyboardButton(text=f" {option_f}",
                                                  callback_data=f'que6 f {question.get("id")} {topic_id} {6} ')]
                        ])






                        if data1[0] == 'que1':
                            answer_an =1
                            answer_a = option_a
                            user_id = xabar.from_user.id
                            topic_id = topic_id
                            question_id = data1[2]


                            url = 'http://api.onko-fergana.uz/answer/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data = {
                                "answer": answer_a,
                                "user_id": user_id,
                                "topic_id": topic_id,
                                "question_id": question_id
                            }
                            # API ga POST so'rovni jo'natish
                            responsea = await bot.session.post(url, headers=headers, json=data)
                            result = await responsea.json()


                            # statistika uchun
                            url = 'http://api.onko-fergana.uz/statistika/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data2 = {
                                "topic_id": topic_id,
                                "question_id": question_id,
                                "topic_name": topic_name,
                                "question_name": qustion_name,
                                "answer_a": answer_an
                            }
                            # API ga POST so'rovni jo'natish
                            responsean = await bot.session.post(url, headers=headers, json=data2)
                            result = await responsean.json()
                            # API javobini ko'rsatish
                            await xabar.message.reply(result["detail"], reply_markup=keyboard)














                        elif data1[0] == 'que2':
                            answer_bn =1
                            answer_b = option_b
                            user_id = xabar.from_user.id
                            topic_id = topic_id
                            question_id = data1[2]

                            url = 'http://api.onko-fergana.uz/answer/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data = {
                                "answer": answer_b,
                                "user_id": user_id,
                                "topic_id": topic_id,
                                "question_id": question_id
                            }
                            # API ga POST so'rovni jo'natish
                            responsea = await bot.session.post(url, headers=headers, json=data)
                            result = await responsea.json()

                            # statistika uchun
                            url = 'http://api.onko-fergana.uz/statistika/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data2 = {
                                "topic_id": topic_id,
                                "question_id": question_id,
                                "topic_name": topic_name,
                                "question_name": qustion_name,
                                "answer_b": answer_bn
                            }
                            # API ga POST so'rovni jo'natish
                            responsean = await bot.session.post(url, headers=headers, json=data2)
                            result = await responsean.json()
                            # API javobini ko'rsatish
                            await xabar.message.reply(result["detail"], reply_markup=keyboard)



                        elif data1[0] == 'que3':
                            answer_cn = 1
                            answer_c = option_c
                            user_id = xabar.from_user.id
                            topic_id = topic_id
                            question_id = data1[2]

                            url = 'http://api.onko-fergana.uz/answer/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data = {
                                "answer": answer_c,
                                "user_id": user_id,
                                "topic_id": topic_id,
                                "question_id": question_id
                            }
                            # API ga POST so'rovni jo'natish
                            responsea = await bot.session.post(url, headers=headers, json=data)
                            result = await responsea.json()

                            # statistika uchun
                            url = 'http://api.onko-fergana.uz/statistika/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data2 = {
                                "topic_id": topic_id,
                                "question_id": question_id,
                                "topic_name": topic_name,
                                "question_name": qustion_name,
                                "answer_c": answer_cn
                            }
                            # API ga POST so'rovni jo'natish
                            responsean = await bot.session.post(url, headers=headers, json=data2)
                            result = await responsean.json()

                            # API javobini ko'rsatish
                            await xabar.message.reply(result["detail"], reply_markup=keyboard)

                        elif data1[0] == 'que4':
                            answer_dn = 1
                            answer_d = option_d
                            user_id = xabar.from_user.id
                            topic_id = topic_id
                            question_id = data1[2]

                            url = 'http://api.onko-fergana.uz/answer/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data = {
                                "answer": answer_d,
                                "user_id": user_id,
                                "topic_id": topic_id,
                                "question_id": question_id
                            }
                            # API ga POST so'rovni jo'natish
                            responsea = await bot.session.post(url, headers=headers, json=data)
                            result = await responsea.json()

                            # statistika uchun
                            url = 'http://api.onko-fergana.uz/statistika/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data2 = {
                                "topic_id": topic_id,
                                "question_id": question_id,
                                "topic_name": topic_name,
                                "question_name": qustion_name,
                                "answer_d": answer_dn
                            }
                            # API ga POST so'rovni jo'natish
                            responsean = await bot.session.post(url, headers=headers, json=data2)
                            result = await responsean.json()

                            # API javobini ko'rsatish
                            await xabar.message.reply(result["detail"], reply_markup=keyboard)

                        elif data1[0] == 'que5':
                            answer_en = 1
                            answer_e = option_e
                            user_id = xabar.from_user.id
                            topic_id = topic_id
                            question_id = data1[2]

                            url = 'http://api.onko-fergana.uz/answer/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data = {
                                "answer": answer_e,
                                "user_id": user_id,
                                "topic_id": topic_id,
                                "question_id": question_id
                            }
                            # API ga POST so'rovni jo'natish
                            responsea = await bot.session.post(url, headers=headers, json=data)
                            result = await responsea.json()

                            # statistika uchun
                            url = 'http://api.onko-fergana.uz/statistika/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data2 = {
                                "topic_id": topic_id,
                                "question_id": question_id,
                                "topic_name": topic_name,
                                "question_name": qustion_name,
                                "answer_e": answer_en
                            }
                            # API ga POST so'rovni jo'natish
                            responsean = await bot.session.post(url, headers=headers, json=data2)
                            result = await responsean.json()
                            # API javobini ko'rsatish
                            await xabar.message.reply(result["detail"], reply_markup=keyboard)



                        elif data1[0] == 'que6':
                            answer_fn = 1
                            answer_f = option_f
                            user_id = xabar.from_user.id
                            topic_id = topic_id
                            question_id = data1[2]

                            url = 'http://api.onko-fergana.uz/answer/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data = {
                                "answer": answer_f,
                                "user_id": user_id,
                                "topic_id": topic_id,
                                "question_id": question_id
                            }
                            # API ga POST so'rovni jo'natish
                            responsea = await bot.session.post(url, headers=headers, json=data)
                            result = await responsea.json()

                            # statistika uchun
                            url = 'http://api.onko-fergana.uz/statistika/add'
                            headers = {
                                'accept': 'application/json',
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjIyMzMyMTY2Mzh9.EG_mnwMWqXONkaZw-wRKJzByY9WDBVnk0w4qLSEF8tw',
                                'Content-Type': 'application/json'
                            }
                            data2 = {
                                "topic_id": topic_id,
                                "question_id": question_id,
                                "topic_name": topic_name,
                                "question_name": qustion_name,
                                "answer_f": answer_fn
                            }
                            # API ga POST so'rovni jo'natish
                            responsean = await bot.session.post(url, headers=headers, json=data2)
                            result = await responsean.json()

                            # API javobini ko'rsatish
                            await xabar.message.reply(result["detail"], reply_markup=keyboard)

                        else:
                            await xabar.message.answer(text="Qayta urining xato javob yo'lladingiz")

