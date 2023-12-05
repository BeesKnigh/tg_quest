from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.reply import main
from data.database import DataBase

router = Router()


@router.message(CommandStart())
async def start(message: Message, db: DataBase):
    print(db.name)
    await message.answer('Привет! это рпг игра от BeesKnight для квестиков. Нажми на кнопку "start" если хочешь начать игру', reply_markup=main)



