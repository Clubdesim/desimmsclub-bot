
import logging
from typing import Final

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,KeyboardButton, ReplyKeyboardMarkup,InputMediaPhoto, InputMediaVideo
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes,Updater, MessageHandler,filters, CallbackContext

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

TOKEN: Final = '6313265812:AAHJcLQs92u2QmUBKh35vwPMGhEbS4tYmvM'
PRIVATE_CHANNEL_ID = -1002048925926



Mainchannel = InlineKeyboardButton("🌟ᴅᴇꜱɪᴍᴍꜱᴄʟᴜʙ🌟", url="https://t.me/desimmsclub")
PreChannel = InlineKeyboardButton("🌟ᴅᴀɪʟʏ ᴜᴘᴅᴀᴛᴇꜱ ᴘʀᴇᴍɪᴜᴍ🌟", url="https://t.me/+QH-E1xQ-rRxmNjM1")
OFIndChannel = InlineKeyboardButton("🌟ɪɴᴅɪᴀɴ ᴏɴʟʏꜰᴀɴꜱ🌟", url="https://t.me/indianonlyfansexclusive")
OFChannel = InlineKeyboardButton("🌟ᴏɴʟʏꜰᴀɴꜱ ᴍᴇɢᴀ ʟɪɴᴋꜱ🌟", url="https://t.me/+Q85KlRG1Vs42ZmM1")
website = InlineKeyboardButton("★ ᴏᴜʀ ᴡᴇʙꜱɪᴛᴇꜱ ★", url="https://desimmsclub1.blogspot.com/")

Vidchannel = InlineKeyboardButton("🔞 ᴅɪʀᴇᴄᴛ ᴠɪᴅᴇᴏꜱ ᴅᴀɪʟʏ 🔞", url="https://t.me/StreamA2z_Videos")
PdfChannel = InlineKeyboardButton("🔞 ᴀᴅᴜʟᴛ ᴘᴅꜰ ᴅᴀɪʟʏ 🔞", url="https://t.me/Desi_PDF")

earnSite01 = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ ➊",url="https://r.adbtc.top/2715978")
earnSite02 = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ ➋",url="https://viefaucet.com?r=642c826e6b56e9fd87529a07")
earnSite03 = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ ➌",url="https://allfaucet.xyz/?r=18051")
earnSite04 = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ ➍",url="https://larvelfaucet.com/ref/2jj0cEn1")
earnSite05 = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ ➎",url="https://ourcoincash.xyz/?r=39464")
earnSite06 = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ ➏",url="https://earnbitmoon.club/?ref=698055")

earnBot01 = InlineKeyboardButton ("🤖 ᴛʀx ʙᴏᴛ ➊",url="https://t.me/hkearn_trx_bot?start=1042204742")
earnBot02 = InlineKeyboardButton ("🤖 ᴛʀx ʙᴏᴛ ➋",url="https://t.me/ClickBeeBot?start=1042204742")
earnBot03 = InlineKeyboardButton ("🤖 ʟᴛᴄ ʙᴏᴛ ➊",url="https://t.me/hkearn_ltc_bot?start=1042204742")
earnBot04 = InlineKeyboardButton ("🤖 ʟᴛᴄ ʙᴏᴛ ➋",url="https://t.me/ClickBeeLTCBot?start=1042204742")
earnBot05 = InlineKeyboardButton ("🤖 ᴅᴏɢᴇ ʙᴏᴛ ➊",url="https://t.me/hkearn_doge_bot?start=1042204742")
earnBot06 = InlineKeyboardButton ("🤖 ᴅᴏɢᴇ ʙᴏᴛ ➋",url="https://t.me/ClickBeeDOGEBot?start=1042204742")
earnBot07 = InlineKeyboardButton ("🤖 ʙᴛᴄ ʙᴏᴛ",url="https://t.me/HKEarnBTCBot?start=1042204742")
earnBot08 = InlineKeyboardButton ("🤖 ᴇᴛʜ ʙᴏᴛ",url="https://t.me/HKEarnETHBot?start=1042204742")
earnBot09 = InlineKeyboardButton ("🤖 ʙɴʙ ʙᴏᴛ",url="https://t.me/hkearn_bnb_bot?start=1042204742")
earnBot10 = InlineKeyboardButton ("🤖 ᴜꜱᴅᴛ ʙᴏᴛ",url="https://t.me/hkearn_usdt_bot?start=1042204742")
earnBot11 = InlineKeyboardButton ("🤖 ᴍᴀᴛɪᴄ ʙᴏᴛ",url="https://t.me/HKEarnMATICBot?start=1042204742")

