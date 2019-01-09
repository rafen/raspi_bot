from datetime import datetime, timedelta

from settings import ALLOWED_USERS_IDS


def private(command):
    def new_command(bot, update):
        if update.message.from_user.id in ALLOWED_USERS_IDS:
            command(bot, update)
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="Who are you, {} people?".format(
                    update.message.from_user.id
                )
            )
    return new_command


def time_sensitive(command):
    def new_command(bot, update):
        if datetime.now() - update.message.date < timedelta(seconds=10):
            command(bot, update)
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="Ignored message: '{}' from {}".format(
                    update.message.text,
                    update.message.date
                )
            )
    return new_command
