import logging

from aiogram import Dispatcher

from data.config import ADMINS
import datetime

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            current_datetime = datetime.datetime.now()
            date_time_str = current_datetime.strftime("%d/%m/%Y %H:%M:%S")

            await dp.bot.send_message(admin, f"Bot Started at {date_time_str}")

        except Exception as err:
            pass
            # logging.exception(err)