wallet = InlineKeyboardButton ("🖥 ꜱɪᴛᴇ ʟɪɴᴋ",url="https://faucetpay.io/?r=958961")

sendLink = InlineKeyboardButton ("📤 ᴜᴘʟᴏᴀᴅ ᴘɪᴄꜱ & ᴠɪᴅᴇᴏꜱ ʜᴇʀᴇ",url="https://mega.nz/filerequest/R3KdzKLOreQ")

status = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
 
    keyboard = [
        [
            InlineKeyboardButton("📝 ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ & ᴛᴇʀᴍꜱ ᴏꜰ ꜱᴇʀᴠɪᴄᴇ",url="https://telegra.ph/Desimmsclub-Bot-11-20" ),
        ],
        [
            InlineKeyboardButton("✔️ ᴀɢʀᴇᴇ", callback_data="yes"),
            InlineKeyboardButton("✖️ ɴᴏᴛ ᴀɢʀᴇᴇ", callback_data="no"),
        ]
    ]
   
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏꜰꜰɪᴄɪᴀʟ ᴅᴇꜱɪᴍᴍꜱᴄʟᴜʙ ʙᴏᴛ !! 🎉\n")
    
    await update.message.reply_text(
       
        "✪ ʙᴇꜰᴏʀᴇ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ, ᴘʟᴇᴀꜱᴇ ᴛᴀᴋᴇ ᴀ ᴍᴏᴍᴇɴᴛ ᴛᴏ ʀᴇᴠɪᴇᴡ ᴏᴜʀ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ & ᴛᴇʀᴍꜱ ᴏꜰ ꜱᴇʀᴠɪᴄᴇ.\n" 
        "━━━━━━━━━━━━━━━\n"
        "\n"
        "ᴄʟɪᴄᴋ 'ᴀɢʀᴇᴇ' ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ ᴏʀ 'ɴᴏᴛ ᴀɢʀᴇᴇ' ɪꜰ ʏᴏᴜ ᴅᴇᴄʟɪɴᴇ."
        , reply_markup=reply_markup) 



