import logging
from commands import command_list

from decorators import private
from settings import TOKEN
from telegram.ext import CommandHandler, Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

for name, cmd in command_list:
    handler = CommandHandler(name, cmd)
    dispatcher.add_handler(handler)


# Add help command
@private
def help(bot, update):
    commands = "\n".join(['/{}'.format(n) for n, c in command_list])
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Available Commands: \n{}".format(commands)
    )


handler = CommandHandler('help', help)
dispatcher.add_handler(handler)


# Main loop
updater.start_polling()
