from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from utils.states import Round
import keyboards.inline
from data.database import DataBase
router = Router()

from keyboards.reply import go_gaming
from aiogram.types.callback_query import CallbackQuery
from keyboards.inline import Attacking, Defense


@router.message(F.text.lower() == "start_game")
async def game(message: Message):
    print('hell1o')
    db = DataBase('gaming.db', 'search')
    db_p = DataBase('gaming.db', 'players')
    db_g = DataBase('gaming.db', 'game')
    await db.register_pl(message.from_user.id)
    await message.answer('Начался поиск оппонента, ожидайте!')
    if await db.count_pl() >= 2:

        await db_p.add_to_game()
        await db.delete_in_search()
        await message.answer('Соперник найден! Бой начался! Если ты готов, то нажми на кнопку снизу!'
                             , reply_markup=go_gaming)
        print(await db_p.get_user_id())


@router.message(F.text.lower() == "готов!")
async def game(message: Message):
    await message.answer('жмай', reply_markup=keyboards.inline.attack())

@router.callback_query(Attacking.filter(F.action == 'Head'))
async def head(message: Message, call: CallbackQuery, callback_data: keyboards.inline.Attacking):
    await call.message.answer('Ты выбрал "Ударить в голову", жди пока твой соперник сделает ход')
    db_g = DataBase('gaming.db', 'game')
    health = db_g.last_health(message.from_user.id)
    session_id = ...
    round_id = await int(db_g.select_rounds(КАКОЙ-ТО СЕССИОН АЙДИ)) // 2 + 1
    print(round_id)
    await db_g.round_game(message.from_user.user_id, round_id, 0, 3, health, )

@router.callback_query(Attacking.filter(F.action == 'Body'))
async def body(message: Message, call: CallbackQuery, callback_data: keyboards.inline.Attacking):
    await call.message.answer('Ты выбрал "Ударить в тело", жди пока твой соперник сделает ход')
    db_g = DataBase('gaming.db', 'game')
    health = db_g.last_health(message.from_user.id)
    session_id = ...
    round_id = await int(db_g.select_rounds(КАКОЙ-ТО СЕССИОН АЙДИ)) // 2 + 1
    print(round_id)
    await db_g.round_game(message.from_user.user_id, round_id, 0, 2, health, )

@router.callback_query(Attacking.filter(F.action == 'Legs'))
async def legs(message: Message, call: CallbackQuery, callback_data: keyboards.inline.Attacking):
    await call.message.answer('Ты выбрал "Ударить в ноги", жди пока твой соперник сделает ход')
    db_g = DataBase('gaming.db', 'game')
    health = db_g.last_health(message.from_user.id)
    session_id = ...
    round_id = await int(db_g.select_rounds(КАКОЙ-ТО СЕССИОН АЙДИ)) // 2 + 1
    print(round_id)
    await db_g.round_game(message.from_user.user_id, round_id, 0, 1, health, )


@router.message(F.text.lower() == "не готов!")
async def game(message: Message):
    await message.answer('жмай', reply_markup=keyboards.inline.defense())


@router.callback_query(Defense.filter(F.action == 'Def_legs'))
async def def_legs(call: CallbackQuery, callback_data: keyboards.inline.Defense):
    await call.message.answer('ты защитил ноги')
    db_g = DataBase('gaming.db', 'game')
    await db_g.insert_legs_def()

@router.callback_query(Defense.filter(F.action == 'Def_body'))
async def def_body(call: CallbackQuery, callback_data: keyboards.inline.Defense):
    await call.message.answer('ты защитил тело')


@router.callback_query(Defense.filter(F.action == 'Def_head'))
async def def_head(call: CallbackQuery, callback_data: keyboards.inline.Defense):
    await call.message.answer('ты защитил голову')

import dataclasses


@dataclasses.dataclass
class AttackAction:
    action_id: int
    name: str

@dataclasses.dataclass
class DefAction:
    action_id: int
    name: str
    counteraction: AttackAction


actions = [DefAction(0, 'Защита рукой', AttackAction(0, 'Удар рукой'))]

action_dict = {}

for i in actions:
    action_dict.update({i.name: i.counteraction.name})

print(action_dict.get('Защита рукой'))
print(action_dict.get('Защита ногой'))