async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global PrivacyPolicyConfirmation
    PrivacyPolicyConfirmation = update.callback_query
    
    await PrivacyPolicyConfirmation.answer()
    
    bot = context.bot
    global status
    if PrivacyPolicyConfirmation.data == "no":
        
        
        await PrivacyPolicyConfirmation.edit_message_text(
            text=f"✪ ᴘʟᴇᴀꜱᴇ ᴀɢʀᴇᴇ ᴏᴜʀ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ ᴀɴᴅ ᴛᴇʀᴍꜱ ᴏꜰ ꜱᴇʀᴠɪᴄᴇ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ.\n"
            "ᴄʟɪᴄᴋ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ \n"
            "━━━━━━━━━━━━━━━\n"
            "\n"
            "ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ !!\n")
        return
        
    elif PrivacyPolicyConfirmation.data == "yes":
        
        
         
        joinedStatus = InlineKeyboardButton("Joined", callback_data="done")

        keyboard = [[Mainchannel],[PreChannel],[OFIndChannel],[OFChannel], [joinedStatus]]

        await PrivacyPolicyConfirmation.edit_message_text(
            text="✪ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏᴜʀ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ᴛʜɪꜱ ʙᴏᴛ.\n"
           ,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        
    elif PrivacyPolicyConfirmation.data == "done":

        no=0
        channels = ["@desimmsclub",-1001574818296,-1001620088802]
        
        for i in channels:
            
            chat_id = channels[no]
            user_id = update.effective_user.id
            
            chat_member = await bot.getChatMember(chat_id, user_id)

            if chat_member.status == 'member' or chat_member.status == 'administrator':
                if no == 2:
                    status = 0
                    await PrivacyPolicyConfirmation.message.reply_text(
                        "ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴊᴏɪɴɢ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ !!\n"
                    )

                    commands_keyboard = [
                        [
                            KeyboardButton("⚜️ ᴅᴇꜱɪᴍᴍꜱᴄʟᴜʙ ɴᴇᴛᴡᴏʀᴋ ⚜️"), 
                        ],
                        [
                            KeyboardButton("🎁 ᴘʀᴏᴍᴏᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ 🎁"),
                        ],
                        [
                            KeyboardButton("💰 ᴇᴀʀɴ ᴍᴏɴᴇʏ 💰"),
                        ],
                        [
                            KeyboardButton("📸 ꜱᴇɴᴅ ᴜꜱ ᴘɪᴄꜱ ᴠɪᴅᴇᴏꜱ 🎬"),
                        ],
                        [
                            KeyboardButton("👍🏼 ꜰᴇᴇᴅʙᴀᴄᴋ 👍🏼"),
                        ],
                        [
                            KeyboardButton("©️ ᴅᴍᴄᴀ ©️"),
                        ],
                        
                    ]

                    await PrivacyPolicyConfirmation.message.reply_text(
                        "ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ:",
                        reply_markup=ReplyKeyboardMarkup(commands_keyboard, one_time_keyboard=True),
                    )
            else:
                
                global stat
                stat = "no"
                await PrivacyPolicyConfirmation.message.reply_text(
                    "ᴊᴏɪɴ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ !!\n"
                )
                break

            no = no + 1
    
            


            
       # await PrivacyPolicyConfirmation.edit_message_text(text=f"Selected option: {query.data}")
       # await update.message.reply_text("Please choose:", reply_markup=reply_markup) {PrivacyPolicyConfirmation.data}
async def reStart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        text=f"✪ ᴘʟᴇᴀꜱᴇ ᴀɢʀᴇᴇ ᴏᴜʀ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ ᴀɴᴅ ᴛᴇʀᴍꜱ ᴏꜰ ꜱᴇʀᴠɪᴄᴇ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ᴀɴᴅ ᴊᴏɪɴ ᴏᴜʀ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ\n"
        "ᴄʟɪᴄᴋ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ \n"
        "━━━━━━━━━━━━━━━\n"
        "\n"
        "ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ !!\n")
    return
   
     
async def allChannels_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    

    keyboard = [[Mainchannel],[PreChannel],[OFIndChannel],[OFChannel],[website]]

    await update.message.reply_text(
        text="⚜️ ᴅᴇꜱɪᴍᴍꜱᴄʟᴜʙ ɴᴇᴛᴡᴏʀᴋ ⚜️",
        reply_markup=InlineKeyboardMarkup(keyboard),
        )
    
async def promoChannels_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = [[Vidchannel],[PdfChannel]]

    await update.message.reply_text(
        text="🎁 ᴘʀᴏᴍᴏᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ 🎁\n"
            "━━━━━━━━━━━━━━━\n"
            "✪ ʏᴏᴜ ꜱʜᴏᴜʟᴅ ʙᴇ 18+ ᴛᴏ ᴊᴏɪɴ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ'ꜱ\n"
            "✪ ᴛʜɪꜱ ᴀʀᴇ ᴘʀᴏᴍᴏᴛɪᴏɴ ᴄʜᴀɴɴᴇʟꜱ ꜱᴏ ᴊᴏɪɴ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪꜱᴋ.",
 
        reply_markup=InlineKeyboardMarkup(keyboard),
        )
 
