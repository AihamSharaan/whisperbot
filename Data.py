from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

I am the Master of Whisperers (like Varys in Game of Thrones).
يمكنك استخدامني لإرسال رسائل تهمس إلى صديقك في مجموعات وقنوات (حتى لو لم أكن موجودًا).
فقط هذا الصديق وأنت ستكون قادرًا على قراءة الرسالة على الرغم من وجود آخرين في نفس المجموعة.

لمعرفة كيفية استخدامي ، اضغط على "كيفية الاستخدام" أدناه.

By @S8Y8Y
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 أرسل الهمس 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 العودة للمنزل 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 ارسل الهمس 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("كيف تستعمل ❔", callback_data="help"),
            InlineKeyboardButton("🎪 عن 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ المزيد من البوتات المذهلة ♥", url="https://t.me/S8Y8S")],
        [InlineKeyboardButton("🎨 للابلاغ عن مشكله 🎨", url="https://t.me/N_B_1N")],
    ]

    # Help Message
    HELP = """
ما عليك سوى كتابة الرسالة بالتنسيق أدناه في أي دردشة.

`@WhisperStarkBot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**عن هذا البوت** 

Bot created by @S8Y8S

Source Code : [Click Here](https://github.com/ANES0H/WhisperBot)

Inspired By : nnbbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @S8Y8S
    """
