import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Define the start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm ChatGPT Bot. Ask me anything!")

# Define a function to handle messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        # Call OpenAI's GPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
        )
        reply = response['choices'][0]['message']['content']
        update.message.reply_text(reply)
    except Exception as e:
        logging.error(f"Error: {e}")
        update.message.reply_text("Sorry, I couldn't process your request. Please try again later.")

# Main function to set up the bot
def main():
    # Your Telegram bot token
    TELEGRAM_TOKEN = "7202462788:AAFPaTQpSobueeHB_yxxJhMzlXz3mIk3fiE"

    # Set up the Updater
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
