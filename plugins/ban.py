from pyrogram import Client, filters

@Client.on_message(filters.command(["ban"]))
async def ban(app, message):
    chatid = message.chat.id
    if message.reply_to_message:
        admins_list = await app.get_chat_members(
            chat_id=chatid, filter="administrators"
        )
        admins = []
        for admin in admins_list:
            id = admin.user.id
            admins.append(id)
        userid = message.from_user.id
        if userid in admins:
            user_to_ban = message.reply_to_message.from_user.id
            if user_to_ban in admins:
                await message.reply(text="Think he is Admin, Can't Ban Admins")
            else:
                try:
                    await app.kick_chat_member(chat_id=chatid, user_id=user_to_ban)
                    await message.reply_text(
                        f"Banned {message.reply_to_message.from_user.mention}Reason:📃 റൂൾ നമ്പർ 7 പ്രകാരം 😊"
                    )
                except Exception as error:
                    await message.reply_text(f"{error}")
        else:
            await message.reply_text("Nice try, But wrong move..")
            return
    else:
        return
