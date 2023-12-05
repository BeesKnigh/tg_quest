from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='start_game'),
            KeyboardButton(text='stat')
        ]
    ], resize_keyboard=True, one_time_keyboard=True,
)

go_gaming = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Готов!'),
            KeyboardButton(text='Не готов!')
        ]
    ], resize_keyboard=True, one_time_keyboard=True,
)