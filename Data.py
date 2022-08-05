from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
مرحبا {}.
اهلا بك في {}

انا بوت همسه).
يمكنك استخدامي لإرسال رسائل تهمسه إلى صديقك في مجموعات وقنوات (حتى لو لم أكن موجودًا).
فقط هذا الصديق وأنت ستكون قادرًا على قراءة الرسالة على الرغم من وجود آخرين في نفس المجموعة.

لمعرفة كيفية استخدامي ، اضغط على "كيفية الاستخدام" أدناه.

By @N_B_1N
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" أرسل الهمسه ", switch_inline_query="")],
        [InlineKeyboardButton(text=" العودة للمنزل ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton(" ارسل الهمسه ", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("كيف تستعمل ❔", callback_data="help"),
            InlineKeyboardButton(" عن ", callback_data="about")
        ],
        [InlineKeyboardButton("♥ المزيد من البوتات ♥", url="https://t.me/S8Y8S")],
        [InlineKeyboardButton(" للابلاغ عن مشكله ", url="https://t.me/N_B_1N")],
    ]

    # Help Message
    HELP = """
ما عليك سوى كتابة الرسالة بالتنسيق أدناه في أي دردشة.

`@HMA2Bot رسالتك USER/ID صديقك`
    """

    # About Message
    ABOUT = """
**عن هذا البوت** 

مطور البوت @N_B_1N

قناه البوت @S8Y8S

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)
    """
