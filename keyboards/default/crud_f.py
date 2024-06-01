from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crud_f_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Get_user"),
            KeyboardButton("Add_user")

        ],
        [
          KeyboardButton("Bosh menu")
        ]
],
resize_keyboard=True
)