from aiogram.dispatcher.filters.state import State,StatesGroup

class List(StatesGroup):
    name_accept= State()
    last_name_accept = State()
    middle_name_accept= State()
    phone_number_accept= State()
    region_accept = State()
    city_accept = State()
    village_accept = State()
    home_number_accept = State()
    birth_day_accept = State()
    tall_accept = State()
    weight_accept = State()
    password_accept = State()
    confirmation=State()

class Topic_add(StatesGroup):
    topic_name = State()
    confirmation_text =State()


class Question_add(StatesGroup):
    topic_id = State()
    question = State()
    option_a = State()
    option_b = State()
    option_c = State()
    option_d = State()
    option_e = State()
    option_f = State()