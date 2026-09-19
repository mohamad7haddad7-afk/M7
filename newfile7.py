import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Your bot token
TOKEN = "8386757122:AAGTIlu962P8Yw8peRReyKVvFz-0S6o3DfQ"

# Payment code or wallet address
PAYMENT_CODE = "0x038edc0ff2670a8ef48eff5f866d04cee787efd9"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create the inline button
    keyboard = [
        [InlineKeyboardButton("Show Payment Address 💳", callback_data="show_payment")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the logo photo with caption and button
    with open("logo.Jpg", "rb") as photo_file:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo_file,
            caption="Welcome! Click the button below to get the payment address:",
            reply_markup=reply_markup
        )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "show_payment":
        # Send payment code with HTML formatting for easy copying
        await query.message.reply_text(
            f"<b>Your Payment Address (BEP20 - Binance):</b>\n<code>{PAYMENT_CODE}</code>\n\n(Tap the address above to copy and send the funds)",
            parse_mode="HTML"
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()
