from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
lenguage_buttun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data="til1"),
            InlineKeyboardButton(text="Rus tili",callback_data="til2")

        ]
   ]
)