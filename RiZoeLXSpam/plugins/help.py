from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/9acc785291052c8f8998d.jpg"

Riz_Help = "ð¥ ð¦ð£ðð  ð¥\n\n"
 
Riz_Help += f"__á´á´á´s á´á´ á´ÉªÊá´ÊÊá´ ÉªÉ´ ÊÉªá´¢á´á´Ê x sá´á´á´__\n\n"

Riz_Help += f" â§ ððð´ðð±ð¾ð ð²ð¼ð³ð â§\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Riz_Help += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Riz_Help += f"á´ÊÉªá´á´ Êá´Êá´á´¡ Êá´á´á´á´É´ Òá´Ê á´á´Êá´ ÉªÉ´Òá´.\n\n"

Riz_Help += f"Â© @KSKxBOTS | @TheFRiendGroup\n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("á´ÊÊ á´á´á´s", "https://telegra.ph/%F0%9D%97%A5%F0%9D%97%9C%F0%9D%97%AD%F0%9D%97%A2%F0%9D%97%98%F0%9D%97%9F-%F0%9D%97%AB-%F0%9D%97%A6%F0%9D%97%A3%F0%9D%97%94%F0%9D%97%A0-11-28-2")
        ],
        [
        Button.url("á´Êá´É´É´á´Ê", "https://t.me/KSKxBOTS")
        ] 
        ]
        )                                                         
