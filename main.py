from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Replace this with your bot token from BotFather
BOT_TOKEN = "7596370285:AAEo33rMQMRyTfFKsvTmo-vppjpvqaL5S6E"

# This function will respond the same way to any message
async def static_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cuz You're A Woman 😎")

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Catch all messages with a static response
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, static_response))

print("Bot is running...")
app.run_polling()
