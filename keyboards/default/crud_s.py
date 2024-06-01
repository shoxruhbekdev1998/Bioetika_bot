from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crud_s_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Get_question"),
            KeyboardButton("Add_question")
        ],
        [
          KeyboardButton("Bosh menu")
        ]
],
resize_keyboard=True
)