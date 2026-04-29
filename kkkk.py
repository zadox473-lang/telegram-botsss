import asyncio
import json
import os
import random
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

# ---------------------------
# CONFIG
# ---------------------------
TOKENS = [
    "8598475680:AAGL83MFJjooS8pvca3nFUp8ORlo3VXqhlM",
    "8412182639:AAGAi34TgCiwJqBrRt_yRaI-yRWtNPbSkf4",
    "8651760309:AAE1G721KOaUnRLyjM3Lj5qCJNLMartF1x8",
    "8743347235:AAHCGZi9qiZbrIZBROfgdgFv-d8BmILZsrM",
    "8236012068:AAG87ItwklhppnorP2kedn-SOHfNdVuJNIc",
    "8760396691:AAFBmTZDooB67oHJK3xawhIkCZaDqnln2Gg",
    "8621431374:AAHflAs4DjYiVzCpZeqKubtbxcSYZy3lBeA",
    "8706272380:AAEaqaj1wZL8PLKMDAkEjVqctlZbx3bNjXE",
    "8617207286:AAH6xvLRs3JfZ15ve-Y7aN_2UlUm-lgJDY4",
]

OWNER_ID = 8602543306
SUDO_FILE = "sudo.json"

# ---------------------------
# SIMPLIFIED TEXT LISTS (Fixed)
# ---------------------------
RAID_TEXTS = ["RND", "NICHI JAAT", "HAKLE", "TMKC", "BAUNE", "BITCH", "CHUD", "TMKB", "KAMZOR", "TATTI KHA", "CHINNAL", "MOTE", "GAREEB", "HIJDE", "LAND LE", "TERI MA RNDI", "CVR KR", "MAR MAT", "BHAGA", "KIDEE", "ANDHE LODE"]

NCEMO_EMOJIS = ["🐕", "🐈", "🐒", "🐖", "🐪", "🦒", "🦓", "🐄", "🐏", "🦍", "🐘", "🦏", "🦙", "🐫", "🦘", "🐅", "🐆", "🦌", "🦩", "🦢", "🐧", "🦅", "🦚", "🦜", "🐝", "🦋", "🐌", "🐞", "🦗", "🕷️", "🦂", "🐠", "🐟", "🐡", "🐙", "🦑", "🐬", "🐳", "🦈", "🦭", "🐉", "🦕", "🦖"]

HEART_EMOJIS = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💖", "💗", "💓", "💕", "💞", "💘", "💝", "💟"]

ANIMAL_EMOJIS = ["🐕", "🐈", "🐒", "🐖", "🐪", "🦒", "🦓", "🐄", "🐏", "🦍", "🐘", "🦏", "🦙", "🐫", "🦘", "🐅", "🐆", "🦌"]

MASK_EMOJIS = ["😉", "😗", "😙", "😚", "😘", "🥰", "😍", "😋", "😛", "😝", "😜", "🤪"]

# ---------------------------
# STATE
# ---------------------------
SUDO_USERS = {OWNER_ID}
GLOBAL_DELAY = 0.1

if os.path.exists(SUDO_FILE):
    try:
        with open(SUDO_FILE, "r") as f:
            SUDO_USERS.update(int(x) for x in json.load(f))
    except:
        pass

group_tasks = {}
bots_data = []
logging.basicConfig(level=logging.INFO)

