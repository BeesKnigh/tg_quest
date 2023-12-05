from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData





class Attacking(CallbackData, prefix='atk'):
    action: str
    turn: int


def attack(turn: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Удар в голову', callback_data=Attacking(action='Head', turn=3).pack()),
        InlineKeyboardButton(text='Удар в тело', callback_data=Attacking(action='Body', turn=2).pack()),
        InlineKeyboardButton(text='Удар в голову', callback_data=Attacking(action='Legs', turn=1).pack()),
    )
    return builder.as_markup()


class Defense(CallbackData, prefix='def'):
    action: str
    turn: int


def defense(turn: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Защита головы', callback_data=Defense(action='Def_head', turn=3).pack()),
        InlineKeyboardButton(text='Защита тела', callback_data=Defense(action='Def_body', turn=2).pack()),
        InlineKeyboardButton(text='Защита ног', callback_data=Defense(action='Def_legs', turn=1).pack()),
    )
    return builder.as_markup()