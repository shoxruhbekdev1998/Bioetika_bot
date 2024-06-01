from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Foydalanuvchilar"),
            KeyboardButton("Javoblar")

        ],

[
            KeyboardButton("Mavzular"),
            KeyboardButton("Savollar")

        ],
],
resize_keyboard=True
)