# ---------------------------
# HELPERS
# ---------------------------
def only_sudo(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.effective_user or update.effective_user.id not in SUDO_USERS:
            await update.message.reply_text("❌ You are not authorized!")
            return
        return await func(update, context)
    return wrapper

async def bot_loop(bot, chat_id, base, mode, reply_to_id=None):
    i = 0
    mapping = {
        "raid": RAID_TEXTS,
        "ncemo": NCEMO_EMOJIS,
        "heartloop": HEART_EMOJIS,
        "animal": ANIMAL_EMOJIS,
        "mask": MASK_EMOJIS,
    }
    
    text_list = mapping.get(mode, RAID_TEXTS)
    
    while True:
        try:
            txt = f"{base} {text_list[i % len(text_list)]}"
            
            if mode in ["ncemo", "heartloop", "animal", "mask"]:
                await bot.set_chat_title(chat_id, txt)
            else:
                await bot.send_message(chat_id, txt, reply_to_message_id=reply_to_id)
            
            i += 1
            await asyncio.sleep(GLOBAL_DELAY)
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(1)

# ---------------------------
# HANDLERS
# ---------------------------
@only_sudo
async def start_cmd(update, context):
    await update.message.reply_text("🚀 Bot is running! Use /help for commands.")

@only_sudo
async def help_cmd(update, context):
    help_text = """
📌 **Available Commands:**

/raid <word> - Spam word
/ncemo <word> - Change group title with emojis
/heartloop <word> - Heart emoji title loop
/animal <word> - Animal emoji title loop
/mask <word> - Mask emoji title loop

/stopall - Stop all tasks in current chat
/status - Check active tasks
/delay <seconds> - Change speed (default: 0.1s)

⚡ Fast mode enabled!
    """
    await update.message.reply_text(help_text)

@only_sudo
async def stopall(update, context):
    cid = update.message.chat_id
    if cid in group_tasks:
        for t in group_tasks[cid].values():
            t.cancel()
        group_tasks[cid] = {}
    await update.message.reply_text("🛑 All tasks stopped!")

@only_sudo
async def status(update, context):
    cid = update.message.chat_id
    active = group_tasks.get(cid, {})
    if not active:
        return await update.message.reply_text("No active tasks.")
    await update.message.reply_text(f"Active: {', '.join(active.keys())}")

@only_sudo
async def set_delay(update, context):
    global GLOBAL_DELAY
    if not context.args:
        return await update.message.reply_text(f"Current delay: {GLOBAL_DELAY}s\nUse /delay <seconds>")
    try:
        GLOBAL_DELAY = float(context.args[0])
        await update.message.reply_text(f"✅ Speed: {GLOBAL_DELAY}s")
    except ValueError:
        await update.message.reply_text("❌ Invalid number!")

@only_sudo
async def handle_loop(update, context):
    text = update.message.text
    if not text:
        return
    
    cmd = text.split()[0][1:].split("@")[0]
    mode = cmd
    
    if not context.args:
        return await update.message.reply_text(f"/{mode} <text>")
    
    base = " ".join(context.args)
    cid = update.message.chat_id
    
    reply_to_id = None
    if update.message.reply_to_message:
        reply_to_id = update.message.reply_to_message.message_id
    
    group_tasks.setdefault(cid, {})
    
    for bot_info in bots_data:
        task_key = f"{bot_info['id']}_{mode}"
        if task_key not in group_tasks[cid]:
            bot = Application.builder().token(bot_info['token']).build().bot
            group_tasks[cid][task_key] = asyncio.create_task(bot_loop(bot, cid, base, mode, reply_to_id))
    
    await update.message.reply_text(f"{mode.upper()} ACTIVE on all bots!")

# ---------------------------
# MAIN
# ---------------------------
async def main():
    global bots_data
    apps = []
    
    for token in TOKENS:
        try:
            app = Application.builder().token(token).build()
            bot_obj = await app.bot.get_me()
            bots_data.append({'id': bot_obj.id, 'token': token})
            
            # Add handlers
            app.add_handler(CommandHandler("start", start_cmd))
            app.add_handler(CommandHandler("help", help_cmd))
            app.add_handler(CommandHandler("stopall", stopall))
            app.add_handler(CommandHandler("status", status))
            app.add_handler(CommandHandler("delay", set_delay))
            
            # Loop commands
            for m in ["raid", "ncemo", "heartloop", "animal", "mask"]:
                app.add_handler(CommandHandler(m, handle_loop))
            
            await app.initialize()
            await app.start()
            
            if app.updater:
                await app.updater.start_polling()
            
            apps.append(app)
            print(f"✅ Bot @{bot_obj.username} started!")
            
        except Exception as e:
            print(f"❌ Error starting bot: {e}")
    
    if not bots_data:
        print("No bots started!")
        return
    
    print("🚀 All bots running...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
