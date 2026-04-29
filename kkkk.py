import asyncio
import json
import os
import random
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# CONFIG
TOKENS = [
    "8236012068:AAFNu_lVLp8u0IzCqVki6bHLpWrG7ssYUqM",
    "8760396691:AAG92xda9deZLByYQQMLkZyyqqp3MQzpLXI",
    "8621431374:AAEps8MLGYRW7cNDcRCp-yu7WqErcMVNyx0",
    "8706272380:AAFVbxnKLRUgQFDQJ1AH25QPFJ5eMTg2g4Y",
    "8412182639:AAGAi34TgCiwJqBrRt_yRaI-yRWtNPbSkf4",
    "8743347235:AAHkiME7wDz_TSOkGhZyF616bduEbBBAh8E",
    "8651760309:AAE3ccUzWi2incOx8KJBiNz1gllVdJ9m8BU",
    "8668142941:AAFNSBvnULs0kxK89bOYd8MuYteZiWCyYvw",
]

OWNER_ID = 8625596680
SUDO_FILE = "sudo.json"

# TEXT LISTS (Fixed)
RAID_TEXTS = ["RND", "NICHI JAAT", "HAKLE", "TMKC", "BAUNE", "CHUD", "KAMZOR", "TATTI KHA", "CHINNAL", "MOTE", "GAREEB", "HIJDE", "LAND LE", "TERI MA RNDI"]

NCEMO_EMOJIS = ["🐕", "🐈", "🐒", "🐖", "🐪", "🦒", "🦓", "🐄", "🐏", "🦍", "🐘", "🦏", "🐫", "🦘", "🐅", "🐆", "🦌", "🦩", "🦢", "🐧", "🦅", "🦚", "🦜"]

HEART_EMOJIS = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💖"]

ANIMAL_EMOJIS = ["🐕", "🐈", "🐒", "🐖", "🐪", "🦒", "🦓", "🐄", "🐏", "🦍"]

# STATE
SUDO_USERS = {OWNER_ID}
group_tasks = {}
bots_data = []
logging.basicConfig(level=logging.INFO)

def only_sudo(func):
    async def wrapper(update, context):
        if not update.effective_user or update.effective_user.id not in SUDO_USERS:
            await update.message.reply_text("❌ Not authorized!")
            return
        return await func(update, context)
    return wrapper

async def bot_loop(bot, chat_id, base, mode):
    i = 0
    mapping = {
        "raid": RAID_TEXTS,
        "ncemo": NCEMO_EMOJIS,
        "heartloop": HEART_EMOJIS,
        "animal": ANIMAL_EMOJIS,
    }
    text_list = mapping.get(mode, RAID_TEXTS)
    while True:
        try:
            txt = f"{base} {text_list[i % len(text_list)]}"
            if mode in ["ncemo", "heartloop", "animal"]:
                await bot.set_chat_title(chat_id, txt)
            else:
                await bot.send_message(chat_id, txt)
            i += 1
            await asyncio.sleep(0.1)  # Fixed delay
        except:
            await asyncio.sleep(1)

@only_sudo
async def start_cmd(update, context):
    await update.message.reply_text("🚀 Bot is running!")

@only_sudo
async def help_cmd(update, context):
    await update.message.reply_text("/raid\n/ncemo\n/heartloop\n/animal\n/stopall\n/status\n/ping")

@only_sudo
async def ping_cmd(update, context):
    await update.message.reply_text("🏓 PONG!")

@only_sudo
async def stopall(update, context):
    cid = update.message.chat_id
    if cid in group_tasks:
        for t in group_tasks[cid].values():
            t.cancel()
        group_tasks[cid] = {}
    await update.message.reply_text("🛑 Stopped!")

@only_sudo
async def status(update, context):
    cid = update.message.chat_id
    active = group_tasks.get(cid, {})
    if not active:
        await update.message.reply_text("No active tasks")
    else:
        await update.message.reply_text(f"Active: {', '.join(active.keys())}")

@only_sudo
async def handle_loop(update, context):
    cmd = update.message.text.split()[0][1:].split("@")[0]
    if not context.args:
        await update.message.reply_text(f"/{cmd} <text>")
        return
    base = " ".join(context.args)
    cid = update.message.chat_id
    group_tasks.setdefault(cid, {})
    for bot_info in bots_data:
        task_key = f"{bot_info['id']}_{cmd}"
        if task_key not in group_tasks[cid]:
            bot = Application.builder().token(bot_info['token']).build().bot
            group_tasks[cid][task_key] = asyncio.create_task(bot_loop(bot, cid, base, cmd))
    await update.message.reply_text(f"{cmd.upper()} active!")

async def main():
    global bots_data
    for token in TOKENS:
        try:
            app = Application.builder().token(token).build()
            bot_obj = await app.bot.get_me()
            bots_data.append({'id': bot_obj.id, 'token': token})
            app.add_handler(CommandHandler("start", start_cmd))
            app.add_handler(CommandHandler("help", help_cmd))
            app.add_handler(CommandHandler("ping", ping_cmd))
            app.add_handler(CommandHandler("stopall", stopall))
            app.add_handler(CommandHandler("status", status))
            for m in ["raid", "ncemo", "heartloop", "animal"]:
                app.add_handler(CommandHandler(m, handle_loop))
            await app.initialize()
            await app.start()
            if app.updater:
                await app.updater.start_polling()
            print(f"✅ Bot @{bot_obj.username} started!")
        except Exception as e:
            print(f"❌ Error: {e}")
    print("🚀 All bots running!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
