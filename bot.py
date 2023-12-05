import asyncio
from aiogram import Bot, Dispatcher

from config import settings
from data.database import DataBase
import handlers


async def main() -> None:
    bot = Bot(settings['TOKEN'])
    dp = Dispatcher()
    db = DataBase('gaming.db', 'search')
    await db.create_table()
    dp.include_routers(
        handlers.start.router,
        handlers.start_game.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, db=db)

if __name__ == "__main__":
    asyncio.run(main())