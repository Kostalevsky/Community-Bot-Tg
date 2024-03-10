import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from helpers import config, helpers

from routers.main_router import main_r
from routers.payment_router import payment
from routers.confirm_router import confirm
from routers.edit_router import edit
from routers.create_router import create


async def main():
    bot = Bot(config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(main_r, payment, confirm, edit, create)

    await bot.set_my_commands(helpers.bot_cmd)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
