from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final[str] = '6632957712:AAFFJoEJ2e-9cBIctitgZMjhfBvtxxOr0lY'
BOT_USERNAME: Final[str] = '@YourPersonalJarvisBot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! Nice to meet you. Let\'s chat.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am ready! Let me know how I can help.')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Begin a custom command.')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if any(greeting in processed for greeting in ['hello', 'hey', 'hi']):
        return 'Hey there!'

    if any(greeting in processed for greeting in ['how are you', 'how is it going', 'what\'s up']):
        return 'I am well, thank you for asking!'

    if any(greeting in processed for greeting in ['do you like Python?', 'do you enjoy python?']):
        return 'Python is the best tool in the world!'

    return 'I do not understand...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User -- {update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return

    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')


def main():
    print('Starting up the bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=2)


if __name__ == '__main__':
    main()



# Potential add-ons
  # 1. Experiment with it.
  # 2. Script must be running to respond. If you want to host, look for hosting python services.