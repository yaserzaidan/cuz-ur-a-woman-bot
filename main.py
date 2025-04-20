from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def static_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cuz Your're A Woman 😎")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, static_response))

print("Bot is running...")
app.run_polling()
