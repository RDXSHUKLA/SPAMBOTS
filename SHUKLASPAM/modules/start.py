from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10
from SHUKLASPAM.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", data="help_back")
        ],
        [
        Button.url("𝗖𝗛𝗔𝗡𝗡𝗘𝗟", "https://t.me/SHIVANSH474"),
        Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/MASTIWITHFRIENDSXD")
        ],
        [
        Button.url("𝗥𝗘𝗣𝗢", "https://github.com/itzshukla/STRANGER-SPAM-X/fork")
        ]
        ]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝗛𝗘𝗬 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠  [{BotName}](tg://user?id={BotId})**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 𝗕𝗬 :~ [𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛](https://t.me/SHIVANSH39)**\n\n"
        TEXT += f"» **𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗦𝗣𝗔𝗠 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `3.2`\n"
        TEXT += f"» **𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://graph.org/file/c6a2ed96648fd03377dc9.jpg",
                caption=TEXT, 
                buttons=PythonButton)