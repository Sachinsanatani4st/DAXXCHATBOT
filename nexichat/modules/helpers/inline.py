from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER
from nexichat import nexichat

DEV_OP = [
    [
        InlineKeyboardButton(text="⦿ уσυʀ ℓσνє ⦿", user_id=OWNER),
        InlineKeyboardButton(text="⦿ ѕυρρσʀт ⦿", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="⦿ α∂∂ мє вαву ⦿",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="◎ нєℓρ ◎", callback_data="HELP"),
    ],
    [
       # InlineKeyboardButton(text="⦿️ ѕσυʀᴄє ⦿️", callback_data="SOURCE"),
        InlineKeyboardButton(text="⦿️ αвσυт ⦿️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="⦿ α∂∂ мє вαву ⦿ ",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⦿ ᴄℓσѕє ⦿",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⦿ вαᴄк ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄнαт-вσт ⦿", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="⦿ тσσℓѕ ⦿", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⦿ вαᴄк ⦿", callback_data="BACK"),
        InlineKeyboardButton(text="⦿ ᴄℓσѕє ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄℓσѕє ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⦿ вαᴄк ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ ᴄℓσѕє ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ вαᴄк ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ ᴄℓσѕє ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="⦿ нєℓρ ⦿", callback_data="HELP"),
        InlineKeyboardButton(text="⦿ ᴄℓσѕє ⦿", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{nexichat.username}?start=help"
        ),
        InlineKeyboardButton(text="⦿ ᴄℓσѕє ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="⦿ ѕυρρσʀт ⦿", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="⦿ нєℓρ ⦿", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="⦿ уσυʀ ℓσνє ⦿", user_id=OWNER),
     #   InlineKeyboardButton(text="⦿ ѕσυʀᴄє️ ⦿️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="⦿ υρ∂αтєѕ ⦿", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⦿ вαᴄк ⦿", callback_data="BACK"),
    ],
]
