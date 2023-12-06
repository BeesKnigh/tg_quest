from aiogram.fsm.state import StatesGroup, State


class Round(StatesGroup):
    user_id = State()
    round_id = State()
    step = State()
    health = State()