async def earnMoney_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands_keyboard = [
        [
            KeyboardButton("🖥 ꜱɪᴛᴇꜱ 🖥"), 
        ],
        [
            KeyboardButton("🤖 ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛꜱ 🤖"),
        ],
        [
            KeyboardButton("💲 ᴡᴀʟʟᴇᴛ 💲"),
        ],
        [
            KeyboardButton("⬅️ ʙᴀᴄᴋ"),
        ]
        ]

    await update.message.reply_text(
        "ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ:",
            reply_markup=ReplyKeyboardMarkup(commands_keyboard, one_time_keyboard=True),
            )    
    
    
async def earnMoneySites(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = [[earnSite01,earnSite02],
                [earnSite03,earnSite04],
                [earnSite05,earnSite06]]

    await update.message.reply_text(
        text="💰ᴜꜱᴇ ᴛʜɪꜱ ꜱɪᴛᴇꜱ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴅɪꜰꜰᴇʀᴇɴᴛ ᴛʏᴘᴇꜱ ᴏꜰ ᴄʀʏᴘᴛᴏ ᴄᴏɪɴꜱ ᴛᴏ ʏᴏᴜʀ ꜰᴀᴜᴄᴇᴛᴘᴀʏ ᴡᴀʟʟᴇᴛ ᴅᴀɪʟʏ !!\n"
                "━━━━━━━━━━━━━━━\n"
                "✅ ᴇᴀꜱʏ ꜱɪɢɴ ᴜᴘ\n"
                "✅ ᴇᴀʀɴ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴀᴅꜱ\n"
                "✅ ᴇᴀʀɴ ʙʏ ꜰᴀᴜᴄᴇᴛ ᴄᴏʟʟᴇᴄᴛ\n"
                "✅ ᴇᴀʀɴ ʙʏ ꜱʜᴏʀᴛ ʟɪɴᴋꜱ\n"
                "✅ ᴇᴀʀɴ ʙʏ ꜱᴜʀᴠᴇʏꜱ\n"
                "✅ ᴇᴀʀɴ ʙʏ ᴅᴀɪʟʏ ʙᴏɴᴜꜱ\n"
                "✅ ᴇᴀʀɴ ʙʏ ꜱɪᴍᴘʟᴇ ᴛᴀꜱᴋꜱ\n"
                "✅ ᴍɪɴɪᴍᴜᴍ ꜰᴀꜱᴛ ᴡɪᴛʜᴅʀᴀᴡ\n"
                "✅ ᴅᴀɪʟʏ ᴇᴀʀɴ & ᴡɪᴛʜᴅʀᴀᴡ'n"
                "💰ᴇᴀʀɴ ᴜᴘ ᴛᴏ 𝟭𝟬$ ᴡᴏʀᴛʜ ᴄʀʏᴘᴛᴏ ᴍᴏɴᴛʜʟʏ\n"

        ,reply_markup=InlineKeyboardMarkup(keyboard),
        )
    
async def earnMoneyBots(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = [[earnBot01,earnBot02],
                [earnBot03,earnBot04],
                [earnBot05,earnBot06],
                [earnBot07],
                [earnBot08,earnBot09],
                [earnBot10,earnBot11]]

    await update.message.reply_text(
        text="💰ᴜꜱᴇ ᴛʜɪꜱ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛꜱ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴅɪꜰꜰᴇʀᴇɴᴛ ᴛʏᴘᴇꜱ ᴏꜰ ᴄʀʏᴘᴛᴏ ᴄᴏɪɴꜱ ᴛᴏ ʏᴏᴜʀ ꜰᴀᴜᴄᴇᴛᴘᴀʏ ᴡᴀʟʟᴇᴛ ᴅᴀɪʟʏ !!\n"       
        ,reply_markup=InlineKeyboardMarkup(keyboard),
        )
    

async def earnMoneyWallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    keyboard = [[wallet]]
    
    await update.message.reply_text(
        text="🤔 ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀ ᴄʀʏᴘᴛᴏ ᴡᴀʟʟᴇᴛ ?\n"
            "ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴡᴀʟʟᴇᴛ ɴᴏᴡ !!\n"       
            "\n"
            "✅ ᴀʟʟ ꜰᴀᴜᴄᴇᴛ ꜱɪᴛᴇ ꜱᴜᴘᴘᴏʀᴛ\n"
            "✅ ꜱᴜᴘᴘᴏʀᴛ 16 ᴅɪꜰꜰᴇʀᴇɴᴛ ᴄᴏɪɴꜱ\n"
            "✅ ᴇᴀꜱʏ ᴡɪᴛʜᴅʀᴀᴡ & ᴄᴏɪɴ ꜱᴡᴀᴘ\n"
            "✅ ᴍᴏꜱᴛ ᴜꜱᴇᴅ ᴄʀʏᴛᴏ ᴡᴀʟʟᴇᴛ\n"
        
        
        ,reply_markup=InlineKeyboardMarkup(keyboard),
        )
    
    
async def sendUs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    keyboard = [[sendLink]]
   
    await update.message.reply_text(
        text="🎬 ꜱᴇɴᴅ ᴜꜱ ʏᴏᴜʀ ᴘɪᴄꜱ & ᴠɪᴅᴇᴏꜱ !!\n"
            "ᴍᴀᴋᴇ ʏᴏᴜʀ ɢɪʀʟ ꜰᴀᴍᴏᴜꜱ !! 💃\n"
            "━━━━━━━━━━━━━━━\n"

            "🌟 ᴡᴇ ᴡɪʟʟ ᴘᴏꜱᴛ ᴛʜᴇᴍ ᴏɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ & ꜱɪᴛᴇꜱ.\n"
            "ɪᴍᴘᴏʀᴛᴀɴᴛ : ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ʏᴏᴜ ꜱʜᴇᴀʀɪɴɢ ᴡɪᴛʜ ᴜꜱ ᴡɪʟʟ ʙᴇ ᴘᴏꜱᴛ ᴏɴ ꜰᴇᴡ ᴘʟᴀᴛꜰᴏʀᴍꜱ ɪɴᴄʟᴜᴅɪɴɢ ɪɴᴛᴇʀɴᴇᴛ ᴀɴᴅ ᴡᴇ ᴅᴏ ɴᴏᴛ ʀᴇꜱᴘᴏɴꜱɪʙʟᴇ ꜰᴏʀ ᴀɴʏ ᴏꜰ ᴛʜᴀᴛ. ꜱᴏ ꜱᴇɴᴅ ʏᴏᴜʀ ᴘɪꜱᴄ ᴠɪᴅᴇᴏꜱ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪꜱᴋ"
                    
        
        ,reply_markup=InlineKeyboardMarkup(keyboard),
        )
    
async def feedBack(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    await update.message.reply_text(
        text=f"😊 ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴛʜɪɴᴋ ᴏꜰ ᴏᴜʀ ꜱᴇʀᴠɪᴄᴇ?\n"
            "━━━━━━━━━━━━━━━\n"
            "😉 ᴡʀɪᴛᴇ ᴛᴏ ᴜꜱ ʏᴏᴜʀ ɪᴅᴇᴀꜱ, ᴀɴʏᴛʜɪɴɢ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ꜱᴀʏ ᴛᴏ ᴜꜱ.. ᴡᴇ ᴀʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀᴡᴀʀᴅ ᴛᴏ ʜᴇᴀʀ ɪᴛ 👍\n"
            "\n"
            "ᴇᴍᴀɪʟ ᴛᴏ desimmsclub@gmail.com ᴀɴᴅ ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴛʏᴘᴇ ꜰᴇᴇᴅʙᴀᴄᴋ ᴀꜱ ꜱᴜʙᴊᴇᴄᴛ ʙᴇꜰᴏʀᴇ ʏᴏᴜ ᴇᴍᴀɪʟ ɪᴛ ᴛᴏ ᴜꜱ.. ᴜɴʟᴇꜱꜱ ᴏᴜʀ ᴛᴇᴀᴍ ᴡɪʟʟ ᴀᴠᴏɪᴅ ɪᴛ.\n"
            "\n"
            "ᴛʜᴀɴᴋ ʏᴏᴜ !!\n"
        )
    
async def dmca(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    await update.message.reply_text(
        text=f"🔴 ᴅᴍᴄᴀ ᴛᴀᴋᴇ ᴅᴏᴡɴ !!\n"
"━━━━━━━━━━━━━━━\n"

"ᴛᴏ ᴄʟᴀɪᴍ ᴅᴍᴄᴀ ᴀɴᴅ ᴛᴀᴋᴇ ᴅᴏᴡɴ ᴀɴʏ ᴘᴏꜱᴛ ᴛʜᴀᴛ ᴡᴇ ꜱʜᴀʀᴇᴅ ᴛʜʀᴏᴜɢʜ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ, ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴇᴍᴀɪʟ ᴛᴏ ᴏᴜʀ ᴇᴍᴀɪʟ ᴡɪᴛʜ ᴛʜᴇ ʙᴇʟᴏᴡ ʀᴇQᴜɪʀᴇᴅ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.\n"
"\n"
"🔰 ʏᴏᴜʀ ꜰᴜʟʟ ɴᴀᴍᴇ\n"
"🔰 ʏᴏᴜʀ ᴀɢᴇ\n"
"🔰 ʏᴏᴜʀ ᴇᴍᴀɪʟ\n "
"🔰 ᴅᴍᴄᴀ ᴄʟᴀɪᴍ (ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ɪᴅᴇɴᴛɪꜰʏ ᴛʜᴀᴛ ᴘᴏꜱᴛ ɪꜱ ʏᴏᴜʀꜱ)\n"
"🔰 ʀᴇᴀꜱᴏɴ ᴛᴏ ᴛᴀᴋᴇ ᴅᴏᴡɴ\n"
"🔰 ꜱᴄʀᴇᴇɴ ꜱʜᴏᴛꜱ ᴏꜰ ᴛʜᴇ ᴘᴏꜱᴛ ʏᴏᴜ ʀᴇꜰᴇʀʀɪɴɢ ( ᴊᴜꜱᴛᴘᴀꜱᴛᴇ ꜱɪᴛᴇ ꜱᴄʀᴇᴇɴꜱʜᴏᴛꜱ )\n"
"\n"
"ᴇᴍᴀɪʟ ᴛᴏ desimmsclub@gmail.com ᴡɪᴛʜ ᴛʜᴇꜱᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴛʏᴘᴇ ᴅᴍᴄᴀ ᴀꜱ ꜱᴜʙᴊᴇᴄᴛ ʙᴇꜰᴏʀᴇ ʏᴏᴜ ᴇᴍᴀɪʟ ɪᴛ ᴛᴏ ᴜꜱ.. ᴜɴʟᴇꜱꜱ ᴏᴜʀ ᴛᴇᴀᴍ ᴡɪʟʟ ᴀᴠᴏɪᴅ ɪᴛ.\n"
"\n"
"ᴡᴇ ᴡɪʟʟ ᴄᴏɴᴛᴀᴄᴛ ʏᴏᴜ ᴡɪᴛʜ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴇᴍᴀɪʟ ᴀɴᴅ ᴍᴀʏ ᴀꜱᴋ ꜰᴇᴡ Qᴜᴇꜱᴛɪᴏɴꜱ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴅᴍᴄᴀ ᴄʟᴀɪᴍ ᴛʜᴇɴ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴛᴀᴋᴇ ɪᴛ ᴅᴏᴡɴ..\n"
"\n"
"ᴛʜᴀɴᴋ ʏᴏᴜ !!\n"
        )
    
    
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    commands_keyboard = [
        [
            KeyboardButton("⚜️ ᴅᴇꜱɪᴍᴍꜱᴄʟᴜʙ ɴᴇᴛᴡᴏʀᴋ ⚜️"), 
        ],
        [
            KeyboardButton("🎁 ᴘʀᴏᴍᴏᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ 🎁"),
        ],
        [
            KeyboardButton("💰 ᴇᴀʀɴ ᴍᴏɴᴇʏ 💰"),
        ],
        [
            KeyboardButton("📸 ꜱᴇɴᴅ ᴜꜱ ᴘɪᴄꜱ ᴠɪᴅᴇᴏꜱ 🎬"),
        ],
        [
            KeyboardButton("👍🏼 ꜰᴇᴇᴅʙᴀᴄᴋ 👍🏼"),
        ],
        [
            KeyboardButton("©️ ᴅᴍᴄᴀ ©️"),
        ],
                        
        ]

    await update.message.reply_text(
        text=f"ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ:",
            reply_markup=ReplyKeyboardMarkup(commands_keyboard, one_time_keyboard=True),
        )
    

    

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if '⚜️ ᴅᴇꜱɪᴍᴍꜱᴄʟᴜʙ ɴᴇᴛᴡᴏʀᴋ ⚜️' in processed:
        return 'allChannels_command'
    
    if '🎁 ᴘʀᴏᴍᴏᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ 🎁' in processed:
        return 'promoChannels_command'
    
    if '💰 ᴇᴀʀɴ ᴍᴏɴᴇʏ 💰' in processed:
        return 'earnMoney_command'
    
    if '🖥 ꜱɪᴛᴇꜱ 🖥' in processed:
        return 'earnMoneySites'
    
    if '🤖 ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛꜱ 🤖' in processed:
        return 'earnMoneyBots'
    
    if '💲 ᴡᴀʟʟᴇᴛ 💲' in processed:
        return 'earnMoneyWallet'
    
    if '⬅️ ʙᴀᴄᴋ' in processed:
        return 'menu'
    
    if '📸 ꜱᴇɴᴅ ᴜꜱ ᴘɪᴄꜱ ᴠɪᴅᴇᴏꜱ 🎬' in processed:
        return 'sendUs'
    
    if '👍🏼 ꜰᴇᴇᴅʙᴀᴄᴋ 👍🏼' in processed:
        return 'feedBack'
    
    if '©️ ᴅᴍᴄᴀ ©️' in processed:
        return 'dmca'    
    
    return 'I do not understand it'

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text: str = update.message.text
    
    '''print(f'User({update.message.chat.id}) in {message_type}: " {text}"')'''
    
    
    response= handle_response(text)
    
    if status == 1:
        await reStart(update, context)
    else:
        if response == 'allChannels_command':
            await allChannels_command(update, context)
        elif response == "promoChannels_command":
            await promoChannels_command(update, context)
        elif response == "earnMoney_command":
            await earnMoney_command(update, context)
            
        elif response == "earnMoneySites":
            await earnMoneySites(update, context)
        elif response == "earnMoneyBots":
            await earnMoneyBots(update, context)
        elif response == "earnMoneyWallet":
            await earnMoneyWallet(update, context)
            
        elif response == "menu":
            await menu(update, context)
            
        elif response == "sendUs":
            await sendUs(update, context)    
        elif response == "feedBack":
            await feedBack(update, context) 
        elif response == "dmca":
            await dmca(update, context)
            
            
        else:
            await update.message.reply_text(response)
        

def main() -> None:
    
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.add_handler(CommandHandler("channels", allChannels_command))
    application.add_handler(CommandHandler("promoted", promoChannels_command))
    application.add_handler(CommandHandler("earn", earnMoney_command))
    application.add_handler(CommandHandler("send", sendUs))
    application.add_handler(CommandHandler("feedback", feedBack))
    application.add_handler(CommandHandler("copyright", dmca))

    application.add_handler(MessageHandler(filters.TEXT,handle_messages))


    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()