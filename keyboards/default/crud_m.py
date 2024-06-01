from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crud_m_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Get_topic"),
            KeyboardButton("Add_topic")

        ],
        [
          KeyboardButton("Bosh menu")
        ]
],
resize_keyboard=True
)