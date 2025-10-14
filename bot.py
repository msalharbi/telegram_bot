import pandas as pd
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load Excel
df = pd.read_excel("problems.xlsx")  # Make sure it's in the same folder
problems = dict(zip(df['Problem'].str.lower(), df['Solution']))

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Send me a problem and I’ll give you the solution.")

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower().strip()
    response = problems.get(user_input, "Sorry, I don't have a solution for that problem.")
    await update.message.reply_text(response)

def main():
    app = Application.builder().token("TOKEN_HERE").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
