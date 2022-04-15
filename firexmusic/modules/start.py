from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hi there,👋 {message.from_user.first_name}!
\nThis is firex Music Bot.
I play music on Telegram's Voice Chats.
\nFo More Help Use Buttons Below:
 """,
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/flashokillerify/firexmusic")
                  ],[
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/firextech"
                    ),
                    InlineKeyboardButton(
                        "💻 Support Group", url="https://t.me/firextechchat"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url="https://t.me/FireXmusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""*FireX Music Bot is alive.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/firextech")
                ]
            ]
        )
   )


