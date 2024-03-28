# © @SHIVANSH474
from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 •", data="help_back")
    ],
    [
        Button.url("•  𝗖𝗛𝗔𝗡𝗡𝗘𝗟 •", "https://t.me/SHIVANSH474"),
        Button.url("• 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 •", "https://t.me/mastiwithfriendsx")
    ],
    [
        Button.url("• 𝗥𝗘𝗣𝗢 •", "https://github.com/itzshukla/STRANGER-SPAM-X/fork")
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
        ShuklaBot = await event.client.get_me()
        bot_name = ShuklaBot.first_name
        bot_id = ShuklaBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛](https://t.me/SHIVANSH39)**\n\n"
        TEXT += f"» **sᴛʀᴀɴɢᴇʀʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/c6a2ed96648fd03377dc9.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )