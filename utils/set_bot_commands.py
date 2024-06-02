from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", """ʜɪ ɪ ᴀᴍ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇʀ ʙᴏᴛ
            
            ᴍʏ ᴍᴇᴛʜᴏᴅꜱ :

                    1. ɪɴʟɪɴᴇ 

                    2.ᴅɪʀᴇᴄᴛ ᴍᴇꜱꜱᴀɢᴇ
            """),
            types.BotCommand("help", "to get help"),
            types.BotCommand("about","""ᴡʜʏ ɪ ᴄʀᴇᴀᴛᴇ ᴛʜɪꜱ ʙᴏᴛ ʙᴇᴄᴀᴜꜱᴇ ᴛʜᴇʀᴇ ᴀʀᴇ ᴍᴀɴʏ ᴡᴇʙꜱɪᴛᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ꜰᴏɴᴛꜱ ʙᴜᴛ ᴛʜᴇʏ ᴜꜱᴇ ᴀᴅs, 
            
            ɪᴛ ᴡɪʟʟ ᴍᴀᴋᴇꜱ ᴀɴɴᴏʏɪɴɢ ᴛᴏ ᴇᴠᴇʀʏ ᴏɴᴇ 
            
            ꜱᴏ ɪ ᴍᴀᴋᴇ ᴛʜɪꜱ ᴛʏᴘᴇ ᴏꜰ ʙᴏᴛ
            """
        ]
    )

from aiogram import types

async def start_command(message: types.Message):
    # Create an inline keyboard markup with a button
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="ᴛʀᴜᴍʙᴏᴛꜱ", url="https://t.me/movie_time_botonly")
    keyboard.add(button)

    # Send a message with the text, photo, and inline keyboard
    await message.answer_photo(
        photo="",
        caption="""ʜɪ ɪ ᴀᴍ ꜰᴏɴᴛ ᴄʜᴀɴɢᴇʀ ʙᴏᴛ

        ᴍʏ ᴍᴇᴛʜᴏᴅꜱ :

                1. ɪɴʟɪɴᴇ 

                2.ᴅɪʀᴇᴄᴛ ᴍᴇꜱꜱᴀɢᴇ""",
        reply_markup=keyboard
    )

