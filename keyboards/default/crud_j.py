from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crud_j_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Get_answer"),
        ],
        [
          KeyboardButton("Bosh menu")
        ]
],
resize_keyboard=True
)