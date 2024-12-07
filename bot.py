import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set your API keys
TELEGRAM_TOKEN = "7202462788:AAFPaTQpSobueeHB_yxxJhMzlXz3mIk3fiE"
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your ChatGPT-powered bot. Ask me anything!")

# Handle user messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        # Call ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        update.message.reply_text(reply)
    except Exception as e:
        logger.error(f"Error: {e}")
        update.message.reply_text("Sorry, I couldn't process your request. Please try again later.")

# Main function to start the bot
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
